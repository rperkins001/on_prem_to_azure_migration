resource "azurerm_storage_account" "example" {
  name                     = "examplestorageacc"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_sql_server_extended_auditing_policy" "example" {
  server_id                              = azurerm_sql_server.example.id
  storage_endpoint                       = azurerm_storage_account.example.primary_blob_endpoint
  storage_account_access_key             = azurerm_storage_account.example.primary_access_key
  storage_account_access_key_is_secondary = false
  retention_in_days                      = 30
}

resource "azurerm_sql_server_security_alert_policy" "example" {
  server_id               = azurerm_sql_server.example.id
  state                   = "Enabled"
  email_account_admins    = true
  email_addresses         = ["example@example.com"]
  disabled_alerts         = []
  retention_days          = 30
}