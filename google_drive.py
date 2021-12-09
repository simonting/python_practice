from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from datetime import datetime, timedelta
# Create GoogleDrive instance with authenticated GoogleAuth instance.
gauth = GoogleAuth()
drive = GoogleDrive(gauth)
folder = 'YOUR FOLDER URL'

now = datetime.now()
today = now.strftime('%Y%m%d')
remove_time = now - timedelta(days=7)

today_file = "test_" + today +".sql"
remove_file = "test_" + remove_time.strftime('%Y%m%d') +".sql"

# Delete file
file_list = drive.ListFile({'q': "'YOUR FOLDER URL' in parents and trashed=False"}).GetList()
for x in  range(len(file_list)):
   if file_list[x]['title'] == remove_file:
       file_id = file_list[x]['id']
       file1 = drive.CreateFile({'id': file_id})
       file1.Delete()

# Create GoogleDriveFile instance with title 'Hello.txt'.
file1 = drive.CreateFile({'parents' : [{'id': folder}], 'title' : today_file})
file1.SetContentFile('./'+ today_file)
file1.Upload() # Upload the file.


