import psutil
value = int(input("Enter the Threshold Value of the CPU"))
Current_value = psutil.cpu_percent(interval=1)
if value>Current_value:
    print("CPU is Safe")
else:
    print("Alert Email Sent!")