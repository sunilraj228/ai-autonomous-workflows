/**
 * n8n Code Node Script
 * Purpose: Filter incoming Google Sheet rows where "Due Date" equals "Today".
 * Locale: 'en-CA' is used to ensure YYYY-MM-DD formatting.
 */

// 1. Get today's date in local timezone (YYYY-MM-DD)
const today = new Date().toLocaleDateString('en-CA');

// 2. Get incoming items from the previous node (Google Sheets)
const items = $input.all();

// 3. Filter logic: Only allow rows where the date matches today
const filtered = items.filter(item => {
  const due = item.json["Due Date"]; // Ensure your Google Sheet column header matches this exactly

  if (!due) return false;

  // Normalize date: Remove time strings (e.g., T00:00:00Z) if they exist in the cell
  const normalizedDue = due.split("T")[0]; 
  
  // Return true only if the record's due date matches today's date
  return normalizedDue === today;
});

// 4. Return the filtered list for the Gmail node to process
return filtered;
