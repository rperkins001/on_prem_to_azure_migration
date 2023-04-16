# Import required libraries
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import DeploymentMode
import json
import os

# Set required variables
subscription_id = "your_subscription_id"
resource_group_name = "your_resource_group_name"
deployment_name = "your_deployment_name"
template_file_path = "path/to/your/arm_template.json"
parameters_file_path = "path/to/your/arm_parameters.json"

# Authenticate using Azure CLI credentials
credentials = AzureCliCredential()

# Create a ResourceManagementClient object
resource_client = ResourceManagementClient(credentials, subscription_id)

# Load ARM template and parameters from JSON files
with open(template_file_path, "r") as template_file:
    template = json.load(template_file)
with open(parameters_file_path, "r") as parameters_file:
    parameters = json.load(parameters_file)

# Deploy Azure VM using ARM template
deployment_properties = {
    'mode': DeploymentMode.incremental,
    'template': template,
    'parameters': parameters
}
deployment_async_operation = resource_client.deployments.begin_create_or_update(
    resource_group_name,
    deployment_name,
    deployment_properties
)
deployment_async_operation.wait()

print(f"Deployment {deployment_name} completed.")