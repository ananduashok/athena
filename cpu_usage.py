import psutil

cpu = psutil.cpu_percent(None)
cpu1 = psutil.cpu_percent(1.0)
cpu2 = psutil.cpu_percent(0.0)

print(cpu,cpu1,cpu2)