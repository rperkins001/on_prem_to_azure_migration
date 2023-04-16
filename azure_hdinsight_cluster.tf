provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"
}

resource "azurerm_storage_account" "example" {
  name                     = "examplestorageacc"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "GRS"
}

resource "azurerm_hdinsight_hadoop_cluster" "example" {
  name                = "example-hdinsight"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  cluster_version     = "4.0"
  tier                = "Standard"

  component_version {
    hadoop = "3.1"
  }

  gateway {
    enabled  = true
    username = "exampleuser"
    password = "ExamplePassword123!"
  }

  storage_account {
    storage_container_id = azurerm_storage_account.example.primary_blob_endpoint
    storage_account_key  = azurerm_storage_account.example.primary_access_key
    is_default           = true
  }

  roles {
    head_node {
      vm_size  = "A6"
      username = "exampleuser"
      password = "ExamplePassword123!"
    }

    worker_node {
      vm_size               = "A6"
      username              = "exampleuser"
      password              = "ExamplePassword123!"
      target_instance_count = 3
    }

    zookeeper_node {
      vm_size  = "A6"
      username = "exampleuser"
      password = "ExamplePassword123!"
    }
  }
}
