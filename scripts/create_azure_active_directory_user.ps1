# Script to create an Azure Active Directory user

# Define variables
$displayName = "John Doe"
$userPrincipalName = "johndoe@contoso.com"
$password = "myp@ssw0rd123"

# Create the user
New-AzADUser -DisplayName $displayName -UserPrincipalName $userPrincipalName -Password $password
