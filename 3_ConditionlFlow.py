# if and nested if
a = 10

if a > 10:
    print(a, " is greater than 10")
    print("Block 1")
else:
    if a < 10:
        print(a, " is lesser than 10")
        print("Block 2")
    else:
        print(a, " is equal to 10")
        print("Block 3")

print("Outside if")

# for loop
myList = [1, 6, 3, 5, 4, 8, 9]
sumMe = 0
for i in myList:
    print(i)
    sumMe = sumMe + i

print("Sum ", sumMe)

for j in range(5, 10):
    print(j)

# print a pattern
newList = []
for k in range(5, 10):
    newList.append(k)
    print(newList)

newList = []
for k in range(10, 5, -1):
    newList.append(k)
    print(newList)

newList = [10, 9, 8, 7, 6]
for k in reversed(newList):
    print(newList)
    newList.pop()

# while loop
let = 10
while let >= 1:
    if let == 5:
        print("Hello", let)
    else:
        if let == 7:
            let = let - 1
            continue
        else:
            if let == 3:
                break
            else:
                print("Hi", let)
    let = let - 1

