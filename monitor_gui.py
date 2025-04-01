import tkinter as tk
from tkinter import ttk
import subprocess
import json
import psutil
import os
import platform
import threading

# Function to run PowerShell script and retrieve system health data
def get_system_health():
    # Running the PowerShell script and getting the output
    result = subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', 'system_health.ps1'], capture_output=True, text=True)
    
    # If PowerShell script ran successfully, return the JSON data
    if result.returncode == 0:
        return json.loads(result.stdout)
    else:
        return {}

# Function to update the GUI with system health data
def update_gui():
    # Retrieve system health data
    system_health = get_system_health()
    
    # Update CPU usage label
    cpu_usage_label.config(text=f"CPU Usage: {system_health.get('CPU_Usage', 'N/A')}")
    
    # Update RAM usage label
    ram_usage_label.config(text=f"RAM Usage: {system_health.get('RAM_Usage', 'N/A')}")
    
    # Update Network status label
    network_status_label.config(text=f"Network Status: {'Connected' if system_health.get('Network_Status', False) else 'Disconnected'}")
    
    # Update Top Processes Table
    for i, process in enumerate(system_health.get('Top_Processes', [])):
        if i < len(top_processes_table.get_children()):
            top_processes_table.item(top_processes_table.get_children()[i], values=(process['Name'], process['CPU']))
        else:
            top_processes_table.insert('', 'end', values=(process['Name'], process['CPU']))
    
    # Update Disk Usage Table
    for i, disk in enumerate(system_health.get('Disk_Usage', [])):
        if i < len(disk_table.get_children()):
            disk_table.item(disk_table.get_children()[i], values=(disk['Name'], f"{disk['Free(GB)']} GB", f"{disk['Used(GB)']} GB"))
        else:
            disk_table.insert('', 'end', values=(disk['Name'], f"{disk['Free(GB)']} GB", f"{disk['Used(GB)']} GB"))
    
    # Refresh the GUI every 5 seconds
    root.after(5000, update_gui)

# Creating the main window (root)
root = tk.Tk()
root.title("System Health Monitor")

# CPU Usage label
cpu_usage_label = tk.Label(root, text="CPU Usage: N/A", font=('Arial', 14))
cpu_usage_label.pack(pady=10)

# RAM Usage label
ram_usage_label = tk.Label(root, text="RAM Usage: N/A", font=('Arial', 14))
ram_usage_label.pack(pady=10)

# Network Status label
network_status_label = tk.Label(root, text="Network Status: N/A", font=('Arial', 14))
network_status_label.pack(pady=10)

# Top Processes Table
top_processes_label = tk.Label(root, text="Top 5 Processes", font=('Arial', 14))
top_processes_label.pack(pady=10)

top_processes_table = ttk.Treeview(root, columns=("Process", "CPU Usage"), show="headings")
top_processes_table.heading("Process", text="Process")
top_processes_table.heading("CPU Usage", text="CPU Usage (%)")
top_processes_table.pack(pady=10)

# Disk Usage Table
disk_usage_label = tk.Label(root, text="Disk Usage", font=('Arial', 14))
disk_usage_label.pack(pady=10)

disk_table = ttk.Treeview(root, columns=("Disk", "Free(GB)", "Used(GB)"), show="headings")
disk_table.heading("Disk", text="Disk")
disk_table.heading("Free(GB)", text="Free(GB)")
disk_table.heading("Used(GB)", text="Used(GB)")
disk_table.pack(pady=10)

# Start the GUI update
update_gui()

# Run the application
root.mainloop()
