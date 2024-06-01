# class which comes as pat of oops
class Calculator:
    num = 100  # class variable

    # default constructor
    def __init__(self,num1,num2):
        self.firstNum=num1
        self.secondNum=num2
        print("In default constructor")

    def getData(self):
        print("In getdata method")

    def addMe(self):
        return self.firstNum + self.secondNum

    def minusMe(self):
        if self.firstNum > self.secondNum:
            return  self.firstNum - self.secondNum
        else:
            return  self.secondNum - self.firstNum

    def numMeMethod1(self):
        return self.firstNum + self.secondNum + self.num

    def numMeMethod2(self):
        return self.firstNum + self.secondNum + Calculator.num


firstObject = Calculator(4,5)  # creating new object
firstObject.getData()
print(firstObject.num)
print(firstObject.addMe())
print(firstObject.numMeMethod1())
print(firstObject.numMeMethod2())

secondObject = Calculator(5,4)  # creating new object
print(secondObject.minusMe())

# constructor is a method which is automatically called when an object is created for the class
