'''
try:
    pass
except expression as identifier:
    pass
else:
    pass
'''
try:
    fh = open("myfile.txt", "wb")
    fh.write("File operation is success!")
except BaseException as exception:
    print("Error while working with file! ", exception)
else:
    fh.close()
    print("File operation is success!")