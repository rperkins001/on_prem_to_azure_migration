import sys
from azure.identity import DefaultAzureCredential
from azure.mgmt.servicebus import ServiceBusManagementClient
from azure.mgmt.servicebus.models import SBNamespace, QueueCreateOrUpdateParameters

# Set required variables
subscription_id = "your_subscription_id"
resource_group_name = "your_resource_group_name"
namespace_name = "your_namespace_name"
location = "your_location"

# Authenticate using DefaultAzureCredential
credentials = DefaultAzureCredential()

# Create a ServiceBusManagementClient object
servicebus_client = ServiceBusManagementClient(credentials, subscription_id)

def create_namespace():
    print(f"Creating namespace '{namespace_name}'...")
    namespace_parameters = SBNamespace(location=location)
    servicebus_client.namespaces.create_or_update(resource_group_name, namespace_name, namespace_parameters)
    print(f"Namespace '{namespace_name}' created successfully.")

def delete_namespace():
    print(f"Deleting namespace '{namespace_name}'...")
    servicebus_client.namespaces.delete(resource_group_name, namespace_name)
    print(f"Namespace '{namespace_name}' deleted successfully.")

def list_queues():
    print("Listing queues:")
    queues = servicebus_client.queues.list_by_namespace(resource_group_name, namespace_name)
    for queue in queues:
        print(f"  - {queue.name}")

def create_queue(queue_name):
    print(f"Creating queue '{queue_name}'...")
    queue_parameters = QueueCreateOrUpdateParameters()
    servicebus_client.queues.create_or_update(resource_group_name, namespace_name, queue_name, queue_parameters)
    print(f"Queue '{queue_name}' created successfully.")

def delete_queue(queue_name):
    print(f"Deleting queue '{queue_name}'...")
    servicebus_client.queues.delete(resource_group_name, namespace_name, queue_name)
    print(f"Queue '{queue_name}' deleted successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python manage_azure_service_bus.py [create_ns|delete_ns|list|create_queue|delete_queue] [queue_name]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command in ["create_ns", "delete_ns", "list"]:
        if command == "create_ns":
            create_namespace()
        elif command == "delete_ns":
            delete_namespace()
        elif command == "list":
            list_queues()
    elif command in ["create_queue", "delete_queue"]:
        if len(sys.argv) < 3:
            print("Error: queue_name is required.")
            sys.exit(1)
        queue_name = sys.argv[2]
        if command == "create_queue":
            create_queue(queue_name)
        elif command == "delete_queue":
            delete_queue(queue_name)
    else:
        print("Error: Invalid command.")
        sys.exit(1)