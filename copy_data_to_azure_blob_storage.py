# Import required libraries
import sys
import os
from azure.storage.blob import BlobServiceClient, BlobUploadFromFileOptions

# Set required variables
connection_string = "your_connection_string"
container_name = "your_container_name"
source_directory = "your_source_directory"

# Create a BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Get the container client for the specified container
container_client = blob_service_client.get_container_client(container_name)

def upload_file(file_path, blob_name):
    print(f"Uploading file '{file_path}' to blob '{blob_name}'...")
    with open(file_path, "rb") as data:
        upload_options = BlobUploadFromFileOptions(
            overwrite=True,
            content_settings=None,
            metadata=None,
            tier=None
        )
        container_client.upload_blob_from_file(blob_name, data, upload_options)
        print(f"File '{file_path}' uploaded successfully to blob '{blob_name}'.")

def upload_directory(source_directory):
    for root, _, files in os.walk(source_directory):
        for file in files:
            file_path = os.path.join(root, file)
            blob_name = os.path.relpath(file_path, source_directory).replace("\\", "/")
            upload_file(file_path, blob_name)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        source_directory = sys.argv[1]
    upload_directory(source_directory)