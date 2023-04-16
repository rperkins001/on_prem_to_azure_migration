# Import required libraries
import sys
from azure.identity import DefaultAzureCredential
from azure.mgmt.eventgrid import EventGridManagementClient
from azure.mgmt.eventgrid.models import Topic

# Set required variables
subscription_id = "your_subscription_id"
resource_group_name = "your_resource_group_name"
location = "your_location"

# Authenticate using DefaultAzureCredential
credentials = DefaultAzureCredential()

# Create an EventGridManagementClient object
eventgrid_client = EventGridManagementClient(credentials, subscription_id)

def list_topics():
    print("Listing topics:")
    topics = eventgrid_client.topics.list_by_resource_group(resource_group_name)
    for topic in topics:
        print(f"  - {topic.name}")

def create_topic(topic_name):
    print(f"Creating topic '{topic_name}'...")
    topic_parameters = Topic(location=location)
    eventgrid_client.topics.create_or_update(resource_group_name, topic_name, topic_parameters)
    print(f"Topic '{topic_name}' created successfully.")

def delete_topic(topic_name):
    print(f"Deleting topic '{topic_name}'...")
    eventgrid_client.topics.delete(resource_group_name, topic_name)
    print(f"Topic '{topic_name}' deleted successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python manage_event_grid_topics.py [list|create|delete] [topic_name]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "list":
        list_topics()
    elif command in ["create", "delete"]:
        if len(sys.argv) < 3:
            print("Error: topic_name is required.")
            sys.exit(1)
        topic_name = sys.argv[2]
        if command == "create":
            create_topic(topic_name)
        elif command == "delete":
            delete_topic(topic_name)
    else:
        print("Error: Invalid command.")
        sys.exit(1)