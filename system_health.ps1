# Get CPU Usage
$cpuUsage = (Get-WmiObject -Class Win32_Processor | Select-Object -ExpandProperty LoadPercentage | Measure-Object -Minimum).Minimum

# Get RAM Usage
$ramInfo = Get-WmiObject -Class Win32_OperatingSystem
$totalRam = [math]::round($ramInfo.TotalVisibleMemorySize / 1MB, 2)
$freeRam = [math]::round($ramInfo.FreePhysicalMemory / 1MB, 2)
$usedRam = $totalRam - $freeRam
$ramUsagePercentage = [math]::round(($usedRam / $totalRam) * 100, 2)

# Get Network Status (Ping Google to check)
$pingResult = Test-Connection -ComputerName google.com -Count 1 -Quiet
$networkStatus = if ($pingResult) { $true } else { $false }

# Get Disk Usage
$diskUsage = Get-PSDrive -PSProvider FileSystem | Select-Object Name, 
    @{Name="Free(GB)";Expression={[math]::Round($_.Free/1GB,2)}}, 
    @{Name="Used(GB)";Expression={[math]::Round($_.Used/1GB,2)}}

# Get Top Processes (CPU)
$topProcesses = Get-Process | Select-Object -First 5 Name, @{Name="CPU";Expression={[math]::Round($_.CPU, 2)}}

# Output as JSON
$output = @{
    CPU_Usage = "$cpuUsage%"
    RAM_Usage = "$ramUsagePercentage%"
    Network_Status = $networkStatus
    Disk_Usage = $diskUsage
    Top_Processes = $topProcesses
}

$output | ConvertTo-Json -Depth 4
