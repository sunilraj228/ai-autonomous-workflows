# ⚠️ Common Errors & Troubleshooting — AI Log Analyzer

This document lists common issues encountered while building the AI Log Analyzer workflow using Make, OpenRouter, and Google integrations.

---

## **1. No Data Triggered in Make**

### ❌ Error

```
The module didn't return any new data
```

### 🔍 Cause

* No new Google Form submission after clicking “Run once”
* Trigger is set incorrectly

### ✅ Fix

* Click **Run once** → then submit a new form response
* Set **Choose where to start → All responses**

---

## **2. Invalid JSON Body**

### ❌ Error

```
Invalid JSON body / Unexpected character
```

### 🔍 Cause

* Broken JSON formatting
* Extra commas or missing quotes
* Injecting raw JSON inside a string

### ✅ Fix

* Ensure only ONE valid JSON object is present
* Avoid embedding unescaped JSON
* Use Make variable picker instead of manual typing

---

## **3. 404 Not Found (OpenRouter)**

### ❌ Error

```
404 Not Found
```

### 🔍 Cause

* Incorrect API endpoint
* Wrong HTTP method

### ✅ Fix

* Use:

```
POST https://openrouter.ai/api/v1/chat/completions
```

---

## **4. Authentication Failure**

### ❌ Error

```
Unauthorized / Invalid API key
```

### 🔍 Cause

* Missing "Bearer" in header
* Invalid API key

### ✅ Fix

```
Authorization: Bearer YOUR_API_KEY
```

---

## **5. Wrong HTTP Method**

### ❌ Error

* No response or API failure

### 🔍 Cause

* Using GET instead of POST

### ✅ Fix

* Change method to:

```
POST
```

---

## **6. Variable Mapping Issues**

### ❌ Error

* Empty log input
* Incorrect or null values

### 🔍 Cause

* Selecting wrong field (e.g., answers[1] instead of answers[0])
* Mapping entire object instead of value

### ✅ Fix

* Use:

```
answers[0].value
```

---

## **7. JSON Injection from Form Data**

### ❌ Error

```
Unexpected token or invalid JSON
```

### 🔍 Cause

* Passing full JSON object instead of string

### ✅ Fix

* Extract only the text value
* OR let AI parse raw input safely

---

## **8. No AI Output in Make**

### ❌ Error

* Response appears empty

### 🔍 Cause

* Parse response disabled
* Incorrect field mapping

### ✅ Fix

* Enable:

```
Parse response = TRUE
```

* Use:

```
choices[0].message.content
```

---

## **9. Google Sheets Not Updating**

### ❌ Error

* No rows added

### 🔍 Cause

* Incorrect sheet selection
* Columns not matching

### ✅ Fix

* Ensure column headers match mapping
* Select correct spreadsheet and sheet

---

## **10. Delayed Form Trigger**

### ❌ Issue

* Workflow not triggered immediately

### 🔍 Cause

* Google Forms delay

### ✅ Fix

* Use Google Sheets trigger for faster response
* Or wait for polling interval

---

## **🧠 Key Takeaway**

Most issues arise from:

* Incorrect JSON formatting
* Wrong variable mapping
* Trigger misconfiguration

Understanding these helps build more reliable AI workflows.

---
