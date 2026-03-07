
🤖 OpenClaw-EC2-Starter
A minimal guide to deploying OpenClaw, an autonomous AI agent capable of running tasks 24/7 and being controlled remotely through Telegram. This implementation is optimized for AWS EC2 Free Tier in the Europe (Stockholm) region.

📑 Table of Contents
Infrastructure Overview

Security Protocols

Prerequisites

Installation

Connecting Telegram

Directory Structure

🏗️ Infrastructure Overview
This guide was tested on a high-performance, cost-effective configuration within the AWS Europe region:

Cloud Provider: AWS EC2

Region: Europe (Stockholm – eu-north-1)

Instance Type: m7i-flex.large

Operating System: Ubuntu 22.04

Deployment: Docker Compose

⚠️ Security Protocols
OpenClaw requires system-level access and external API keys. Please adhere to these safety standards:

[!IMPORTANT]
Isolation: Always run autonomous agents on a dedicated instance, never your primary personal computer.

Credential Safety: Never commit your .env file to GitHub.

Network: Restrict inbound ports using EC2 Security Groups.

Key Management: Rotate API keys from OpenAI, Anthropic, or Gemini regularly.

Risk Awareness: Be mindful of "Prompt Injection" which could lead to unintended file deletion or data exfiltration.

📋 Prerequisites
Before starting, ensure you have:

An active AWS Account.

An EC2 instance with Docker and Docker Compose installed.

API Keys: OpenAI, Anthropic (Claude), or Gemini.

Telegram Bot Token: Obtained via @BotFather.

🚀 Installation
Clone the Repository

Bash
git clone https://github.com/your-username/OpenClaw-EC2-Starter.git
cd OpenClaw-EC2-Starter
Configure Environment
Copy the template and add your specific tokens:

Bash
cp .env.example .env
nano .env
Deploy Container

Bash
docker-compose up -d
📱 Connecting Telegram
Access the OpenClaw terminal and copy your unique Gateway Token.

Message your Telegram Bot: I want to connect Telegram.

Follow the prompts to enter your Pairing Code to establish the "handshake".

📂 Directory Structure
agents/: Custom AI roles and skill definitions.

telegram/: Bot communication and pairing logic.

cron/: Automated task scheduling (e.g., reminders).

identity/: AI persona and name configurations.

openclaw.json: Main configuration file (scrubbed of private keys).

Next Step:
Would you like me to create a .gitignore file specifically for this project to ensure your .bak and .env files stay off GitHub?
