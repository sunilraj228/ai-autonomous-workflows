Markdown
# 🤖 OpenClaw-EC2-Starter

A professional, minimal guide to deploying **OpenClaw**—an autonomous AI agent capable of running tasks 24/7. This implementation is optimized for the **AWS Free Tier** and features remote control via **Telegram**.

---

## 📑 Table of Contents
* [Infrastructure Overview](#-infrastructure-overview)
* [Security Protocols](#-security-protocols)
* [Getting a Free API Key](#-getting-a-free-api-key)
* [Quick Start & Installation](#-quick-start--installation)
* [Project Architecture](#-project-architecture)
* [Directory Structure](#-directory-structure)

---

## 🏗️ Infrastructure Overview
This setup was tested and verified on the following AWS configuration:

* **Cloud Provider**: AWS EC2
* **Region**: Europe (Stockholm – `eu-north-1`)
* **Instance Type**: `m7i-flex.large`
* **Operating System**: Ubuntu 22.04
* **Deployment Method**: Docker Compose

---

## ⚠️ Security Protocols
OpenClaw requires system-level access and external API keys. Adhere to these safety standards:

> [!IMPORTANT]
> **Isolation**: Always run autonomous agents on a dedicated instance, never your primary personal computer.

* **Credential Safety**: Never commit your `.env` file to GitHub.
* **Network Security**: Restrict inbound ports using EC2 Security Groups.
* **Key Management**: Rotate API keys from OpenAI, Anthropic, or Gemini regularly.
* **Risk Awareness**: Be mindful of "Prompt Injection" (e.g., malicious data causing file deletion) and "Data Exfiltration" risks.

---

## 🔑 Getting a Free API Key
This project requires an API key to access AI models. You can obtain a free key from **OpenRouter**:

1. **Create Account**: Sign up at [OpenRouter.ai](https://openrouter.ai).
2. **Generate Key**: Navigate to **Keys** > **Create Key**. Your key will look like: `sk-or-v1-xxxxxxxxxxxxxxxx`.
3. **Select Model**: OpenRouter offers free models like `openrouter/qwen/qwen3-vl-30b-a3b-thinking:free`.

---

## 🚀 Quick Start & Installation
Follow these steps to get your Telegram AI bot running quickly on your EC2 instance.

### 1. Clone the Repository

```bash

git clone [https://github.com/YOUR_USERNAME/OpenClaw-EC2-Starter.git](https://github.com/YOUR_USERNAME/OpenClaw-EC2-Starter.git)

cd OpenClaw-EC2-Starter

2. Configure Environment Variables
Copy the template and edit it with your credentials:

Bash

cp .env.example .env
nano .env
Ensure these fields are filled:

OPENAI_API_KEY=your_openrouter_key

TELEGRAM_BOT_TOKEN=your_telegram_bot_token

MODEL=openrouter/qwen/qwen3-vl-30b-a3b-thinking:free

3. Start the Bot with Docker

Launch the OpenClaw gateway and Telegram bot integration:

Bash

docker compose up -d

4. Test the Connection

Open Telegram and send a message to your bot (e.g., "Hello"). The bot should respond using the configured AI model. For initial pairing, use the Gateway Token from your terminal to establish the "handshake".

🛠️ Project Architecture

The system follows a modular flow to process requests and execute tasks:


Telegram User
      │
      ▼
Telegram Bot (Interface)
      │
      ▼
OpenClaw Gateway (Logic & System Access)
      │
      ▼
AI Model (OpenRouter / Intelligence)
      │
      ▼
Response sent back to Telegram

📂 Directory Structure

agents/: Custom AI roles and skill definitions.

telegram/: Bot communication and pairing logic.

cron/: Automated task scheduling (e.g., reminders).

identity/: AI persona and name configurations.

openclaw.json: Main configuration file (scrubbed of private keys).
