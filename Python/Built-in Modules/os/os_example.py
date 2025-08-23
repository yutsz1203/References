import os

# current directory
print(os.getcwd())

# change directory
os.chdir("/Users/yutsz/Desktop")
print(os.getcwd())

# list out directories
print(os.listdir())

# create directory
os.mkdir("Test_OS")

# create directories, including all sub directories
os.makedirs("Test/OS")

# remove directory (only empty directory)
os.rmdir("Test_OS")

# remove directoeis, including all sub directions
os.removedirs("Test/OS")

# rename file
# os.rename("text.txt", "demo.txt")

# print info of a file
print(os.stat("demo.txt"))

# traverse directory recursively
# for dirpath, dirname, filename in os.walk(os.getcwd()):
#     print(f"Path: {dirpath}, Directories: {dirname}, Files: {filename}")

# get environment variables
print(os.environ.get("HOME"))

# join paths without worrying about "/"s
file_path = os.path.join(os.environ.get("HOME"), "test.txt")
print(file_path)

# get basename (file name)
print(os.path.basename("/tmp/test.txt"))

# get directory name
print(os.path.dirname("/tmp/test.txt")) # return: /tmp
print(os.path.dirname(__file__)) # return: /Users/yutsz/Documents/References/Python/Built-in Modules/os

# split path and file 
path, filename = os.path.split("/tmp/test.txt")
print(path)
print(filename)

# check if path exists
print(os.path.exists("/tmp/test.txt"))

# check if a dir
print(os.path.isdir("/tmp/asdfsdf"))

# check if a file
print(os.path.isfile("/tmp/asdfsdf"))

# split path and extension
path, extension = os.path.splitext("/tmp/test.txt")
print(path)
print(extension)

# check what methods exist
print(dir(os.path))

