# Greenie-s-Test-Task

# Power Consumption Monitor for Application

This Python script allows you to monitor the power consumption of a specific application running on your system. It uses the `psutil` library to gather CPU usage data and calculates the power consumption based on CPU frequency and usage percentage.

## Prerequisites

- Python 3.x installed on your system.
- `psutil` library installed. If you haven't installed it yet, you can do so using the following command:

```bash
pip install psutil
```

## How the Script Works

1. The script starts by importing the required modules: `psutil` for system monitoring and `time` for controlling time intervals.
2. The `get_power_consumption(app_name)` function is defined to calculate the power consumption of the specified application (`app_name`).
3. Inside the function:
   - A `duration` variable is initialized to 0, and an empty list `data` is created to store power consumption values during the monitoring period.
   - The script tries to find the process ID (PID) of the application specified by `app_name`. It iterates through all running processes using `psutil.process_iter()`, and if it finds a process with a matching name, it stores its PID in the `pid` variable.
   - If the application is not found or is not running, an appropriate message is displayed, and the function returns.
   - A loop runs for a duration of 15 seconds (you can modify this duration as needed).
   - Within the loop, the script fetches CPU usage data of the application and calculates its power consumption.
   - The power consumption is displayed, and the current value is added to the `data` list.
   - The loop waits for 2 seconds using `time.sleep(2)` to space out the measurements.
   - The loop increments the `duration` variable to keep track of the total monitoring time.
4. After the loop finishes, the average power consumption of the application during the monitoring period is calculated by summing up all data points in `data` and dividing by the total `duration`.
5. The average power consumption is displayed, and the monitoring process ends.

## How to Use the Script

1. Save the script in a Python file, e.g., `power_monitor.py`.
2. Make sure the `psutil` library is installed (see prerequisites).
3. Modify the `app_name` variable at the end of the script to the name of the application you want to monitor (e.g., `"Revit.exe"`).
4. Run the script using the following command:

```bash
python power_monitor.py
```

5. The script will monitor the specified application for 15 seconds (adjustable). During this time, it will display the power consumption at regular intervals (every 2 seconds). At the end of the monitoring period, it will show the average power consumption for the entire duration.

Note: The accuracy of the power consumption calculation may vary depending on the system's power management features and the precision of `psutil` data.

Please ensure that the application you want to monitor is running during the execution of the script.