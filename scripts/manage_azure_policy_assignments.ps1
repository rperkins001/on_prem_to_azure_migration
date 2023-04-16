# Script to manage Azure policy assignments

# Define variables
$policyDefinitionId = "/providers/Microsoft.Authorization/policyDefinitions/9de9e8f8-ff35-4e68-82e7-f8938c3e4e82" # Replace with your policy definition ID
$scope = "/subscriptions/subscription-id/resourceGroups/resource-group-name" # Replace with the scope of the policy assignment
$policyName = "MyPolicyAssignment" # Replace with a name for the policy assignment

# Create the policy assignment
New-AzPolicyAssignment -Name $policyName -DisplayName $policyName -Scope $scope -PolicyDefinitionId $policyDefinitionId

# Remove the policy assignment
Remove-AzPolicyAssignment -Name $policyName -Scope $scope
