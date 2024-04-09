# A class is a blueporint for creating an object

# class Classname:
#       Class attributes and methods

class Person:
    # contructor or intializer
    # atrributes of class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        # method to increase the personsn  age
        def birthday(self):
            self.age = self.age + 1
            print('Happy Birthday, you are now', self.age, 'years old')

            