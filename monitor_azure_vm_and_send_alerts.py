# Import required libraries
import os
from azure.identity import AzureCliCredential
from azure.mgmt.monitor import MonitorManagementClient
from azure.mgmt.monitor.models import ActivityLogAlertResource, ActivityLogAlertAllOfCondition, ActivityLogAlertLeafCondition
import smtplib
from email.message import EmailMessage

# Set required variables
subscription_id = "your_subscription_id"
resource_group_name = "your_resource_group_name"
alert_name = "your_alert_name"
email_address = "your_email_address"
email_password = "your_email_password"

# Authenticate using Azure CLI credentials
credentials = AzureCliCredential()

# Create a MonitorManagementClient object
monitor_client = MonitorManagementClient(credentials, subscription_id)

# Create an Activity Log Alert
all_of_conditions = ActivityLogAlertAllOfCondition(all_of=[
    ActivityLogAlertLeafCondition(field="category", equals="Administrative"),
    ActivityLogAlertLeafCondition(field="resourceGroup", equals=resource_group_name)
])
alert = ActivityLogAlertResource(location="Global", all_of=all_of_conditions)

# Check if the alert exists
alert_exists = False
try:
    existing_alert = monitor_client.activity_log_alerts.get(resource_group_name, alert_name)
    alert_exists = True
except Exception as e:
    pass

# Send an email if the alert exists
if alert_exists:
    msg = EmailMessage()
    msg.set_content(f"An alert ({alert_name}) for the resource group '{resource_group_name}' has been triggered in your Azure subscription.")
    msg["Subject"] = f"Azure Alert: {alert_name}"
    msg["From"] = email_address
    msg["To"] = email_address

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

    print(f"Email alert sent for {alert_name}.")
else:
    print(f"No alert found for {alert_name}.")