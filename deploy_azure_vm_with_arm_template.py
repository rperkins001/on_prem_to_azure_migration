# Import required libraries
import sys
import json
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Set required variables
subscription_id = "your_subscription_id"
resource_group_name = "your_resource_group_name"
deployment_name = "your_deployment_name"
arm_template_file = "your_arm_template_file.json"
parameters_file = "your_parameters_file.json"

# Authenticate using DefaultAzureCredential
credentials = DefaultAzureCredential()

# Create a ResourceManagementClient object
resource_client = ResourceManagementClient(credentials, subscription_id)

# Load ARM template and parameters files
with open(arm_template_file, "r") as template_file:
    arm_template = json.load(template_file)

with open(parameters_file, "r") as params_file:
    arm_parameters = json.load(params_file)

def create_resource_group():
    print(f"Creating resource group '{resource_group_name}'...")
    resource_group_params = {"location": arm_parameters["parameters"]["location"]["value"]}
    resource_client.resource_groups.create_or_update(resource_group_name, resource_group_params)
    print(f"Resource group '{resource_group_name}' created successfully.")

def deploy_arm_template():
    print(f"Deploying ARM template '{deployment_name}'...")
    deployment_properties = {
        "mode": "Incremental",
        "template": arm_template,
        "parameters": arm_parameters["parameters"]
    }
    deployment_async_operation = resource_client.deployments.begin_create_or_update(
        resource_group_name, deployment_name, {"properties": deployment_properties})
    deployment_async_operation.wait()
    print(f"Deployment '{deployment_name}' completed successfully.")

if __name__ == "__main__":
    create_resource_group()
    deploy_arm_template()