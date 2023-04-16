#!/bin/bash

RESOURCE_GROUP="your_resource_group"
LOCATION="your_location"
REGISTRY_NAME="your_registry_name"
OPERATION="create" # Use "create", "delete", "list", or "list-repositories"

if [ "$OPERATION" == "create" ]; then
  az acr create --resource-group $RESOURCE_GROUP --name $REGISTRY_NAME --sku Basic --location $LOCATION
elif [ "$OPERATION" == "delete" ]; then
  az acr delete --resource-group $RESOURCE_GROUP --name $REGISTRY_NAME
elif [ "$OPERATION" == "list" ]; then
  az acr list --resource-group $RESOURCE_GROUP --output table
else
  az acr repository list --name $REGISTRY_NAME --output table
fi
