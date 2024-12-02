Google Drive Automation Script for Legacy Systems
-------------------------------------------------------
**Project Scope**
This project provides a Python-based solution for automating file uploads to Google Drive, designed specifically for obsolete systems like Windows 7, which no longer support the installation of the Google Drive desktop application for scheduled backups.

**Directory Scan:**
Finds the latest file in D:\BKUP by modification time.

**Authentication:**
Authenticates with Google Drive via D:\credentials.json or token.json.

**File Upload:**
s the latest file to Google Drive.

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
Search for "Google Drive API" and click Enable for all relevent APIs.

3-Create Credentials:
Go to APIs & Services > Credentials.
Click Create Credentials and select OAuth 2.0 Client ID.

4-Set Up OAuth Consent Screen:
Fill out the required fields (application name, email, etc.).
Under "Scopes," add https://www.googleapis.com/auth/drive.file.

it should look somthing like this:
![Capture google Cloud](https://github.com/user-attachments/assets/2bea5909-68be-49a8-81a2-1b2805cfd279)

5-Download Credentials:
After creating the OAuth 2.0 Client ID, download the JSON file (credentials.json) to the same location that the python script is running from (e.g., D:\credentials.json).

---------------------------------------------------------
**Step 2: Install Python**
Download Python 3.8.10 (which is the latest version supported for Windows 7) from the official Python website at https://www.python.org/downloads/release/python-3810/.

3. Install Required Python Libraries
cmd
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

--------------------------------------------------
*4. **Prepare and Test the Script**

Place your Python script (e.g., upload_to_drive.py) in the directory D:\

![GCP](https://github.com/user-attachments/assets/61808147-11e5-4d27-a525-fd8c53528d58)

Make sure that the script is updated to use the correct paths:
The credentials.json file should be located at D:\credentials.json.

The directory from which you want to upload files should be D:\BKUP.

To test the script, open Command Prompt and run:
cmd

python D:\upload_to_drive.py

It will create a token.json file initially and will use it aftewards in the automated process.

This will authenticate with Google Drive and upload the latest file from the specified directory.

----------------------------------------
**5.Automate with Windows Task Scheduler**
Open Task Scheduler by searching for it in the Start Menu.
Create a new task:
In the **General** tab, give the task a name.
In the **Triggers** tab, set the schedule (e.g., daily, or at specific intervals).
In the **Actions** tab, set the program/script to python.exe (the path should look like D:\upload_to_drive.py) depending on the filename

 
In the Arguments section, add the full path to the Python script:

cmd

D:\upload_to_drive.py

Save the task and manually test it by right-clicking the task and selecting Run to ensure it works.
It should look like this:

![Capture google Cloud 2](https://github.com/user-attachments/assets/d167b593-744c-490d-8deb-8d70a5d4d04a)


-----------------------------------------------
**6. Check the google drive**
The file should be zipped and uploaded to google drive as below:


![Capture google Cloud 3](https://github.com/user-attachments/assets/95b75235-6079-42a2-9a05-9b63538afc42)


Please contact [me](Yehyamnaimneh@gmail.com) for any questions or troubleshooting steps, if you encountered any problems. 



