class parent:
    def display(self):
        print("This is a parent class")

class child1(parent):
    def display1(self):
        print("This is a child1 class")      


class child2(parent):
    def display2(self):
        print("This is a child2 class")


obj = child1()
obj = child2()
obj.display()
obj.display()




#hybrid inheritance

class A:
    def func(self):
        print("A")

class B(A):
    pass
class C(A):
    pass

class D(B,C):
    pass

obj = D()
obj.func()


#Method overiding

class Animal:
    def animal(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("bark")

class Lion(Animal):
    def sound(self):
        print("Roar")

L1=Lion()
L1.sound()

D1=Dog()
D1.sound()



#Polymorphism
class Animal:
    def animal(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("bark")

class Lion(Animal):
    def sound(self):
        print("Roar")

animals = [Dog(), Lion()]

for animal in animals:
    animal.sound()

#initilitation

class student:
    def __init__(self):
        self.__marks = 101

    def getMarks(self):
        return self.__marks
    
s = student()
print(s.getMarks())

#Abstractshion