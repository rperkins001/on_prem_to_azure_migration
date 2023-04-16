# Script to create an Azure Event Grid subscription

# Define variables
$resourceGroupName = "MyResourceGroup"
$topicName = "MyTopic"
$subscriptionName = "MySubscription"
$endpointUrl = "https://myendpoint.com"

# Create the subscription
New-AzEventGridSubscription -ResourceGroupName $resourceGroupName -TopicName $topicName -SubscriptionName $subscriptionName -Endpoint $endpointUrl
