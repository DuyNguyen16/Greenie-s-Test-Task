import psutil as p
import time as t

# define function to calculate the power consumption of the app
def get_power_consumption(app_name):
  duration = 0
  data = []

  # try get the process ID of the application
  for process in p.process_iter():
    # check if the process of the application is valid
    if process.name() == app_name:
      # initialise prid to the running process pid
      pid = process.pid
      break
  else:
    print(f"Application {app_name} not found or currently not running.")
    return
  
  print("------------------------------------------------------------------------")

  while duration < 5:
    # get the CPU power consumption of the application (Revit2023)
    cpu_counts = p.cpu_count()
    process_infomation = p.Process(pid)

    # the cpu percent that the application is using 
    cpu_percent = process_infomation.cpu_percent(1)

    # calculation for power usages
    power_usage = (p.cpu_freq().current * cpu_percent) / (cpu_counts * 100)

    # display the power consumption of the app
    print(f"The Power consumption of {app_name}: {power_usage:.2f} W.")

    # add current power usage to data array
    data.append(power_usage)

    t.sleep(2)
    duration += 1 
  
  result = sum(data) / duration

  print(f"The average Power consumption of this run for {app_name} is: {result:.2f} W.")
  print("------------------------------------------------------------------------")


# file name must be an executable file
app_name = "Revit.exe"
get_power_consumption(app_name)
