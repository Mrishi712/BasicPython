# datatype available

# numeric - int, float, complex
a = 9495937577
b = 10.123
c = 100 + 1j

print(type(a))
print(type(b))
print(type(c))

# string
d = 'test'
e = "TEST"
print(type(d))
print(type(e))

# list -- its mutable
# we can pass different data types in a list
f = [1, 'test', 'best', 1 + 3j, 3, "bob", "ava"]
print(type(f))
print(f)
print(f[0])
print(f[3])
print(f[-1])  # print last item
print(f[1:4])
print(f)
f.insert(2, 2)
f.insert(3, "Three")
print(f)
print(len(f))
f.append("End")
print(f)
f[0] = "Start"
print(f)
print(len(f))
del f[4]
print(f)
print(len(f))

# tuple -- is immutable
g = ('test', 4, "your name")
print(g)
print(g[1])

# dictionary -- key value pair
h = {"fName": "rishi", 1: "test", 2: "lname"}
print(h)
print(h["fName"])
print(h[2])

runtimeDictnory = {}
runtimeDictnory["first"] = "Hai"
runtimeDictnory[10] = "Hello"
print(runtimeDictnory)
