# Script to create an Azure Logic App

# Define variables
$resourceGroupName = "MyResourceGroup"
$location = "eastus"
$logicAppName = "MyLogicApp"
$workflowName = "MyWorkflow"
$workflowDefinition = "{...}" # Replace with your workflow definition

# Create the Logic App
New-AzLogicApp -ResourceGroupName $resourceGroupName -Location $location -Name $logicAppName -Definition $workflowDefinition

# Add a workflow to the Logic App
Add-AzLogicAppWorkflow -ResourceGroupName $resourceGroupName -Name $logicAppName -Definition $workflowDefinition -WorkflowName $workflowName
