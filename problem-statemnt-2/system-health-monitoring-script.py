import psutil

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Function to check CPU usage
def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"CPU usage is above threshold: {cpu_usage}%")

# Function to check memory usage
def check_memory():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        print(f"Memory usage is above threshold: {memory_usage}%")

# Function to check disk usage
def check_disk():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        print(f"Disk usage is above threshold: {disk_usage}%")

# Function to check running processes
def check_processes():
    running_processes = len(psutil.pids())
    print(f"Number of running processes: {running_processes}")

# Run checks
check_cpu()
check_memory()
check_disk()
check_processes()
