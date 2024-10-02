import speedtest as st
import os

#retreive best server 
server = st.Speedtest()
server.get_best_server()

down_load = server.download()
#in mb/s
down_load = down_load / 1000000
y=F"Download Speed: {down_load} Mb/s\n"
print(f"Download Speed: {down_load} Mb/s")

# Test Upload Speed
up_load = server.upload()
# in mb/s
up_load = up_load / 1000000
x=f"Upload Speed: {up_load} Mb/s\n"
print(f"Upload Speed: {up_load} Mb/s")

# Test Ping speed
ping = server.results.ping
print(f"Ping Speed: {ping}")
print(server)

file_path= "C:\\Users\\f3l1x\\OneDrive\\Desktop\\Automation\\internet_speeds.txt"

with open(file_path, "w") as file:
    file.write(x)
    file.write(y)
    


current_directory = os.getcwd()
print(f"Current directory: {current_directory}")


print("File created successfully at:", file_path,"\n")



