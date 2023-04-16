# Script to create an Azure Key Vault

# Define variables
$resourceGroupName = "MyResourceGroup"
$location = "eastus"
$vaultName = "MyKeyVault"

# Create the Key Vault
New-AzKeyVault -Name $vaultName -ResourceGroupName $resourceGroupName -Location $location
