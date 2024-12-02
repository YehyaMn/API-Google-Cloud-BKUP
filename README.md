Google Drive Automation Script for Legacy Systems

**Project Scope**
This project provides a Python-based solution for automating file uploads to Google Drive, designed specifically for obsolete systems like Windows 7, which no longer support the installation of the Google Drive desktop application for scheduled backups.

**Directory Scan:**
Finds the latest file in D:\BKUP by modification time.

**Authentication:**
Authenticates with Google Drive via D:\credentials.json or token.json.

**File Upload:**
Uploads the latest file to Google Drive.

**Confirmation:**
Prints the success message, including the file ID, or shows errors with stack traces.
