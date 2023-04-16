# Provider Configuration
provider "azurerm" {
  features {}
}

# Resource Group Creation
resource "azurerm_resource_group" "storage_rg" {
  name     = "storage-rg"
  location = "eastus"
}

# Storage Account Creation
resource "azurerm_storage_account" "storage_account" {
  name                     = "mystorageaccount"
  resource_group_name      = azurerm_resource_group.storage_rg.name
  location                 = azurerm_resource_group.storage_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  # Encryption Configuration
  encryption {
    services {
      blob {
        enabled = true
      }
    }
    key_source = "Microsoft.Storage"
  }

  # Network Rule Configuration
  network_rules {
    default_action             = "Deny"
    virtual_network_subnet_ids = []
    ip_rules                   = []
  }

  # Blob Service Properties Configuration
  blob_properties {
    delete_retention_policy {
      enabled = false
    }
    versioning {
      enabled = false
    }
  }
}