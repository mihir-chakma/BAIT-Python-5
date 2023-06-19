# BAIT - Problem 5 with Solution in Python

1. Create a class called Dog containing two fields, name and age declared as non-public variables.

2. Define two setters and two getters with appropriate arguments to set name, age and get name, age respectively. Also, create a function called **```showDetails()```** to display the name and age of dogs.

3. Create two sub-classes of the Dog super class called Bulldog, and Basenji to create objects only.

4. Create objects of the two sub-classes Bulldog and Basenji respectively and call the **```showDetails()```** function with appropriate arguments to obtain the following output.

## Solution

```python
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
        print(f"The {self.getName()} dog is {self.getAge()} years old")
        # print(f"The {self.__name} dog is {self.__age} years old")
        

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


```


```
Output:

 The Rocky dog is 5 years old
 The Bruno dog is 7 years old
```

