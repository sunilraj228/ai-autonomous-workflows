# 🎙️ AI Voice Support Assistant (Ollama + Whisper)

An end-to-end **Voice AI Agent** deployed on **AWS EC2** that transcribes human speech, processes it using a local LLM (**Llama3**), and responds with synthesized speech.

This project demonstrates a full-stack integration of:

- **Speech-to-Text (STT)**
- **Large Language Models (LLM)**
- **Text-to-Speech (TTS)**

The system converts **speech → reasoning → speech**, creating a conversational voice assistant.

---

# 🛠️ Tech Stack

| Component | Technology |
|--------|-------------|
| Cloud Infrastructure | AWS EC2 (t3.large), Ubuntu 22.04 |
| AI Engine | Ollama running Llama3 |
| Speech-to-Text | Faster-Whisper |
| Text-to-Speech | Google TTS (gTTS) |
| Backend | Flask (Python) |
| Media Processing | FFmpeg |

---

# 🏗️ Architecture

The system follows a **Speech → AI → Speech pipeline**.

User Voice (.m4a)  
        ↓  
Flask API (AWS EC2)  
        ↓  
FFmpeg converts audio  
        ↓  
Faster-Whisper (Speech-to-Text)  
        ↓  
Llama3 via Ollama (LLM reasoning)  
        ↓  
gTTS (Text-to-Speech)  
        ↓  
Voice Response (.wav)

---

# 🚀 Installation & Setup

## 1️⃣ EC2 Environment Setup

Connect to your Ubuntu instance and install system dependencies.

sudo apt update && sudo apt upgrade -y  
sudo apt install python3-pip python3-venv python3-full ffmpeg git -y

---

## 2️⃣ Install & Configure Ollama

Ollama serves as the **local inference engine** for the Llama3 model.

Install Ollama:

curl -fsSL https://ollama.com/install.sh | sh

Pull the Llama3 model (~4.7 GB):

ollama pull llama3

Start Ollama server:

nohup ollama serve &

Verify Ollama is running:

ps aux | grep ollama

---

## 3️⃣ Application Setup

Clone the repository and prepare the Python environment.

git clone https://github.com/YOUR_USERNAME/voice-assistant-ollama.git  
cd voice-assistant-ollama

Create a virtual environment:

python3 -m venv venv  
source venv/bin/activate

Install Python dependencies:

pip install flask faster-whisper requests gTTS pydub

---

## 4️⃣ Running the Application

Start the Flask API server.

python bot.py

The server will start at:

http://0.0.0.0:5000

---

# ⚠️ AWS Configuration

Ensure your EC2 **Security Group** allows inbound traffic.

Type: Custom TCP  
Port: 5000  
Source: 0.0.0.0/0

---

# 🧪 Testing

From your local machine, send a voice file to your EC2 instance.

curl -X POST http://<YOUR_EC2_PUBLIC_IP>:5000/voice-support \
     -F "audio=@sunilvoice.m4a" \
     --output reply.wav

---

# 🔊 Play the AI Response

Windows:

start reply.wav

Mac:

afplay reply.wav

Linux:

aplay reply.wav

---

# ⚙️ Voice Bot Workflow

Audio Input (.m4a)  
        ↓  
Flask API  
        ↓  
FFmpeg Conversion  
        ↓  
Whisper Transcription  
        ↓  
Ollama Llama3 Processing  
        ↓  
gTTS Speech Generation  
        ↓  
Voice Response (.wav)

---

# 🎯 Features

✔ Voice-to-Voice AI conversation  
✔ Local LLM inference using Ollama  
✔ Conversational memory support  
✔ Fully self-hosted architecture  
✔ Cloud deployment on AWS EC2  

---

# 🔮 Future Improvements

- Real-time voice streaming
- Browser microphone interface
- Lower latency with streaming STT/TTS
- WebSocket audio pipeline
- GPU acceleration for Whisper
