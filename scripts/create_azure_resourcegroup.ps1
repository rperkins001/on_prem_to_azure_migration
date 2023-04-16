# Script to create an Azure resource group

# Define variables
$resourceGroupName = "MyResourceGroup"
$location = "eastus"

# Create the resource group
New-AzResourceGroup -Name $resourceGroupName -Location $location
