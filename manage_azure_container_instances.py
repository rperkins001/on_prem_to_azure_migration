# Import required libraries
import sys
from azure.identity import DefaultAzureCredential
from azure.mgmt.containerinstance import ContainerInstanceManagementClient
from azure.mgmt.containerinstance.models import ContainerGroup, Container, ResourceRequirements, ResourceRequests, ImageRegistryCredential

# Set required variables
subscription_id = "your_subscription_id"
resource_group_name = "your_resource_group_name"
location = "your_location"

# Authenticate using DefaultAzureCredential
credentials = DefaultAzureCredential()

# Create a ContainerInstanceManagementClient object
container_instance_client = ContainerInstanceManagementClient(credentials, subscription_id)

def list_container_groups():
    print("Listing container groups:")
    container_groups = container_instance_client.container_groups.list_by_resource_group(resource_group_name)
    for container_group in container_groups:
        print(f"  - {container_group.name}")

def create_container_group(container_group_name, container_image, cpu, memory):
    print(f"Creating container group '{container_group_name}'...")
    container_resource_requests = ResourceRequests(memory_in_gb=memory, cpu=cpu)
    container_resource_requirements = ResourceRequirements(requests=container_resource_requests)
    container = Container(name=container_group_name, image=container_image, resources=container_resource_requirements)
    container_group = ContainerGroup(location=location, containers=[container], os_type='Linux')
    container_instance_client.container_groups.create_or_update(resource_group_name, container_group_name, container_group)
    print(f"Container group '{container_group_name}' created successfully.")

def delete_container_group(container_group_name):
    print(f"Deleting container group '{container_group_name}'...")
    container_instance_client.container_groups.delete(resource_group_name, container_group_name)
    print(f"Container group '{container_group_name}' deleted successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python manage_azure_container_instances.py [list|create|delete] [container_group_name] [container_image] [cpu] [memory]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "list":
        list_container_groups()
    elif command in ["create", "delete"]:
        if len(sys.argv) < 3:
            print("Error: container_group_name is required.")
            sys.exit(1)
        container_group_name = sys.argv[2]
        if command == "create":
            if len(sys.argv) < 6:
                print("Error: container_image, cpu, and memory are required.")
                sys.exit(1)
            container_image = sys.argv[3]
            cpu = float(sys.argv[4])
            memory = float(sys.argv[5])
            create_container_group(container_group_name, container_image, cpu, memory)
        elif command == "delete":
            delete_container_group(container_group_name)
    else:
        print("Error: Invalid command.")
        sys.exit(1)
