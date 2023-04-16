# Import required libraries
import sys
from azureml.core import Workspace
from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException

# Set required variables
subscription_id = "your_subscription_id"
resource_group_name = "your_resource_group_name"
workspace_name = "your_workspace_name"
location = "your_location"

# Create an Azure Machine Learning workspace object
ws = Workspace.create(name=workspace_name,
                      subscription_id=subscription_id,
                      resource_group=resource_group_name,
                      location=location,
                      exist_ok=True)

def list_compute_targets():
    print("Listing compute targets:")
    compute_targets = ws.compute_targets
    for compute_target_name in compute_targets:
        print(f"  - {compute_target_name}")

def create_compute_target(cluster_name, vm_size, max_nodes):
    print(f"Creating compute target '{cluster_name}'...")
    try:
        compute_target = ComputeTarget(workspace=ws, name=cluster_name)
        print(f"Compute target '{cluster_name}' already exists.")
    except ComputeTargetException:
        compute_config = AmlCompute.provisioning_configuration(vm_size=vm_size, max_nodes=max_nodes)
        compute_target = ComputeTarget.create(ws, cluster_name, compute_config)
        compute_target.wait_for_completion(show_output=True)
        print(f"Compute target '{cluster_name}' created successfully.")

def delete_compute_target(cluster_name):
    print(f"Deleting compute target '{cluster_name}'...")
    try:
        compute_target = ComputeTarget(workspace=ws, name=cluster_name)
        compute_target.delete()
        print(f"Compute target '{cluster_name}' deleted successfully.")
    except ComputeTargetException:
        print(f"Error: Compute target '{cluster_name}' not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python manage_azure_ml_services.py [list|create|delete] [cluster_name] [vm_size] [max_nodes]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "list":
        list_compute_targets()
    elif command in ["create", "delete"]:
        if len(sys.argv) < 3:
            print("Error: cluster_name is required.")
            sys.exit(1)
        cluster_name = sys.argv[2]
        if command == "create":
            if len(sys.argv) < 5:
                print("Error: vm_size and max_nodes are required.")
                sys.exit(1)
            vm_size = sys.argv[3]
            max_nodes = int(sys.argv[4])
            create_compute_target(cluster_name, vm_size, max_nodes)
        elif command == "delete":
            delete_compute_target(cluster_name)
    else:
        print("Error: Invalid command.")
        sys.exit(1)