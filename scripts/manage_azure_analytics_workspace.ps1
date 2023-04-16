# Script to manage Azure Log Analytics Workspace

# Define variables
$resourceGroupName = "MyResourceGroup"
$workspaceName = "MyWorkspace"

# Create a Log Analytics Workspace
New-AzOperationalInsightsWorkspace -ResourceGroupName $resourceGroupName -Name $workspaceName -Location "eastus"

# Remove a Log Analytics Workspace
Remove-AzOperationalInsightsWorkspace -ResourceGroupName $resourceGroupName -Name $workspaceName
