# Script to manage Azure API Management

# Define variables
$resourceGroupName = "MyResourceGroup"
$serviceName = "MyApiManagementService"
$location = "eastus"

# Create the API Management service
New-AzApiManagement -ResourceGroupName $resourceGroupName -Name $serviceName -Location $location -Organization "My Organization" -AdministratorEmail "admin@contoso.com"

# Add an API to the service
$apiName = "MyApi"
$openApiSpecUrl = "https://petstore.swagger.io/v2/swagger.json"
New-AzApiManagementApi -Context $apimContext -ApiId $apiName -DisplayName $apiName -Path "/$apiName" -Protocol "https" -ServiceUrl $openApiSpecUrl
