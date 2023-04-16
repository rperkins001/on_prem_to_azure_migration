provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "myResourceGroup"
  location = "East US"
}

resource "azurerm_key_vault" "kv" {
  name                = "myKeyVault"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  tenant_id           = "YOUR_TENANT_ID"

  sku_name = "standard"

  access_policy {
    tenant_id = azurerm_key_vault_access_policy.ap.tenant_id
    object_id = azurerm_key_vault_access_policy.ap.object_id

    key_permissions = [
      "get",
      "create",
      "delete",
      "list",
      "update",
      "import",
      "backup",
      "restore"
    ]

    secret_permissions = [
      "get",
      "list",
      "set",
      "delete",
      "backup",
      "restore"
    ]
  }

  tags = {
    Environment = "Prod"
  }
}

resource "azurerm_key_vault_access_policy" "ap" {
  key_vault_id = azurerm_key_vault.kv.id

  tenant_id = "YOUR_TENANT_ID"
  object_id = "YOUR_OBJECT_ID"

  key_permissions = [
    "get",
    "list"
  ]

  secret_permissions = [
    "get",
    "list"
  ]
}