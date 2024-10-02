# Specify the file path and where file will be put in
file_path = "C:\\Users\\f3l1x\\OneDrive\\Desktop\\Automation\\filename.txt"

# Open the file in write mode and write content
with open(file_path, "w") as file:
    # Write some content to the file
    file.write("Hello, this is a test file.\n")
    file.write("This is my first time creating a file\n")
    file.write("This file was created using a Python script :)\n")
   

print("File created successfully at:", file_path,"\n")

#Read file and itterate through all lines in text to match word. 
with open(file_path, "r") as file:
        lines= file.readlines()
        for line in lines:
              #print(line)
            x=line.strip()
            if any (word in x for word in [ "test file"]):
                print("Authorized users only. Contact Admin")