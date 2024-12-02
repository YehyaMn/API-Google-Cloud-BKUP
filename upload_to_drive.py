from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
import sys
import traceback

# Define the scopes for Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenticate():
    """Authenticate and return the Google Drive API service."""
    creds = None
    # Check if token.json exists to get credentials
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no valid credentials, prompt for login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print("Current Working Directory:", os.getcwd())
            print("Looking for credentials.json in:", os.path.abspath('credentials.json'))
            # Update the path to point to D:\credentials.json
            flow = InstalledAppFlow.from_client_secrets_file(r'D:\credentials.json', SCOPES)  # Use absolute path I used D:\ and named the json file as credentials
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def get_latest_file(directory):
    """Get the latest modified file in the specified directory."""
    try:
        # Get all files in the directory and sort by modification time
        files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        if not files:
            raise Exception("No files found in the directory")
        
        latest_file = max(files, key=os.path.getmtime)  # Get the file with the latest modification time
        return latest_file
    except Exception as e:
        print(f"An error occurred while finding the latest file: {e}")
        traceback.print_exc()
        sys.exit(1)  # Exit if no files are found or an error occurs

def upload_file(file_path):
    """Upload a file to Google Drive."""
    try:
        creds = authenticate()
        service = build('drive', 'v3', credentials=creds)
        file_metadata = {'name': os.path.basename(file_path)}
        media = MediaFileUpload(file_path, resumable=True)
        
        # Upload the file and get the response
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        
        # Print a confirmation message with the file ID
        print(f"File uploaded successfully. File ID: {file.get('id')}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Stack trace:")
        traceback.print_exc()  # Print the stack trace for better debugging
        return  # Exit the function to prevent further execution

if __name__ == '__main__':
    # Set the directory path, in my case it is reading from D:\BKUP
    directory = r'D:\BKUP'
    
    # Find the latest file in the directory
    latest_file = get_latest_file(directory)
    
    # Print the file being uploaded
    print(f"Uploading the latest file: {latest_file}")
    
    # Upload the latest file
    upload_file(latest_file)

    # This input line keeps the window open after successful upload or error
    # input("Press Enter to exit...")
