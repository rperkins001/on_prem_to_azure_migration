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

def list_network_security_groups():
    print("Listing network security groups:")
    network_security_groups = network_client.network_security_groups.list(resource_group_name)
    for nsg in network_security_groups:
        print(f"  - {nsg.name}")

def show_network_security_group_rules(network_security_group_name):
    print(f"Showing rules for network security group '{network_security_group_name}':")
    network_security_group = network_client.network_security_groups.get(resource_group_name, network_security_group_name)
    for rule in network_security_group.security_rules:
        print(f"  - Name: {rule.name}")
        print(f"    Priority: {rule.priority}")
        print(f"    Protocol: {rule.protocol}")
        print(f"    Source address prefix: {rule.source_address_prefix}")
        print(f"    Source port range: {rule.source_port_range}")
        print(f"    Destination address prefix: {rule.destination_address_prefix}")
        print(f"    Destination port range: {rule.destination_port_range}")
        print(f"    Access: {rule.access}")
        print(f"    Direction: {rule.direction}")
        print("")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python monitor_azure_network_security_groups.py [list|show] [network_security_group_name]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "list":
        list_network_security_groups()
    elif command == "show":
        if len(sys.argv) < 3:
            print("Error: network_security_group_name is required.")
            sys.exit(1)
        network_security_group_name = sys.argv[2]
        show_network_security_group_rules(network_security_group_name)
    else:
        print("Error: Invalid command.")
        sys.exit(1)