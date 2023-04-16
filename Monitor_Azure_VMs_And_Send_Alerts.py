# Script to monitor Azure virtual machines and send alerts
# Uses the Azure Monitor Python SDK

from azure.monitor.query import MetricsQueryClient
from azure.identity import DefaultAzureCredential

# Authenticate with Azure
credential = DefaultAzureCredential()

# Connect to Azure Monitor
query_client = MetricsQueryClient(credential)

# Query VM metrics
metrics = query_client.query(
    "<your resource id>",
    metrics=["Percentage CPU"],
    timespan="PT1H"
)

# Send alerts if CPU usage exceeds threshold
for metric in metrics:
    if metric["Percentage CPU"] > 80:
        # send alert
