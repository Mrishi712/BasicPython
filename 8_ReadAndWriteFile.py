# open a file
fileCreated = open("sampleTextFile.txt")

# # read all the lines
# print(fileCreated.read())
#
# # read specific amount of characters
# print(fileCreated.read(2))

# read one line at a time
# print(fileCreated.readline())
# print(fileCreated.readline())
#
# # read specific amount of characters
# print(fileCreated.read(2))

# currentLine = fileCreated.readline()
#
# while currentLine != "":
#     print(currentLine)
#     currentLine = fileCreated.readline()

for line in fileCreated.readlines():
    print(line)

# close the file
fileCreated.close()
