import os
cwd = os.getcwd()    # current working directory
print(cwd)

os.mkdir("Folder1")  # Create folder
os.mkdir("Folder1/Folder2") # Create sub folder
os.makedirs("sub1/sub2/sub3")  # Create sub folders


os.rmdir("Folder1/Folder2")  # Removes folder
os.mkdir("vamsi")
os.rename("vamsi","kamal")

os.listdir('.')