import psutil
import platform
import vision


def SystemInfo():
    def get_size(bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    # System Information
    uname = platform.uname()

    vision.speak("System Information")
    vision.speak(f"System {uname.system}, Version {uname.version}, "
                 f"Machine {uname.machine}, Processor {uname.processor}, Node Name {uname.node}")

    # CPU Information
    cpu_freq = psutil.cpu_freq()

    vision.speak("CPU Information")
    vision.speak(f"Total Number Of CPU Cores: {psutil.cpu_count(logical=True)}, "
                 f"Current CPU Frequency: {cpu_freq.current:.2f}Mhz, Total CPU Usage: {psutil.cpu_percent()}%")

    # Memory Information
    memory = psutil.virtual_memory()

    vision.speak("Memory Information")
    vision.speak(f"Total Memory Size: {get_size(memory.total)}, Total Free Memory: {get_size(memory.available)}, "
                 f"Total Used Memory: {get_size(memory.used)}")

    # Disk Information
    par_t = 0
    par_u = 0
    par_f = 0

    partitions = psutil.disk_partitions()

    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue

        par_t = par_t + partition_usage.total
        par_u = par_u + partition_usage.used
        par_f = par_f + partition_usage.free

    vision.speak("Disk Information")
    vision.speak(f"Total Size Of Your Disk: {get_size(par_t)}, "
                 f"Currently Used Disk Size: {get_size(par_u)}, Currently Free Disk Size: {get_size(par_f)}")

    # Battery information
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)

    if not plugged:
        vision.speak(f"Currently Your Battery Is {percent}% And Not Plugged In")

    else:
        vision.speak(f"Currently Your Battery Is {percent}% And Plugged In")

    return
