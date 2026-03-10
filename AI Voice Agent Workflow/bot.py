from flask import Flask, request, send_file
from faster_whisper import WhisperModel
from gtts import gTTS
import requests
import subprocess
import os

app = Flask(__name__)

# Initialize Whisper Model (Base)
whisper = WhisperModel("base", device="cpu", compute_type="int8")

OLLAMA_URL = "http://localhost:11434/api/generate"
conversation_history = []

def speech_to_text(audio_file):
    segments, _ = whisper.transcribe(audio_file, beam_size=5)
    return "".join([segment.text for segment in segments]).strip()

def ask_ai(question):
    global conversation_history
    conversation_history.append(f"Customer: {question}")

    prompt = f"You are a friendly customer support voice assistant. Speak naturally. Short responses.\n\n"
    prompt += "\n".join(conversation_history[-5:]) # Keep last 5 exchanges

    response = requests.post(
        OLLAMA_URL,
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )
    answer = response.json().get("response", "").strip()
    conversation_history.append(f"Assistant: {answer}")
    return answer

@app.route("/voice-support", methods=["POST"])
def voice_support():
    if "audio" not in request.files:
        return "No audio file", 400

    audio = request.files["audio"]
    audio.save("input.m4a")

    # Convert M4A to WAV using subprocess
    subprocess.run(["ffmpeg", "-y", "-i", "input.m4a", "input.wav"], check=True)

    text = speech_to_text("input.wav")
    answer = ask_ai(text)

    # Text to Speech
    tts = gTTS(text=answer, lang="en")
    tts.save("reply.mp3")

    # Convert MP3 to WAV for return
    subprocess.run(["ffmpeg", "-y", "-i", "reply.mp3", "reply.wav"], check=True)

    return send_file("reply.wav", mimetype="audio/wav")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
