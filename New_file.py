
#Read a file
file = open("Assignment.xlsm", "r")
content = file.read()
print(content)

#Modified the file 
file = open("Assignment.xlsm", "+r")
modified_version = content.upper()

#Read modified version of file
data = open("modified_content.xlsm", "+w")
data.write(modified_version) 
modified_version = content.upper()
print(modified_version) 


#Handling error from file not existing
try:
    with open("my_file.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File Not Found, Please check the filename.")    



