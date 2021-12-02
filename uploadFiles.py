import dropbox, os
from dropbox.files import WriteMode

class TransferData:
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(access_token)
        for root, dirs, files in os.walk(file_from):
            for file in files:
                localPath = os.path.join(root, file)                
                relativePath = os.path.relpath(localPath, file_from)
                dropboxPath = os.path.join(file_to, relativePath)
                with open(localPath, 'rb') as file:
                    dbx.files_upload(file.read, dropboxPath, mode=WriteMode("overwrite"))
access_token = "sl.A8kf4sGxfwmsK7Jbb1xDq6fpPYy_iaMJjQhf7WnuSxYh-3pyBQ_XTih4iCZcgOhqhTYgOgNUA500dVng7ZC6d4gWE2urMokxYZWGyO5WNE6tlNDI5IXOD_C8iYCi8XV98KFX5Ok"
def main():
    transferData = TransferData()
    file1 = input("What file path do you want to upload?")
    file2 = input("What file path on dropbox do you want to upload to?")
    transferData.upload_file(file1, file2)

main()