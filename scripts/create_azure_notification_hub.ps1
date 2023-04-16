# Script to create an Azure Notification Hub

# Define variables
$resourceGroupName = "MyResourceGroup"
$namespaceName = "MyNotificationHubNamespace"
$location = "eastus"
$hubName = "MyNotificationHub"
$sku = "Standard"
$authentication = "DefaultFullSharedAccessSignature"

# Create the Notification Hub namespace
New-AzNotificationHubsNamespace -ResourceGroupName $resourceGroupName -NamespaceName $namespaceName -Location $location

# Create the Notification Hub
New-AzNotificationHub -ResourceGroupName $resourceGroupName -NamespaceName $namespaceName -Name $hubName -Sku $sku -Authentication $authentication
