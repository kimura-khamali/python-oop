# Inheritance

class Vehicle:
    def __init__(self,make,color):
        self.make = make
        self.color = color

    def accelerate(self):
        print("Accelaration start")    

    def hoot(self):
        print("Hoot Hoot") 


class Bus(Vehicle):
    def __init__(self,make,color,progress):   
        super().__init__(make, color)
        self.progress = progress

    def start_descending(self):
        print("The bus is descending")  


class Lorry(Vehicle):
    def __init__(self, make, color,max_load):
        super().__init__(make, color)
        self.max_load = max_load

    def unload(self):
        print("unloading")  


""">>> from vehicle import Bus,Lorry
>>> b=Bus(make="Toyota",color="Red",progress="70")
>>> l=Lorry(make="Lorzo",color="White",max_load="100")
>>> b.accelerate()
Accelaration start
>>> b.start_descending()
The bus is descending
>>> l.hoot()
Hoot Hoot
>>> l.unload()
unloading
>>> l.accelerate()
Accelaration start
>>> l.start_descending()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Lorry' object has no attribute 'start_descending'
"""


# Polymorphism

class Animal:
    def move(self):
        pass
    def make_sound(self):
        pass

class Bird(Animal):
    def move(self):
        print("Flying")
   
    def make_sound(self):
        print("chirp") 


class cat(Animal):
    def move(self):
        print("Running")

    def make_sound(self):
        print("Meow")   


class Fish(Animal):
    def move(self):
        print("Swimming")

    def make_sound(self):
        print("Stidulation")        



"""
>>> from vehicle import Bird,cat,Fish
>>> p= Fish()
>>> p.move()
Swimming
>>> b= Bird()
>>> b.move()
Flying
>>> c= cat()
>>> c.move()
Running
>>> b.make_sound()
chirp
>>> p.make_sound()
Stidulation
>>> p.make_sound()
Stidulation
>>> c.make_sound()
Meow
>>> 
"""        


# Encapsulation

class Account:
    def __init__(self,number,pin):
        self.number = number
        self.__pin = pin 
        self.__balance = 0


    def check_balance(self,pin):
         if pin == self.__pin:
             return self.__balance
         else:
             return "Wrong pin"

""">>> from vehicle import Account
>>> a = Account(number=2334543,pin=3452)
>>> a.check_balance(pin=3467)
'Wrong pin'
>>> a.check_balance(pin=3452)
0
>>> """


