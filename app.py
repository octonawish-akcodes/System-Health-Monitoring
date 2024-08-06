import psutil
import logging
from datetime import datetime

# Configuration (Consider using environment variables for better security)

CPU_THRESHOLD = 80.0  # CPU usage percentage threshold (e.g., 80%)
MEMORY_THRESHOLD = 40.0  # Memory usage percentage threshold (e.g., 40%)
DISK_THRESHOLD = 60.0  # Disk usage percentage threshold (e.g., 60%)
LOG_FILE = 'system_health.log'  # Path to the log file

# Setup logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def check_cpu_usage():
    """
    Checks CPU usage and logs a warning if it exceeds the threshold.

    This function retrieves the current CPU usage percentage using `psutil.cpu_percent`.
    If the usage is greater than the `CPU_THRESHOLD`, a warning message is printed and
    logged to the file specified by `LOG_FILE`.

    Args:
        None

    Returns:
        None
    """

    cpu_usage = psutil.cpu_percent(interval=1)  # Sample CPU usage for 1 second
    if cpu_usage > CPU_THRESHOLD:
        message = f'CPU usage is high: {cpu_usage}%'
        print(message)
        logging.warning(message)


def check_memory_usage():
    """
    Checks memory usage and logs a warning if it exceeds the threshold.

    This function retrieves memory usage information using `psutil.virtual_memory`.
    It calculates the percentage used and compares it to the `MEMORY_THRESHOLD`. If
    the usage is above the threshold, a warning message is printed and logged.

    Args:
        None

    Returns:
        None
    """

    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        message = f'Memory usage is high: {memory_usage}%'
        print(message)
        logging.warning(message)


def check_disk_usage():
    """
    Checks disk usage and logs a warning if it exceeds the threshold.

    This function retrieves disk usage information for the root mount point (`/`)
    using `psutil.disk_usage`. It calculates the percentage used and compares it
    to the `DISK_THRESHOLD`. If the usage is above the threshold, a warning message
    is printed and logged.

    Args:
        None

    Returns:
        None
    """

    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        message = f'Disk usage is high: {disk_usage}%'
        print(message)
        logging.warning(message)


def check_running_processes():
    """
    Checks for running processes with high CPU usage and logs them.

    This function iterates through running processes using `psutil.process_iter`
    and filters for processes with CPU usage exceeding the `CPU_THRESHOLD`.
    If such processes are found, a message listing them is printed and logged.

    Args:
        None

    Returns:
        None
    """

    processes = [
        proc.info for proc in psutil.process_iter(['pid', 'name', 'cpu_percent'])
        if proc.info['cpu_percent'] > CPU_THRESHOLD
    ]
    if processes:
        message = f'High CPU usage processes: {processes}'
        print(message)
        logging.warning(message)


def main():
    """
    The main function that calls all the system health check functions.

    This function calls each of the individual check functions (`check_cpu_usage`,
    `check_memory_usage`, `check_disk_usage`, and `check_running_processes`) to perform
    their respective checks.

    Args:
        None

    Returns:
        None
    """

    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()


if __name__ == "__main__":
    main()
