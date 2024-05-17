# class Student:
#       name="Ann"
#       school="Akirachix"
#       code= 55
#       age=30


"""In oreder to create an instance, process of creating a class is known as instanceiatiation
instance variable allows to wite data data that are collected  and are passed to the constructor of a class"""


class Student:
      school="Akirachix"
      def __init__(self,first_name,last_name,code,age,country):
          self.first_name = first_name
          self.last_name = last_name
          self.code = code
          self.age = age
          self.country = country

      def greet_student(self):
          greeting = f"{self.first_name},is age {self.age} and this is her code {self.code}"  
          return greeting  
      
# agnes = Student(first_name ="agnes", last_name = "Wangesha", age =21, country="Kenya", code = 79)
# faith = Student(first_name ="Faith", last_name = "Mutava", age =21, country="Kenya", code = 27)
# glory = Student(first_name ="Glory", last_name = "Wachira", age =21, country="Kenya", code = 2)



"""class method are defined as funtion insidet the body of a class
The first argument of a class arg is always self"""          
      