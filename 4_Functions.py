# functions

def greetMe():
    print("Hello")


def greetMewithName(name):
    greetMe()
    print("Hello ", name)


def provideSum(a, b):
    return a + b


greetMe()
greetMewithName("Rishi")
print(provideSum(1 , 2))
print(provideSum(7 , 2))
