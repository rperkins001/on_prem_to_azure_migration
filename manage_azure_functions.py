# Import required libraries
import sys
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.web.models import FunctionEnvelope

# Set required variables
subscription_id = "your_subscription_id"
resource_group_name = "your_resource_group_name"
function_app_name = "your_function_app_name"

# Authenticate using DefaultAzureCredential
credentials = DefaultAzureCredential()

# Create a ResourceManagementClient object
resource_client = ResourceManagementClient(credentials, subscription_id)

# Create a WebSiteManagementClient object
web_client = WebSiteManagementClient(credentials, subscription_id)

def list_functions():
    print("Listing functions:")
    functions = web_client.web_apps.list_functions(resource_group_name, function_app_name)
    for function in functions:
        print(f"  - {function.name}")

def get_function(function_name):
    print(f"Getting function '{function_name}'...")
    function = web_client.web_apps.get_function(resource_group_name, function_app_name, function_name)
    print(f"Function '{function_name}':")
    print(f"  - Name: {function.name}")
    print(f"  - Script file: {function.properties.script_file}")
    print(f"  - Entry point: {function.properties.entry_point}")
    print(f"  - URL: {function.properties.invoke_url_template}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python manage_azure_functions.py [list|get] [function_name]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "list":
        list_functions()
    elif command == "get":
        if len(sys.argv) < 3:
            print("Error: function_name is required.")
            sys.exit(1)
        function_name = sys.argv[2]
        get_function(function_name)
    else:
        print("Error: Invalid command.")
        sys.exit(1)