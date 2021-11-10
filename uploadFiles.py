import dropbox
import os
import dropbox.files 

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)

            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path, mode=os.writeMode("overwrite")

def main():
    access_token = 'sl.A8BpHQV9m2d4W6qCnFVZedtWHEUgNQM4SLVm4p358ZdTv2gVn5Q3V9c8vVvtfhlp5cQqkWIUObVQ0RwHH7rzdMmec4W6uuGBbDIy31sy95Es3O5t2UvSmY_JLB1UJJpPi5zUUk0'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer :"))
    file_to = input("enter the full path to upload to dropbox: ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()