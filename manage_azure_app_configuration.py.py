# Import required libraries
from azure.identity import DefaultAzureCredential
from azure.appconfiguration import AzureAppConfigurationClient
import sys

# Set required variables
app_config_connection_string = "your_connection_string"

# Authenticate using DefaultAzureCredential
credentials = DefaultAzureCredential()

# Create an AzureAppConfigurationClient object
client = AzureAppConfigurationClient.from_connection_string(app_config_connection_string)

def list_settings():
    print("Listing settings:")
    settings = client.list_configuration_settings()
    for setting in settings:
        print(f"  - {setting.key}: {setting.value}")

def set_setting(key, value):
    print(f"Setting '{key}' to '{value}'...")
    client.set_configuration_setting(key=key, value=value)
    print(f"Setting '{key}' set successfully.")

def get_setting(key):
    print(f"Getting setting '{key}'...")
    setting = client.get_configuration_setting(key=key)
    print(f"Setting '{key}': {setting.value}")

def delete_setting(key):
    print(f"Deleting setting '{key}'...")
    client.delete_configuration_setting(key=key)
    print(f"Setting '{key}' deleted successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python manage_app_configuration.py [list|set|get|delete] [key] [value]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "list":
        list_settings()
    elif command in ["set", "get", "delete"]:
        if len(sys.argv) < 3:
            print("Error: key is required.")
            sys.exit(1)
        key = sys.argv[2]
        if command == "set":
            if len(sys.argv) < 4:
                print("Error: value is required.")
                sys.exit(1)
            value = sys.argv[3]
            set_setting(key, value)
        elif command == "get":
            get_setting(key)
        elif command == "delete":
            delete_setting(key)
    else:
        print("Error: Invalid command.")
        sys.exit(1)