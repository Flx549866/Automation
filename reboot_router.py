import paramiko
import logging

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# Router details
router_ip = '192.168.1.1'
username = 'Admin'
password = 'Nissan@350z#'

try:
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the router
    ssh.connect(router_ip, username=username, password=password)

    # Open an interactive session
    channel = ssh.invoke_shell()

    print("Connected to the router. Type your commands below.")

    # Keep the session open to accept user input
    while True:
        command = input("Enter command: ")
        if command.lower() in ["exit", "quit"]:
            print("Exiting session.")
            break
        channel.send(command + '\n')

        # Receive and print the output
        while True:
            if channel.recv_ready():
                output = channel.recv(4096).decode('utf-8')
                print(output, end='')
                break

    # Close the session
    channel.close()
    ssh.close()

except Exception as e:
    print(f"An error occurred: {e}")
