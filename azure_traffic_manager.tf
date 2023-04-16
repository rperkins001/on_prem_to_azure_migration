provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"
}

resource "azurerm_traffic_manager_profile" "example" {
  name                 = "example-tmprofile"
  resource_group_name  = azurerm_resource_group.example.name
  traffic_routing_method = "Performance"

  dns_config {
    relative_name = "example-tm"
    ttl           = 60
  }

  monitor_config {
    protocol = "HTTP"
    port     = 80
    path     = "/"
  }
}

resource "azurerm_traffic_manager_endpoint" "example_endpoint1" {
  name                = "example-endpoint1"
  resource_group_name = azurerm_resource_group.example.name
  profile_name        = azurerm_traffic_manager_profile.example.name
  type                = "Microsoft.Network/trafficManagerProfiles/azureEndpoints"
  target_resource_id  = "/subscriptions/your_subscription_id/resourceGroups/your_resource_group/providers/Microsoft.Compute/virtualMachines/your_vm_name"
  endpoint_status     = "Enabled"
  weight              = 1
  priority            = 1
  endpoint_location   = "East US"
}

# Add more azurerm_traffic_manager_endpoint resources as needed.