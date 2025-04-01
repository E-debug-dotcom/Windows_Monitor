# Windows System Health Monitor 🖥️⚡

This project provides a system health monitor for Windows that tracks the current status of your system's resources, such as CPU usage, RAM usage, Disk usage, and more. The monitor also checks the network connection and provides a detailed report of the most resource-intensive processes running on your system.

The monitor is implemented using Python and PowerShell scripts, and it can be run with a graphical user interface (GUI) built using Tkinter. The GUI allows users to see real-time system stats, including CPU, RAM, and disk usage, in an easy-to-read table format.

## Features ✨

- **Real-time monitoring** of CPU, RAM, and Disk usage 📊
- Displays **top running processes** by CPU usage 🔝
- **Network status check** to verify internet connectivity 🌐
- Provides a **GUI** using Tkinter to visualize system health 🖼️
- Automatically fetches and updates system health data from PowerShell scripts 🧠

## Requirements 📦

### Python Dependencies

Make sure you have the following Python libraries installed:

- `psutil` - For system resource monitoring.
- `tkinter` - For GUI.
- `subprocess` - To run PowerShell scripts from Python.

You can install the required Python libraries by running:

```bash
pip install psutil
```
## How It Works 🔍
The Python script calls the PowerShell script (system_health.ps1) to fetch system health information like CPU usage, memory usage, disk usage, and network status.

The data is then parsed and displayed in a GUI format using tkinter.

The GUI updates every few seconds to display real-time data 🔄.

## Contributions 🤝
Feel free to open issues, fork the repository, and contribute with pull requests! 🚀
