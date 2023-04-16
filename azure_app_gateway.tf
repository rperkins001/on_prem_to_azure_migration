# Provider configuration
provider "azurerm" {
  features {}
}

# Resource group creation
resource "azurerm_resource_group" "example" {
  name     = "my-resource-group"
  location = "West US"
}

# Virtual network creation
resource "azurerm_virtual_network" "example" {
  name                = "my-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
}

# Subnet creation
resource "azurerm_subnet" "example" {
  name                 = "my-subnet"
  resource_group_name  = azurerm_resource_group.example.name
  virtual_network_name = azurerm_virtual_network.example.name
  address_prefixes     = ["10.0.1.0/24"]
}

# Public IP address creation
resource "azurerm_public_ip" "example" {
  name                = "my-public-ip"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  allocation_method   = "Static"
  sku                 = "Standard"
}

# Application Gateway creation
resource "azurerm_application_gateway" "example" {
  name                = "my-app-gateway"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  sku {
    name     = "WAF_v2"
    tier     = "WAF_v2"
    capacity = 2
    }
  }

  gateway_ip_configuration {
    name      = "my-gateway-ip-config"
    subnet_id = azurerm_subnet.example.id
    public_ip_address_id = azurerm_public_ip.example.id
  }

  frontend_port {
    name = "http"
    port = 80
  }

  frontend_ip_configuration {
    name                = "my-frontend-ip-config"
    public_ip_address_id = azurerm_public_ip.example.id
  }

  backend_address_pool {
    name = "my-backend-pool"
    backend_address {
      fqdn = "myapp.azurewebsites.net"
    }
  }

  http_listener {
    name                           = "my-http-listener"
    frontend_ip_configuration_name = "my-frontend-ip-config"
    frontend_port_name             = "http"
    protocol                       = "Http"
    host_name                      = "myapp.mydomain.com"
  }

  request_routing_rule {
    name                       = "my-routing-rule"
    rule_type                  = "Basic"
    http_listener_name         = "my-http-listener"
    backend_address_pool_name  = "my-backend-pool"
    backend_http_settings_name = "my-backend-http-settings"
  }

  backend_http_settings {
    name                  = "my-backend-http-settings"
    cookie_based_affinity = "Disabled"
    path                  = "/"
    port                  = 80
    protocol              = "Http"
  }

  web_application_firewall_configuration {
    enabled = true

    firewall_mode = "Prevention"

    request_body_check = true

    max_request_body_size_in_kb = 128

    file_upload_limit_in_mb = 100

    exclusion {
      match_variable = "RequestUri"
      selector       = "StartsWith"
      value          = "/static/"
    }

    managed_rules {
      enabled = true

      managed_rule_set {
        rule_set_type = "OWASP"


        rule_set_version = "3.1"

        rule_group_override {
            rule_group_name = "REQUEST-942-APPLICATION-ATTACK-SQLI"
            rules           = ["941100", "941320"]
        }
      }
    }
  }

