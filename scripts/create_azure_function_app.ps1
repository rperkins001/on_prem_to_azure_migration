# Script to create an Azure Function App

# Define variables
$resourceGroupName = "MyResourceGroup"
$functionAppName = "MyFunctionApp"
$storageAccountName = "mystorageaccount"
$location = "eastus"
$runtime = "dotnet"

# Create the storage account
New-AzStorageAccount -ResourceGroupName $resourceGroupName -Name $storageAccountName -Location $location -SkuName Standard_LRS

# Create the Function App
New-AzFunctionApp -ResourceGroupName $resourceGroupName -Name $functionAppName -Location $location -StorageAccountName $storageAccountName -Runtime $runtime
