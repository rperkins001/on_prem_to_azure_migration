# Define Input Variables
variable "resource_group_name" {
  type        = string
  description = "Name of the Resource Group in which to create the Storage Account"
}

variable "location" {
  type        = string
  description = "Location of the Resource Group in which to create the Storage Account"
}

variable "storage_account_name" {
  type        = string
  description = "Name of the Azure Storage Account to create"
}

variable "account_tier" {
  type        = string
  description = "The performance tier for the Storage Account"
  default     = "Standard"
}

variable "account_replication_type" {
  type        = string
  description = "The type of replication to use for the Storage Account"
  default     = "LRS"
}