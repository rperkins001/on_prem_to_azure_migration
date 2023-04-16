provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"
}

resource "azurerm_cognitive_account" "example" {
  name                  = "example-cogservices"
  location              = azurerm_resource_group.example.location
  resource_group_name   = azurerm_resource_group.example.name
  kind                  = "TextAnalytics"
  sku_name              = "S0"

  tags = {
    environment = "test"
  }
}

output "cognitive_services_account_endpoint" {
  value = azurerm_cognitive_account.example.endpoint
}

output "cognitive_services_account_primary_access_key" {
  value = azurerm_cognitive_account.example.primary_access_key
}
