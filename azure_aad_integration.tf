provider "azuread" {}

resource "azuread_application" "app" {
  name = "myapp"
}

resource "azuread_service_principal" "sp" {
  application_id = azuread_application.app.application_id
}

resource "azuread_group" "group" {
  name        = "mygroup"
  description = "My group description"
}

resource "azuread_user" "user" {
  user_principal_name = "user1@mydomain.com"
  display_name        = "User 1"
  password            = "MyPassw0rd!"
}

resource "azuread_group_member" "group_member" {
  group_object_id = azuread_group.group.id
  member_object_id = azuread_user.user.id
}