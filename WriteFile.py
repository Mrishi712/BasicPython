# with open('sampleTextFile.txt','r') as fileCreated: ---> if in read mode
# with open('sampleTextFile.txt','w') as fileCreated: ---> if in write mode

with open('sampleTextFile.txt', 'r') as reader:
    currentContent = reader.readlines()
    print(currentContent)
    with open('sampleTextFile.txt', 'w') as writer:
        for line in reversed(currentContent):
            writer.write(line)
