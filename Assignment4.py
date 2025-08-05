# Assignment 4:
# Files, Exceptions and Errors in Python

# Task 1 Read a file and Handle Errors.
def readFile():
    vFileName = 'sample.txt'
    try:
        vFile = open(vFileName, 'r')
        vRead_file = vFile.read()
        print(vRead_file)
        vFile.close
    except FileNotFoundError:
        print(f"The file {vFileName} is not found")
        
readFile()

# method 1, Task 2 Write and Append data 

def writeAppendFile():
    vFileName = 'output.txt'
    vFileOperation = input("Which operation you want in file w/a : ")
    try:
        if vFileOperation == 'w':
            vFile = open(vFileName, 'w')
            vWrite_file = vFile.write("Hello, Python\n")
            print(vWrite_file)
            vFile.close
            
            # Reading the file 
            vFile = open(vFileName, 'r')
            vRead_file = vFile.read()
            print(vRead_file)
            vFile.close()
        elif vFileOperation == 'a':
            vFile = open(vFileName, 'a')
            vAppend_file = vFile.write("Learning File Handling in Python")
            print(vAppend_file)
            vFile.close 
            
            # Reading the file 
            vFile = open(vFileName, 'r')
            vRead_file = vFile.read()
            print(vRead_file)
            vFile.close()
        else:
            print("Please enter valid mode")
            
            
    except FileNotFoundError:
        print(f"The file {vFileName} is not found")
        
writeAppendFile()

# method 2, Task 2 Write and Append data
def writeAppendFile():
    vFileName = 'output.txt'
    vFileOperation = input("Which operation do you want in file? (w/a): ")
    
    try:
        if vFileOperation == 'w':
            with open(vFileName, 'w') as vFile:
                vWrite_file = vFile.write("Hello, Python\n")
                print(f"Characters written: {vWrite_file}")

            # Reading the file 
            with open(vFileName, 'r') as vFile:
                vRead_file = vFile.read()
                print("File content after write:\n", vRead_file)

        elif vFileOperation == 'a':
            with open(vFileName, 'a') as vFile:
                vAppend_file = vFile.write("Learning File Handling in Python\n")
                print(f"Characters appended: {vAppend_file}")

            # Reading the file 
            with open(vFileName, 'r') as vFile:
                vRead_file = vFile.read()
                print("File content after append:\n", vRead_file)

        else:
            print("Please enter a valid mode: 'w' for write or 'a' for append.")
            
    except FileNotFoundError:
        print(f"The file {vFileName} is not found")

writeAppendFile()








