# Import required libraries
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import sys

# Set required variables
key_vault_url = "https://your-key-vault-name.vault.azure.net/"

# Authenticate using DefaultAzureCredential
credentials = DefaultAzureCredential()

# Create a SecretClient object to interact with the Key Vault
secret_client = SecretClient(vault_url=key_vault_url, credential=credentials)

def list_secrets():
    print("Listing secrets:")
    secrets = secret_client.list_properties_of_secrets()
    for secret in secrets:
        print(f"  - {secret.name}")

def set_secret(secret_name, secret_value):
    print(f"Setting secret '{secret_name}'...")
    secret_client.set_secret(secret_name, secret_value)
    print(f"Secret '{secret_name}' set successfully.")

def get_secret(secret_name):
    print(f"Getting secret '{secret_name}'...")
    secret = secret_client.get_secret(secret_name)
    print(f"Secret '{secret_name}': {secret.value}")

def delete_secret(secret_name):
    print(f"Deleting secret '{secret_name}'...")
    secret_client.begin_delete_secret(secret_name)
    print(f"Secret '{secret_name}' deleted successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python manage_key_vault_secrets.py [list|set|get|delete] [secret_name] [secret_value]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "list":
        list_secrets()
    elif command in ["set", "get", "delete"]:
        if len(sys.argv) < 3:
            print("Error: secret_name is required.")
            sys.exit(1)
        secret_name = sys.argv[2]
        if command == "set":
            if len(sys.argv) < 4:
                print("Error: secret_value is required.")
                sys.exit(1)
            secret_value = sys.argv[3]
            set_secret(secret_name, secret_value)
        elif command == "get":
            get_secret(secret_name)
        elif command == "delete":
            delete_secret(secret_name)
    else:
        print("Error: Invalid command.")
        sys.exit(1)