filetest = open("test.txt", "w")
filetest.write("Test")
filetest.close()
files=open("test.txt", "r")
print(files.read())
files.close()
