import shutil
import psutil
import time

# def to check disk space on laptop
def check_disk_usage(disk):
    du= shutil.disk_usage(disk)
    #free disk space= free/2**30 in Gb.
    fds= du.free/(2**30)
    print ("test disk space:"+str(fds))
    return fds

#def to check cpu usage on laptop
def check_cpu_usage():
    usage=psutil.cpu_percent(1)
    if  usage < 75:
        print("CPU usage:", usage, "%")
        return usage  # Return the CPU usage value if less than 75

    else:
        print("CPU usage too high")
        return None

#main function
def main():
    disk_to_check = 'C:/'
    #compare disk space from C:/ drive and check cpu usage 
    file_path= "C:\\Users\\f3l1x\\OneDrive\\Desktop\\Automation\\health_check.txt"
    
    while True:
        with open(file_path, 'a' ) as file:
            if  check_disk_usage(disk_to_check) <121  or not check_cpu_usage:
                x=("ERROR!!!\n Contact IT Support at 999-999-9999\nEither low disk space or high cpu usage.")
                print("ERROR!!!\n Contact IT Support at 999-999-9999\nEither low disk space or high cpu usage.")
                y="Disk space should be greater than 121. \nYou currently have: "+ str(check_disk_usage(disk_to_check))
                print("Disk space should be greater than 121. \nYou currently have: "+ str(check_disk_usage(disk_to_check)))
                file.write(x)
                file.write(y)
            else:
                file.write("\n")
                z="Everything is OK\n"
                file.write(z)
                print("Everything is ok")
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                print("Time executed:", current_time)
                file.write("Time executed: " + current_time + "\n")
                file.write("Free disk space: " + str(check_disk_usage(disk_to_check)) + "\n")
                cpu_usage = check_cpu_usage()
                if cpu_usage is not None:
                    file.write("CPU usage: " + str(cpu_usage) + "%\n")
                else:
                    file.write("Error CPU Usage too high!!!!")
        # Wait for x amount of seconds before running again
        time.sleep(15)


if __name__ == "__main__":
    main()
