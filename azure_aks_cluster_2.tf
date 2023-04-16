provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "myResourceGroup"
  location = "East US"
}

resource "azurerm_kubernetes_cluster" "aks" {
  name                = "myAKSCluster"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "myaksdns"

  linux_profile {
    admin_username = "azureuser"
  }

  agent_pool_profile {
    name            = "agentpool"
    count           = 1
    vm_size         = "Standard_D2_v2"
    os_type         = "Linux"
    max_pods        = 30
    type            = "VirtualMachineScaleSets"
    os_disk_size_gb = 30
  }

  service_principal {
    client_id     = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"
  }

  tags = {
    Environment = "Test"
  }

  addon_profile {
    kube_dashboard {
      enabled = true
    }

    azure_policy {
      enabled = true
    }

    oms_agent {
      enabled                    = true
      log_analytics_workspace_id = "YOUR_WORKSPACE_ID"
    }
  }
}

resource "azurerm_role_assignment" "aks_role_assignment" {
  scope              = azurerm_kubernetes_cluster.aks.id
  role_definition_id = "b24988ac-6180-42a0-ab88-20f7382dd24c" # Contributor role
  principal_id       = "YOUR_OBJECT_ID"
}