# Import required libraries
import sys
import requests
import json

# Set required variables
databricks_instance = "https://your-databricks-instance-url"
access_token = "your_access_token"

# Set required headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

def list_clusters():
    print("Listing clusters:")
    response = requests.get(f"{databricks_instance}/api/2.0/clusters/list", headers=headers)
    clusters = response.json()["clusters"]
    for cluster in clusters:
        print(f"  - {cluster['cluster_name']} (ID: {cluster['cluster_id']})")

def get_cluster(cluster_id):
    print(f"Getting cluster '{cluster_id}'...")
    response = requests.get(f"{databricks_instance}/api/2.0/clusters/get?cluster_id={cluster_id}", headers=headers)
    cluster = response.json()
    print(f"Cluster '{cluster_id}':")
    print(json.dumps(cluster, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python manage_azure_databricks.py [list|get] [cluster_id]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "list":
        list_clusters()
    elif command == "get":
        if len(sys.argv) < 3:
            print("Error: cluster_id is required.")
            sys.exit(1)
        cluster_id = sys.argv[2]
        get_cluster(cluster_id)
    else:
        print("Error: Invalid command.")
        sys.exit(1)