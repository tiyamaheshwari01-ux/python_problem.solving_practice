import os

# Specify the directory path

###what is directory path 
# directory = folder it is in  
#path = location with in the computer where the file is stored
path = "/"
# here giving out \ as directory paths gives us the all the files preesent in c drive. 

# Get list of files and directories
contents = os.listdir(path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)