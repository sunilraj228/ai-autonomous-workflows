# 🧩 Architecture — AI Log Analyzer

## **🎯 Overview**

This document explains the architecture and workflow of the AI Log Analyzer system, which automates error log analysis using a no-code pipeline.

---

## **🔄 High-Level Architecture**

```id="j0q3v3"
[Google Form] → [Make] → [OpenRouter (LLM)] → [Google Sheets]
```

---

## **🧠 Component Breakdown**

### **1. Input Layer — Google Forms**

* Collects raw error logs from users
* Provides structured input to the workflow
* Optional fields can include:

  * Source (API, Database, Backend)
  * Expected behavior

---

### **2. Automation Layer — Make**

* Acts as the orchestration engine
* Triggers workflow on new form submission
* Handles:

  * Data extraction
  * API request construction
  * Response handling

---

### **3. AI Processing Layer — OpenRouter**

* Receives log input via HTTP request
* Uses LLM (`openai/gpt-4o-mini`)
* Generates:

  * Root cause analysis
  * Fix recommendations
  * Severity classification

---

### **4. Storage Layer — Google Sheets**

* Stores processed results
* Enables:

  * Tracking of issues
  * Historical analysis
  * Filtering and reporting

---

## **⚙️ Data Flow (Step-by-Step)**

```id="vhhm4c"
1. User submits log via Google Form
2. Make detects new response (trigger)
3. Make extracts log data
4. HTTP module sends request to OpenRouter
5. OpenRouter processes log using LLM
6. Response returned to Make
7. Make writes output to Google Sheets
```

---

## **📦 Request Structure (OpenRouter)**

```json id="y0c0hp"
{
  "model": "openai/gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": "Analyze this log and return root cause, fix, and severity."
    }
  ]
}
```

---

## **📤 Response Structure**

```json id="3az2xj"
{
  "choices": [
    {
      "message": {
        "content": "Root Cause: ... Fix: ... Severity: ..."
      }
    }
  ]
}
```

---

## **🔐 Security Considerations**

* API keys are stored securely in Make
* No sensitive data is exposed publicly
* Access to Google Sheets can be restricted

---

## **🚀 Scalability Considerations**

* Can handle multiple submissions concurrently
* Easily extendable to:

  * Slack alerts
  * Email notifications
  * Dashboard integrations

---

## **🔮 Future Architecture Enhancements**

* Structured JSON output for better parsing
* Vector database for historical log similarity
* Real-time alerting system
* Multi-source ingestion (APIs, logs, monitoring tools)

---

## **🎯 Summary**

This architecture demonstrates how AI can be integrated into real-world operational workflows using no-code tools, enabling faster debugging and improved efficiency.
