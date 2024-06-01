from Parent import Calculator2


class childClass(Calculator2):
    num2 = 50

    def __init__(self):
        Calculator2.__init__(self)
        print("In default constructor of childClass")

    def getChildFunction(self):
        print("in child function")
        print(self.num2)
        print(self.parentFunction())


childObject = childClass()
childObject.getChildFunction()
