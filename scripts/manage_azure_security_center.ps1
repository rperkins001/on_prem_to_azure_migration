# Script to manage Azure Security Center

# Define variables
$subscriptionId = "your-subscription-id" # Replace with your subscription ID
$resourceGroupName = "MyResourceGroup"
$securityName = "MySecurityCenter"

# Enable Security Center for the subscription
Set-AzSubscription -SubscriptionId $subscriptionId -ResourceGroup $resourceGroupName -Name $securityName

# Disable Security Center for the subscription
Set-AzSubscription -SubscriptionId $subscriptionId -ResourceGroup $resourceGroupName -Name $securityName -Disable
