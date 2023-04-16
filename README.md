Azure Security Automation Repository

This repository contains scripts and configurations for automating security and infrastructure tasks in Azure as a Python Developer. The primary 
focus is on protecting sensitive data, minimizing the risk of cyber-attacks, and migrating on-premises resources to the Azure cloud platform.

Key Responsibilities

    Building automation pipelines
    Designing and using APIs
    Creating and maintaining security as code
    Integrating security throughout the development and deployment process
    Collaborating with architects, developers, and business units
    
PowerShell Scripts

    create_azure_resourcegroup.ps1 - Create an Azure Resource Group
    create_azure_storageaccount.ps1 - Create an Azure Storage Account
    create_azure_virtualnetwork.ps1 - Create an Azure Virtual Network
    create_azure_virtualmachine.ps1 - Create an Azure Virtual Machine
    create_azure_active_directory_user.ps1 - Create an Azure Active Directory User
    create_azure_active_directory_group.ps1 - Create an Azure Active Directory Group
    create_azure_key_vault.ps1 - Create an Azure Key Vault
    manage_azure_resource_locks.ps1 - Manage Azure Resource Locks
    manage_azure_policy_assignments.ps1 - Manage Azure Policy Assignments
    manage_azure_policy_assignments.ps1 - Manage Azure Security Center
    manage_azure_analytics_workspace.ps1 - Manage Azure Log Analytics Workspace
    create_azure_sql_database.ps1 - Create an Azure SQL Database
    create_azure_app_service.ps1 - Create an Azure App Service
    create_azure_function_app.ps1 - Create an Azure Function App
    create_azure_logic_app.ps1 - Create an Azure Logic App
    create_azure_grid_subscription.ps1 - Create an Azure Event Grid Subscription
    create_azure_event_hub_namespace.ps1 - Create an Azure Event Hub Namespace
    create_azure_notification_hub.ps1 - Create an Azure Notification Hub
    manage_azure_api_management.ps1 - Manage Azure API Management
    
Bash Scripts

    copy_data_to_azure_blob_storage.sh - Copy Data from On-Premises to Azure Blob Storage
    azure_vm_maintenance_operations.sh - Initiate Maintenance Operations on Azure Virtual Machines
    setup_azure_nsg.sh - Set Up Azure Network Security Groups
    manage_azure_container_instances.sh - Manage Azure Container Instances
    manage_azure_container_registries.sh - Manage Azure Container Registries

Python Scripts

    copy_data_to_azure_blob_storage.py - Copy Data from On-Premises to Azure Blob Storage
    deploy_azure_vm_with_arm_template.py - Deploy Azure Virtual Machines Using Azure Resource Manager (ARM) Templates
    monitor_azure_vm_and_send_alerts.py - Monitor Azure Virtual Machines and Send Alerts
    manage_key_vault_secrets.py - Manage Azure Key Vault Secrets
    manage_azure_app_configuration.py - Manage Azure App Configuration
    manage_azure_functions.py - Manage Azure Functions
    manage_azure_databricks.py - Manage Azure Databricks
    manage_event_grid_topics.py - Manage Azure Event Grid Topics
    manage_azure_service_bus.py - Manage Azure Service Bus
    manage_azure_devops_repositories.py - Manage Azure DevOps Repositories
    manage_azure_container_instances.py - Manage Azure Container Instances
    manage_azure_machine_learning_services.py - Manage Azure Machine Learning Services
    monitor_azure_network_security_groups.py - Monitor Azure Network Security Groups
    manage_key_vault_secrets.py - Monitor Azure Application Gateway
    
Terraform Configurations

    azure_cognitive_services.tf - Deploy an Azure Cognitive Services Resource
    azure_hdinsight_cluster.tf - Deploy an Azure HDInsight Cluster
    azure_traffic_manager.tf - Deploy an Azure Traffic Manager
    azure_expressroute_circuit.tf - Deploy an Azure ExpressRoute Circuit
    azure_virtual_wan.tf - Deploy an Azure Virtual WAN
    
Terraform Use Cases

    azure_vnet.tf - Virtual Network Creation: Set up a virtual network (VNet) in Azure, configuring subnets, network security groups, and rules to control traffic flow and isolate resources.
    azure_aks_cluster.tf - Azure Kubernetes Service (AKS) Cluster: Develop a Terraform script to provision an AKS cluster, enabling container orchestration and ensuring proper access control and security measures are in place.
    azure_active_directory_integration.tf - Azure Active Directory (AAD) Integration: Create a script to integrate Azure AD with your infrastructure, allowing you to manage users, groups, and access controls across your organization.
    azure_log_analytics.tf - Log Analytics Workspace: Design a Terraform script to deploy a Log Analytics Workspace for collecting and analyzing security and operational logs from your Azure resources.
    azure_key_vault.tf - Azure Key Vault: Implement a script to provision an Azure Key Vault, a secure store for secrets, keys, and certificates, and manage access policies.
    azure_application_gateway_waf.tf - Web Application Firewall (WAF): Develop a Terraform script to deploy and configure an Azure Application Gateway with a WAF, protecting your applications from common web-based attacks.
    azure_virtual_machines.tf - Azure Virtual Machines: Develop a script to provision and configure virtual machines (VMs) in Azure, ensuring proper network configuration, monitoring, and security settings.
    azure_storage_account/ - Azure Storage Account: Create a script to provision and configure an Azure Storage Account with proper encryption, access control, and redundancy settings.
    azure_devops_integration/ - Azure SQL Database: Design a Terraform script to deploy and configure an Azure SQL Database with appropriate firewall rules, auditing, and threat detection settings.
    azure_devops_integration/ - Azure DevOps Pipeline Integration: Implement a Terraform script to integrate with Azure DevOps, enabling the automation of infrastructure deployment and continuous integration/continuous deployment (CI/CD) processes.
