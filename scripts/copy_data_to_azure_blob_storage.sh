#!/bin/bash

SOURCE_PATH="/path/to/your/local/data"
STORAGE_ACCOUNT_NAME="yourstorageaccountname"
CONTAINER_NAME="yourcontainername"
SAS_TOKEN="yourSASToken"

azcopy copy "$SOURCE_PATH" "https://$STORAGE_ACCOUNT_NAME.blob.core.windows.net/$CONTAINER_NAME?$SAS_TOKEN" --recursive
