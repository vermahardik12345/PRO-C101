import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)
def main():
    access_token='sl.A4q41qUlUuptd7b6g5sOAlm3lcGg9f_w9yh6oiOfQCeD6KmARFM3VAbUWLko7Iy_D8Hgr_38lwTEwLlC-RknitvNRVzPq9iWKz_F4kVEUq4E8NPm-EU9cdh4qD6YpltXjlBG_9ea5ik'
    transferData=TransferData(access_token)
    file_from=input('Write the path of the file which you want to upload')
    file_to=input('Enter the full path to uplaod')
    print('Uploaded Successfully')
    transferData.upload_file(file_from,file_to)  
if __name__=='__main__':
    main()    

