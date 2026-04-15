# 🚀 AI News → LinkedIn Automation (Make + OpenRouter)

## 📌 Overview

This workflow automatically:
1. Fetches news from RSS  
2. Filters valid articles  
3. Generates a LinkedIn post using AI  
4. Publishes it to LinkedIn  

---

## 🧩 Architecture

```text
RSS → Filter → (HTTP optional) → OpenRouter (LLM) → Set Variable → LinkedIn
⚙️ Step-by-Step Setup
1. Create Scenario in Make
Go to Scenarios
Click Create new scenario
2. Add RSS Module

Module:

RSS → Watch RSS feed items

Configuration:

URL: https://news.ycombinator.com/rss
Mode: From now on
3. Add Filter (Important)

Label:

Filter valid links

Conditions:

link EXISTS
AND
link DOES NOT CONTAIN "pretty.fish"
AND
link DOES NOT CONTAIN "news.ycombinator.com"
4. (Optional) HTTP Module — Scraping

Module:

HTTP → Make a request

Configuration:

Method: GET
URL: {{1.link}}
Return error if HTTP request fails: NO
5. (Optional) Clean Text

Module:

Tools → Set Variable

Configuration:

Name: cleaned_text
Value: {{1.description}}
6. Add OpenRouter (LLM)

Module:

OpenRouter → Create Chat Completion

Model Example:

deepseek/deepseek-v3.2
System Prompt
You are a LinkedIn content writer who creates engaging, concise, and insightful posts. Avoid fluff and write like a human.
User Prompt
Turn the following news into a LinkedIn post.

Rules:
- Start with a strong hook
- Keep it under 120 words
- Make it insightful, not just summary
- End with a question or CTA
- Use simple language

Content:
{{cleaned_text}}
7. Extract LLM Output (Critical Step)

Module:

Tools → Set Variable

Configuration:

Name: linkedin_post
Value: {{first(12.choices).message.content}}
8. Add LinkedIn Module

Module:

LinkedIn → Create a post

Configuration:

Content: {{linkedin_post}}
🧪 Testing
Run once

Expected Result:

LinkedIn post generated

Post published successfully

❗ Common Issues & Fixes
1. HTTP Bad Request

Cause:

Invalid or blocked URLs

Fix:

- Add filters
- Disable "Return error if HTTP request fails"
2. JSON instead of text

Problem:

{ "message": { "content": "..." } }

Fix:

{{first(choices).message.content}}
3. Empty LinkedIn post

Cause:

Incorrect mapping

Fix:

- Use picker
- Ensure content is not empty

4. Mapping issues in Make
Rule:
- Never type paths manually
- Always use picker or full expression

🚀 Enhancements
Limit Post Length
{{substring(trim(first(12.choices).message.content); 0; 2000)}}

Add Scheduling
Use Make scheduler (e.g., every 6 hours)

Multi-source RSS
- TechCrunch
- Reddit
- Product Hunt

Store Posts
- Google Sheets
- Notion

📂 Use Cases

Personal branding
Startup marketing
Developer Relations
Content automation

🎯 Outcome

✅ Automated content pipeline
✅ AI-powered LinkedIn posts
✅ Zero manual effort
✅ Scalable workflow
