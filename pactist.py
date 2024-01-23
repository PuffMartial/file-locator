import os
path = " C:\\Users\\kevin\\OneDrive\Desktop\\my  side prodject\\python\\test.txt"

if os.path.exists(path):
    print("that location exist")
if os.path.isfile(path):
    print("thats a file")
elif os.path.isdir(path):
    print("that is a diractory")
else:
    print("that location is not exist")