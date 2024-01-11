from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'student-information-408604-1a1b268e6dff.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '16-TFDO6h_o6-WqLcXQjgeX0aESvfCz4o'
file_name =['uploaded_image.jpg']
mime_type =['image/jpeg']

for file_name, mime_type in zip(file_name, mime_type):
    file_metadata = {
        'name' : file_name,
        'parents' : [folder_id] 
    }
    media = MediaFileUpload('C:/Users/hosaa/Desktop/projects/python project/test2-4/{0}'.format(file_name), mimetype=mime_type)
    
    service.files().create(
       body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

