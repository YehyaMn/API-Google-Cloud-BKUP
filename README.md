Google Drive Automation Script for Legacy Systems
-------------------------------------------------------
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

---------------------------------------------------------------------------------------------------------------------

**Purpose**
Workaround for Unsupported Systems: Bypasses the limitation of installing the Google Drive .exe by utilizing the Google Drive API.
Automation: Automatically selects the latest file from a designated directory and uploads it to Google Drive.
Seamless Authentication: Uses a browser-based authentication flow to sign in to Google Drive, ensuring compatibility and security.


**Features**
Scans a specified folder for the most recently modified file.
Uploads the selected file to Google Drive using API calls.
Caches credentials in a token.json file for repeat usage without repeated sign-ins.
Designed for scenarios requiring the backup of crucial files.

**Usage Example**
Place the script on the target system (e.g., Windows 7).
Set the directory containing the files (my folder: D:\BKUP) change this in the python script.
Ensure a valid credentials.json is provided for authentication.
Run the script to automatically find the latest file and upload it to Google Drive.

**System Requirements**
Python 3.x
Necessary Python libraries: google-auth, google-auth-oauthlib, google-api-python-client.

-------------------------------------------------------------------------------------------------------------------------------
**Step 1: Create Google API Credentials for Google Drive**
-------------------------------------------------------------
1-Go to [Google Cloud Console]( https://console.cloud.google.com/.).
Create a Project:
Click on the **project** dropdown menu.
Select New Project and give it a name (e.g., "Backup-To-GoogleDrive").


2-Enable Google Drive API:
Go to the APIs & Services > Library section.
Search for "Google Drive API" and click Enable.

3-Create Credentials:
Go to APIs & Services > Credentials.
Click Create Credentials and select OAuth 2.0 Client ID.

4-Set Up OAuth Consent Screen:
Fill out the required fields (application name, email, etc.).
Under "Scopes," add https://www.googleapis.com/auth/drive.file.
Download Credentials:
After creating the OAuth 2.0 Client ID, download the JSON file (credentials.json) to a known location (e.g., D:\credentials.json).
