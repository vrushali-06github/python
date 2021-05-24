#Abstraction*****HIDING INTERNAL THINGS(Data Hiding)
class Maths:
    def additionmeans(self,a,b):
        print("Addition means sum of two numbers:-eg. value 1 + value 2=answer")
        self.addition(a,b)
    def addition(self,a,b):
        print(a,"+",b,"=",a+b)
x=Maths()
x.additionmeans(2,3)

