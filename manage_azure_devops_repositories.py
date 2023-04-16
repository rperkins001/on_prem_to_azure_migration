# Import required libraries
import sys
import requests
import json

# Set required variables
organization = "your_organization_name"
project = "your_project_name"
personal_access_token = "your_personal_access_token"

# Set required headers
headers = {
    "Authorization": f"Basic {personal_access_token}",
    "Content-Type": "application/json"
}

def list_repositories():
    print("Listing repositories:")
    url = f"https://dev.azure.com/{organization}/{project}/_apis/git/repositories?api-version=6.0"
    response = requests.get(url, headers=headers)
    repositories = response.json()["value"]
    for repo in repositories:
        print(f"  - {repo['name']} (ID: {repo['id']})")

def create_repository(repo_name):
    print(f"Creating repository '{repo_name}'...")
    url = f"https://dev.azure.com/{organization}/{project}/_apis/git/repositories?api-version=6.0"
    data = {
        "name": repo_name,
        "project": {
            "name": project
        }
    }
    response = requests.post(url, headers=headers, json=data)
    repo = response.json()
    print(f"Repository '{repo_name}' created successfully (ID: {repo['id']})")

def delete_repository(repo_id):
    print(f"Deleting repository '{repo_id}'...")
    url = f"https://dev.azure.com/{organization}/{project}/_apis/git/repositories/{repo_id}?api-version=6.0"
    response = requests.delete(url, headers=headers)
    print(f"Repository '{repo_id}' deleted successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python manage_azure_devops_repositories.py [list|create|delete] [repo_name|repo_id]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "list":
        list_repositories()
    elif command in ["create", "delete"]:
        if len(sys.argv) < 3:
            print("Error: repo_name or repo_id is required.")
            sys.exit(1)
        repo_name_or_id = sys.argv[2]
        if command == "create":
            create_repository(repo_name_or_id)
        elif command == "delete":
            delete_repository(repo_name_or_id)
    else:
        print("Error: Invalid command.")
        sys.exit(1)