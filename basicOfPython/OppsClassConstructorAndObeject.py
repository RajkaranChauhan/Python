# classes are user defined blueprint or prototype
# This is very similar to class in java


class Calculator():
    num = 100  # class variable

    # default Constructor
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
        print("default constructor")

    def method1(self):
        print("I am in method1 and num is {}".format(Calculator.num))  # as it is a class variable it should be called with class name

    def addition(self):
        return self.num1+self.num2


# creating object of calss
obj=Calculator(2,3)
obj.method1()
print(obj.addition())

obj2=Calculator(5,6)
obj2.method1()
print(obj2.addition())