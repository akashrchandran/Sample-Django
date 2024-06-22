from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError


def upload_file(drive_service, file_name, file_path, mime_type='application/octet-stream'):
    try:
        file_metadata = {'name': file_name}
        media = MediaFileUpload(file_path, mimetype=mime_type)
        file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        
        print(f"File ID: {file.get('id')}")
        return True
    except HttpError as error:
        print(f'An error occurred: {error}')
        return False
    
def check_authentication(drive_service):
    try:
        # Attempt to list files in Google Drive
        results = drive_service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))
        return True
    except HttpError as error:
        # The API encountered a problem before the script started executing
        print(f'An error occurred: {error}')
        return False

# Example usage
credentials = Credentials.from_service_account_file(
                'client_secrets.json',
                scopes=['https://www.googleapis.com/auth/drive'],
            )
_drive_service = build('drive', 'v3', credentials=credentials)
is_authenticated = upload_file(_drive_service, 'test.txt', 'build.sh', )
if is_authenticated:
    print("Authentication successful.")
else:
    print("Authentication failed.")