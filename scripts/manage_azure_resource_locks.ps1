# Script to manage Azure resource locks

# Define variables
$resourceGroupName = "MyResourceGroup"
$resourceName = "MyResource"
$lockType = "ReadOnly" # Options are CanNotDelete or ReadOnly
$lockNotes = "This resource is locked for read-only access."

# Create the resource lock
New-AzResourceLock -ResourceGroupName $resourceGroupName -ResourceName $resourceName -LockName "MyLock" -LockLevel $lockType -Notes $lockNotes

# Remove the resource lock
Remove-AzResourceLock -ResourceGroupName $resourceGroupName -ResourceName $resourceName -LockName "MyLock"
