'''

File IO
1. Open the file in specific mode
2. It will return file handle
3. Use the file handle to do file operations
   (read, write, change, delete, chnage attribute)
4. Close the file handle

'''

fh = open("01_helloworld.py", "r")
print(fh.name)
print(fh.mode)
print(fh.closed)
fh.close()
print(fh.closed)
print("===================================")
#No need to close the file when using with block
with open ("01_helloworld.py", "r") as fh:
    print(fh.name)
    print(fh.mode)
    print(fh.closed)
print(fh.closed)   

#write to a file(in write mode)
with open("python.txt", "w") as fh:
    fh.write("Hello from Python!\n")
    fh.write("In a new Line")

#append in a file(in append mode)
with open("python.txt", "a") as fh:
    fh.write("\nOmkar\n")
    fh.write("Dnyanmote")

#read data from file and write it to console
#to read single line use readline
#and for reading multiple lines use readlines
with open("python.txt", "r") as fh:
    content = fh.readlines()
    for line in content:
        print(line)
print("====================================")
#read data from file in chunk size
with open("python.txt", "r") as fh:
    content1 = fh.read(10)
    content2 = fh.read(10)
    content3 = fh.read(10)
    print(content1)
    print(content2)
    print(content3)
    print(fh.tell())

#seek(how much do I want to seek, from where)
#possible values of from where
#0 -> pointer shift will start from beggining of file!
#1 -> pointer shift will start from curerent offset
#2 -> EOF will be current offset
    fh.seek(10, 0)
    print(fh.tell())
    print(fh.read(7))
    print(fh.tell())
    #print(fh.seek(11, 1))
    #print(fh.read(7))

#copy data from one file to another
with open("python.txt", "r") as fh:
    content = fh.readlines()
    tempfh = open("python1.txt", "w")
    for line in content:
        tempfh.write(line)
    tempfh.close()

#copy data from one image file to another image file
with open("image.png", "rb") as fh:
    content = fh.readlines()
    tempfh = open("copy.png", "wb")
    for line in content:
        tempfh.write(line)
    tempfh.close()