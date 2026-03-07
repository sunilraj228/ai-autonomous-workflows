# 🛠️ OpenClaw Troubleshooting Guide

This document tracks common errors, causes, and solutions encountered during the deployment of OpenClaw on AWS EC2.

---

## 📑 Table of Contents
1. [Environment & CLI Errors](#1-environment--cli-errors)
2. [Network & Gateway Issues](#2-network--gateway-issues)
3. [API & Model Configuration](#3-api--model-configuration)
4. [File System & Permissions](#4-file-system--permissions)
5. [Telegram Integration](#5-telegram-integration)
6. [Process Persistence](#6-process-persistence)

---

## 1. Environment & CLI Errors

### `openclaw: command not found`
* **Cause:** OpenClaw was installed via `npm` user-local install, and the binary path was not added to your system's `$PATH`.
* **Fix:** Use the full binary path:
    ```bash
    /home/ubuntu/.npm-global/bin/openclaw
    ```

### CLI only shows help menu
* **Cause:** Running `openclaw` alone is insufficient; it requires a subcommand.
* **Fix:** Start the gateway service:
    ```bash
    openclaw gateway
    ```

### Service doesn't start after installation
* **Cause:** The CLI installation does not automatically trigger the service.
* **Fix:** Manually start the gateway using the command above.

---

## 2. Network & Gateway Issues

### Gateway UI not accessible in browser
* **Cause:** The gateway binds to `127.0.0.1` by default, blocking external access via the EC2 Public IP.
* **Fix:** Create an SSH tunnel from your local machine:
    ```bash
    ssh -N -L 18789:127.0.0.1:18789 ubuntu@your-ec2-ip
    ```
    Then, open `http://localhost:18789` in your local browser.

---

## 3. API & Model Configuration

### `401 Incorrect API Key`
* **Cause:** OpenClaw defaults to `openai/gpt-5`, but you are likely using OpenRouter.
* **Fix:** Configure your environment variables in `.env`:
    ```bash
    OPENROUTER_API_KEY=your_key
    OPENAI_BASE_URL=[https://openrouter.ai/api/v1](https://openrouter.ai/api/v1)
    ```

### Logs show wrong model (`openai/gpt-5`)
* **Cause:** The `openclaw.json` config file overrides environment variables.
* **Fix:** Edit `~/.openclaw/openclaw.json` and update the `primary` model field.

### Agent won't read files (Tool Restriction)
* **Cause:** The tool profile is set to `messaging` only.
* **Fix:** Change the profile in your config to allow filesystem access:
    ```json
    "tools": { "profile": "full" }
    ```

---

## 4. File System & Permissions

### Bot reports "CSV is empty" or "No access"
* **Cause:** Wrong file location or incorrect permissions.
* **Fix 1 (Location):** Move files to the workspace:
    ```bash
    mv ~/.openclaw/media/inbound/data.csv ~/.openclaw/workspace/
    ```
* **Fix 2 (Permissions):** Ensure the `ubuntu` user owns the file:
    ```bash
    sudo chown ubuntu:ubuntu data.csv
    ```

### Workspace not updating
* **Cause:** The gateway hasn't reloaded the directory changes.
* **Fix:** Restart the service:
    ```bash
    docker compose restart
    ```

---

## 5. Telegram Integration

### Invalid Bot Username
* **Cause:** Telegram requires usernames to end in "bot".
* **Fix:** Ensure your name is formatted as `yourname_bot`.

### Username Taken
* **Cause:** Telegram bot names are globally unique.
* **Fix:** Choose a more specific name like `sunil_claw_helper_bot`.

---

## 6. Process Persistence

### Service stops when SSH closes
* **Cause:** The process is tied to the current shell session.
* **Fix:** Use a terminal multiplexer like `tmux`:
    ```bash
    tmux new -s openclaw
    openclaw gateway
    # Press Ctrl+B, then D to detach
    ```

---
> [!TIP]
> **Warning: Config Overwrite** > If you see `Config overwrite ~/.openclaw/openclaw.json`, it simply means an existing config was detected. No action is required unless you intend to reset your settings.
