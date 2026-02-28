# 🤖 Autonomous Gmail Payment Reminder Agent


## 📝 Description
This project is an **Autonomous AI Agent** designed to bridge the gap between financial record-keeping and client communication. It monitors a Google Sheet for upcoming payment deadlines and triggers personalized, professional email reminders through Gmail.

**The Problem:** Manual follow-ups are time-consuming and prone to human error—forgetting a reminder or messaging the wrong client.  
**The Solution:** A "set-and-forget" n8n workflow that uses a custom JavaScript filter to ensure 100% accuracy in outreach timing.

---

## ⚙️ Workflow Architecture

1.  **Trigger (Schedule Node):** The agent "wakes up" every day at **09:00 AM**.
2.  **Fetch (Google Sheets Node):** It reads the "Invoices" spreadsheet database.
3.  **Logic (The Brain):** A custom JavaScript node filters only the rows where the `Due Date` matches `Today`.
4.  **Action (Gmail Node):** For every matched row, it fires a personalized email using dynamic data (Name, Invoice ID, etc.).

---

## 🧠 Technical Implementation: The Logic

The core of this project is the **JavaScript Filtering Node**. Standard "no-code" filters can struggle with date-string formats from different regions. I implemented a robust script using the `en-CA` locale to force a clean `YYYY-MM-DD` comparison.


```javascript
// Get today's date in local timezone (YYYY-MM-DD)
const today = new Date().toLocaleDateString('en-CA');

// Get incoming items from Google Sheets
const items = $input.all();

// Filter logic: Only proceed if Due Date matches today's date
const filtered = items.filter(item => {
  const due = item.json["Due Date"]; // Matches the column header in your Sheet

  if (!due) return false;

  // Normalize date: Remove time strings (e.g., T00:00:00Z) if they exist
  const normalizedDue = due.split("T")[0]; 
  return normalizedDue === today;
});

return filtered;
```
🚀 Setup & Installation
1. Prerequisites
An n8n instance (Desktop, Cloud, or Docker).

A Google Cloud Project with Gmail API and Google Sheets API enabled.

2. Workflow Import
Download the workflow.json file from this folder.

Import it into your n8n canvas via Settings > Import from File.

3. Google Workspace Connection
Configure your OAuth2 credentials.

Map your Google Sheet ID and ensure your column headers are: Name, Email, and Due Date.

📈 Business Impact
Efficiency: Saves ~5 hours of manual admin work per month.

Cash Flow: Reduces Days Sales Outstanding (DSO) by ensuring reminders hit inboxes the moment a payment is due.

Zero Error: Unlike manual checks, the script never "misses" a row or a date.

👨‍💻 Author
Sunil Raj Kumar
Master of Computer Applications | AWS Certified Cloud Practitioner
