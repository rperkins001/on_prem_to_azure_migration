#!/bin/bash

RESOURCE_GROUP="your_resource_group"
LOCATION="your_location"
CONTAINER_NAME="your_container_name"
IMAGE="your_image_name"
OPERATION="create" # Use "create", "delete", or "list"

if [ "$OPERATION" == "create" ]; then
  az container create --resource-group $RESOURCE_GROUP --name $CONTAINER_NAME --image $IMAGE --location $LOCATION
elif [ "$OPERATION" == "delete" ]; then
  az container delete --resource-group $RESOURCE_GROUP --name $CONTAINER_NAME --yes
else
  az container list --resource-group $RESOURCE_GROUP --output table
fi
