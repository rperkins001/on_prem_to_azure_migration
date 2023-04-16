# Script to create an Azure virtual machine

# Define variables
$resourceGroupName = "MyResourceGroup"
$location = "eastus"
$vmName = "MyVM"
$username = "myadminuser"
$password = "myp@ssw0rd123"
$imagePublisher = "MicrosoftWindowsServer"
$imageOffer = "WindowsServer"
$imageSKU = "2019-Datacenter"
$vmSize = "Standard_DS2_v2"

# Create the virtual machine
New-AzVM -ResourceGroupName $resourceGroupName -Name $vmName -Location $location -ImagePublisher $imagePublisher -ImageOffer $imageOffer -ImageSKU $imageSKU -Credential (Get-Credential -UserName $username -Message "Enter password for the VM") -Size $vmSize
