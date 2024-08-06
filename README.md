# System-Health-Monitoring

**Purpose:**
This Python script monitors system health by checking CPU usage, memory usage, disk usage, and running processes. It logs warnings when values exceed predefined thresholds.

**Dependencies:**
* psutil
* logging

**Configuration:**
* **CPU_THRESHOLD:** Sets the maximum allowed CPU usage percentage.
* **MEMORY_THRESHOLD:** Sets the maximum allowed memory usage percentage.
* **DISK_THRESHOLD:** Sets the maximum allowed disk usage percentage.
* **LOG_FILE:** Specifies the path to the log file.

**How it works:**
1. Imports necessary libraries and sets up logging.
2. Defines functions to check CPU usage, memory usage, disk usage, and running processes.
3. Each function calculates the respective metric and logs a warning if it exceeds the threshold.
4. The `main` function calls all check functions.

**Usage:**
1. Ensure required dependencies are installed (`psutil` and `logging`).
2. Adjust configuration parameters as needed.
3. Run the script `python3 app.py`.

**Output:**
The script logs warning messages to the specified log file when system health metrics exceed thresholds.

**Example Output (Log file):**
```
2024-08-06 10:14:49,056 - WARNING - CPU usage is high: 12.8%
2024-08-06 10:14:49,057 - WARNING - Memory usage is high: 67.1%
2024-08-06 10:14:49,057 - WARNING - Disk usage is high: 31.2%
```
