provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "myResourceGroup"
  location = "East US"
}

resource "azurerm_virtual_network" "vnet" {
  name                = "myVnet"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  address_space       = ["10.0.0.0/16"]

  subnet {
    name           = "subnet1"
    address_prefix = "10.0.0.0/24"
  }

  subnet {
    name           = "subnet2"
    address_prefix = "10.0.1.0/24"
  }
}

resource "azurerm_network_security_group" "nsg" {
  name                = "myNSG"
  resource_group_name = azurerm_resource_group.rg.name

  security_rule {
    name                       = "allowHTTP"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "80"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

  security_rule {
    name                       = "allowSSH"
    priority                   = 200
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

resource "azurerm_subnet_network_security_group_association" "subnet1_nsg" {
  subnet_id                 = azurerm_virtual_network.vnet.subnet_subnet1.id
  network_security_group_id = azurerm_network_security_group.nsg.id
}

resource "azurerm_subnet_network_security_group_association" "subnet2_nsg" {
  subnet_id                 = azurerm_virtual_network.vnet.subnet_subnet2.id
  network_security_group_id = azurerm_network_security_group.nsg.id
}