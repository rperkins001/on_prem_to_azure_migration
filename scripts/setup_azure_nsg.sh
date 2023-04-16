#!/bin/bash

RESOURCE_GROUP="your_resource_group"
LOCATION="your_location"
NSG_NAME="your_nsg_name"
RULE_NAME="your_rule_name"
DIRECTION="Inbound" # Use "Inbound" or "Outbound"
ACCESS="Allow" # Use "Allow" or "Deny"
PROTOCOL="Tcp" # Use "Tcp", "Udp", or "*"
SOURCE_ADDRESS_PREFIX="*"
DESTINATION_ADDRESS_PREFIX="*"
SOURCE_PORT_RANGE="*"
DESTINATION_PORT_RANGE="80"
PRIORITY="100"

az network nsg create --resource-group $RESOURCE_GROUP --name $NSG_NAME --location $LOCATION

az network nsg rule create --resource-group $RESOURCE_GROUP --nsg-name $NSG_NAME --name $RULE_NAME --direction $DIRECTION --access $ACCESS --protocol $PROTOCOL --source-address-prefix $SOURCE_ADDRESS_PREFIX --destination-address-prefix $DESTINATION_ADDRESS_PREFIX --source-port-range $SOURCE_PORT_RANGE --destination-port-range $DESTINATION_PORT_RANGE --priority $PRIORITY

    manage_azure_container_instances.sh:

bash

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

    manage_azure_container_registries.sh:

bash

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

Make sure to replace the placeholder values with your own information, such as resource group, location, storage account name, container name, etc.
