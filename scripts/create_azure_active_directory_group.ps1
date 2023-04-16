# Script to create an Azure Active Directory group

# Define variables
$displayName = "My Group"
$mailNickname = "mygroup"
$description = "My group description"

# Create the group
New-AzADGroup -DisplayName $displayName -MailNickname $mailNickname -Description $description
