# Import required libraries
import sys
from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

# Set required variables
subscription_id = "your_subscription_id"
resource_group_name = "your_resource_group_name"

# Authenticate using DefaultAzureCredential
credentials = DefaultAzureCredential()

# Create a NetworkManagementClient object
network_client = NetworkManagementClient(credentials, subscription_id)

def list_application_gateways():
    print("Listing application gateways:")
    application_gateways = network_client.application_gateways.list(resource_group_name)
    for app_gateway in application_gateways:
        print(f"  - {app_gateway.name}")

def show_application_gateway_configuration(app_gateway_name):
    print(f"Showing configuration for application gateway '{app_gateway_name}':")
    app_gateway = network_client.application_gateways.get(resource_group_name, app_gateway_name)

    print("Backend address pools:")
    for backend_pool in app_gateway.backend_address_pools:
        print(f"  - {backend_pool.name}")

    print("\nBackend HTTP settings:")
    for backend_http_settings in app_gateway.backend_http_settings_collection:
        print(f"  - {backend_http_settings.name}")

    print("\nHTTP listeners:")
    for http_listener in app_gateway.http_listeners:
        print(f"  - {http_listener.name}")

    print("\nRequest routing rules:")
    for request_routing_rule in app_gateway.request_routing_rules:
        print(f"  - {request_routing_rule.name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python monitor_azure_application_gateway.py [list|show] [app_gateway_name]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "list":
        list_application_gateways()
    elif command == "show":
        if len(sys.argv) < 3:
            print("Error: app_gateway_name is required.")
            sys.exit(1)
        app_gateway_name = sys.argv[2]
        show_application_gateway_configuration(app_gateway_name)
    else:
        print("Error: Invalid command.")
        sys.exit(1)