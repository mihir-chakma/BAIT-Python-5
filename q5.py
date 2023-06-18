# Q5.py

class Dog:
    __name = None
    __age = 0
    
    def setName(self, name):
        self.__name = name
    def setAge(self, age):
        self.__age = age
        
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
        
    def showDetails(self):
        print(f"The {self.getName()} dog is {self.getAge()} years old.")
        # print(f"The {self.__name} dog is {self.__age} years old.")
        

class Bulldog(Dog):
    pass
class Basenji(Dog):
    pass


objbd = Bulldog()
objbs = Basenji()

objbd.setName("Rocky")
objbd.setAge(5)

objbs.setName("Bruno")
objbs.setAge(7)


objbd.showDetails()
objbs.showDetails()
