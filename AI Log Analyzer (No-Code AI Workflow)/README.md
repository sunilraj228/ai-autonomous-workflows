🔍 AI Log Analyzer (No-Code AI Workflow)

🚀 Overview

AI Log Analyzer is a no-code automation workflow that analyzes error logs using an LLM and generates:

Root cause analysis
Step-by-step fixes
Severity classification

The system is built using automation tools and requires minimal coding, making it easy to deploy and extend.

🧠 Problem

Support engineers and developers spend significant time manually debugging logs and identifying issues. This process is repetitive, time-consuming, and error-prone.

⚙️ Solution

This project automates log analysis by integrating form input, AI processing, and structured output storage.

🔄 Workflow Architecture

Google Form → Make → OpenRouter (LLM) → Google Sheets

🛠️ Tech Stack

Make (automation workflow engine)
OpenRouter (LLM API gateway)
Google Forms (input collection)
Google Sheets (data storage)

✨ Features

Automated root cause detection
Actionable fix recommendations
Severity classification (Low / Medium / High)
Fully no-code implementation
Real-time log processing

🧪 Example

Input
Error: API returned 500 Internal Server Error
Output
Root Cause: Server-side failure due to unexpected condition

Fix:

1. Check server logs for detailed errors
2. Validate API request parameters
3. Restart the service if needed

Severity: High

📊 Output Storage

All analyzed logs are automatically stored in Google Sheets for tracking and further analysis.

📁 Project Structure
ai-log-analyzer/
│── README.md
│── ARCHITECTURE.md
│── screenshots/
│── prompts/
│── sample-data/
│── demo/

🧩 How It Works

User submits an error log via Google Form
Make captures the form response
HTTP module sends log to OpenRouter
LLM analyzes the log
Output is stored in Google Sheets

🔧 Setup Instructions

Create a Google Form with a log input field
Set up a Make scenario:
Trigger: Google Forms → Watch Responses
Action: HTTP request to OpenRouter
Action: Google Sheets → Add Row
Add OpenRouter API key in HTTP headers
Configure prompt for structured output
Run and test the workflow

🔮 Future Improvements

Structured JSON output parsing
Slack/Email alerts for high severity issues
Dashboard for trend analysis
Multi-log batch processing
🎯 Key Takeaway

This project demonstrates how AI can be integrated into real-world workflows using no-code tools to automate repetitive engineering tasks.
