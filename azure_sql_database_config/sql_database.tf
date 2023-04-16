resource "azurerm_sql_database" "example" {
  name                = "example-sqldatabase"
  resource_group_name = azurerm_resource_group.example.name
  server_name         = azurerm_sql_server.example.name
  location            = azurerm_resource_group.example.location
  edition             = "Standard"
  collation           = "SQL_Latin1_General_CP1_CI_AS"
  max_size_bytes      = "1073741824"

  tags = {
    environment = "production"
  }
}
