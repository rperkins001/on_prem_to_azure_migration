provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"
}

resource "azurerm_express_route_circuit" "example" {
  name                  = "example-ercircuit"
  resource_group_name   = azurerm_resource_group.example.name
  location              = azurerm_resource_group.example.location
  service_provider_name = "example-provider"
  peering_location      = "example-peering-location"
  bandwidth_in_mbps     = 50

  sku {
    tier   = "Standard"
    family = "MeteredData"
  }
}