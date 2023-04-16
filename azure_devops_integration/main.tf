terraform {
  backend "azurerm" {
    resource_group_name  = "example-resources"
    storage_account_name = "examplestorageacc"
    container_name       = "example-tfstate"
    key                  = "terraform.tfstate"
  }
}

# Your infrastructure code here