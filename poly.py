# polymorphism

# inheritance s a mechanism that allows you to create
#a new class (subclass or derived class) that inherits
# properties and behaviors (atrributes and methods)
# from an existing class (superclass ir base class)

from os import name


class Animal ():
    #attributes
    def __init__(self, name):
        self.name = name
        #method
        def speak(self):
            pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says bark"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow"

dog= Dog("Nala")
cat= Cat("Whiskers")

print(dog.speak())
print(cat.speak())


                