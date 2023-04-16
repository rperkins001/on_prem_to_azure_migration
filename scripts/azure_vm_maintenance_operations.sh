#!/bin/bash

RESOURCE_GROUP="your_resource_group"
VM_NAME="your_vm_name"
OPERATION="start" # You can use "start", "stop", "restart", or "deallocate"

az vm $OPERATION --resource-group $RESOURCE_GROUP --name $VM_NAME
