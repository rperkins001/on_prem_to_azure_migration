# Script to create an Azure SQL Database

# Define variables
$resourceGroupName = "MyResourceGroup"
$serverName = "MyServer"
$databaseName = "MyDatabase"
$collation = "SQL_Latin1_General_CP1_CI_AS"
$edition = "Standard"
$serviceObjectiveName = "S1"

# Create the SQL database
New-AzSqlDatabase -ResourceGroupName $resourceGroupName -ServerName $serverName -DatabaseName $databaseName -Collation $collation -Edition $edition -RequestedServiceObjectiveName $serviceObjectiveName
