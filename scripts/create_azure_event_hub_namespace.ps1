# Script to create an Azure Event Hub namespace

# Define variables
$resourceGroupName = "MyResourceGroup"
$namespaceName = "MyEventHubNamespace"
$location = "eastus"

# Create the namespace
New-AzEventHubNamespace -ResourceGroupName $resourceGroupName -NamespaceName $namespaceName -Location $location
