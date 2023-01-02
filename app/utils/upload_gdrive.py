from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from .read_env import get_env
from logging import getLogger

SCOPES = ['https://www.googleapis.com/auth/drive']

logger = getLogger('uvicorn')

def upload(file_path: str, SHARE_FOLDER_ID: str):
    credentials = get_env(['CREDENTIALS_PATH'])['CREDENTIALS_PATH']
    sa_creds = service_account.Credentials.from_service_account_file(credentials)
    creds = sa_creds.with_scopes(SCOPES)
    file_name = file_path.split('/')[-1]
    file_id = ""

    logger.info('start upload file')

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {
            'name': file_name,
            'parents': [SHARE_FOLDER_ID]
            }

        media = MediaFileUpload(
            file_path,
            mimetype='audio/m4a',
            resumable=True
        )

        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

        file_id = file.get("id")
        logger.info(f'success upload file: {file_id}')

    except:
        logger.error('failed upload file')
        return "failed"

    return file_id
