name = "Rishikesh Muraleedharan age is 23"
place = "Kerala"

print("First index : ", name[0])
print("Length: ", len(name))
print("First 5 characters: ", name[0:5])
name = name + " ,   I am from Kerala"
print("After concat with place: ", name)

# substring present or not
if place in name:
    print("True")
else:
    print("False")

# split based on coma
splittedText = name.split(",")
print("First Index:",splittedText[0])
print("Second Index:",splittedText[1])

# trim  -- strip
print("Second Index :",splittedText[1].strip())
# if only trimming from start --- lstrip
# if only trimming from end --- rstrip

print("Length: ", len(name))

