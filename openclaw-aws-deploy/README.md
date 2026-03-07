# 🤖 OpenClaw-EC2-Starter

A minimal, professional guide to deploying **OpenClaw**—an autonomous AI agent capable of running tasks 24/7. This implementation is optimized for the AWS Free Tier and remote control via Telegram.

---

## 📑 Table of Contents
* [Infrastructure Overview](#-infrastructure-overview)
* [Security Protocols](#-security-protocols)
* [Prerequisites](#-prerequisites)
* [Installation](#-installation)
* [Connecting Telegram](#-connecting-telegram)
* [Directory Structure](#-directory-structure)

---

## 🏗️ Infrastructure Overview
Tested on a high-performance, cost-effective configuration within the AWS Europe region:

* **Cloud Provider:** AWS EC2
* **Region:** Europe (Stockholm – `eu-north-1`)
* **Instance Type:** `m7i-flex.large`
* **Operating System:** Ubuntu 22.04
* **Deployment:** Docker Compose

---

## ⚠️ Security Protocols
OpenClaw requires system-level access and external API keys. Adhere to these safety standards:

> [!IMPORTANT]
> **Isolation:** Always run autonomous agents on a dedicated instance, never your primary personal computer.

* **Credential Safety:** Never commit your `.env` file to GitHub.
* **Network:** Restrict inbound ports using EC2 Security Groups.
* **Key Management:** Rotate API keys from OpenAI, Anthropic, or Gemini regularly.
* **Risk Awareness:** Be mindful of "Prompt Injection" (e.g., malicious data causing file deletion) and "Data Exfiltration".

---

## 📋 Prerequisites
Before starting, ensure you have:
* An active **AWS Account**.
* An **EC2 instance** with Docker and Docker Compose installed.
* **API Keys:** OpenAI, Anthropic (Claude), or Gemini.
* **Telegram Bot Token:** Obtained via [@BotFather](https://t.me/botfather).

---

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/OpenClaw-EC2-Starter.git](https://github.com/your-username/OpenClaw-EC2-Starter.git)
cd OpenClaw-EC2-Starter
2. Configure Environment
Copy the template and add your specific tokens:

Bash
cp .env.example .env
nano .env
3. Deploy Container
Bash
docker-compose up -d
📱 Connecting Telegram
Access the OpenClaw terminal and copy your unique Gateway Token.

Message your Telegram Bot: I want to connect Telegram.

Follow the prompts to enter your Pairing Code to establish the "handshake".
