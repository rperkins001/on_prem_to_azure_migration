# Script to create an Azure virtual network

# Define variables
$resourceGroupName = "MyResourceGroup"
$vnetName = "MyVnet"
$location = "eastus"
$subnetName = "MySubnet"
$subnetAddressPrefix = "10.0.0.0/24"

# Create the virtual network and subnet
New-AzVirtualNetwork -ResourceGroupName $resourceGroupName -Name $vnetName -Location $location -AddressPrefix "10.0.0.0/16" -Subnet $subnetName -SubnetAddressPrefix $subnetAddressPrefix
