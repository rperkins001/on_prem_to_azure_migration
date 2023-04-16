# Script to create an Azure App Service

# Define variables
$resourceGroupName = "MyResourceGroup"
$appName = "MyAppService"
$planName = "MyAppServicePlan"
$location = "eastus"
$runtime = "DOTNETCORE|3.1"

# Create the App Service plan
New-AzAppServicePlan -ResourceGroupName $resourceGroupName -Name $planName -Location $location -Tier Basic -WorkerSize Small

# Create the App Service
New-AzWebApp -ResourceGroupName $resourceGroupName -Name $appName -Location $location -AppServicePlan $planName -RuntimeStack $runtime
