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
      
      def year_of_birth(self):
        return f"{self.first_name}, you were born in {2024-self.age}"
      def full_name(self):
          return f"My first name is {self.full_name}"
      def initials(self):
          return f"{self.full_name} {self.last_name} {self.age} {self.code} {self.country}"
      def check_if_student_is_minor(self):
          return Student
      def enroll_student(self):
          return f"This is the new student you need to invite {self.first_name} {self.last_name}"
 
agnes = Student(first_name ="agnes", last_name = "Wangesha", age =21, country="Kenya", code = 79)
faith = Student(first_name ="Faith", last_name = "Mutava", age =21, country="Kenya", code = 27)
glory = Student(first_name ="Glory", last_name = "Wachira", age =21, country="Kenya", code = 2)




"""Add these methods to class students.
Method to show the full name
Method to show the initials
Methods to check if a student is a minor
Method to enroll students in a class"""


""">>> from object import Student
>>> agnes = Student(first_name ="agnes", last_name = "Wangesha", age =21, country="Kenya", code = 79)
>>> agnes.greet_student()
'agnes,is age 21 and this is her code 79'
>>> faith = Student(first_name ="Faith", last_name = "Mutava", age =21, country="Kenya", code = 27)
>>> faith.greet_student()
'Faith,is age 21 and this is her code 27'
>>> glory = Student(first_name ="Glory", last_name = "Wachira", age =21, country="Kenya", code = 2)
>>> glory.greet_student()
'Glory,is age 21 and this is her code 2'
>>> 

[13]+  Stopped                 python3
studen@student-ThinkPad-E14-Gen-4:~/pythonClass/oop$ python3
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from object import Student
>>> agnes = Student(first_name ="agnes", last_name = "Wangesha", age =21, country="Kenya", code = 79)
>>> agnes.year_of_birth()
'agnes, you were born in 2003'
>>> faith = Student(first_name ="Faith", last_name = "Mutava", age =21, country="Kenya", code = 27)
>>> faith.year_of_birth()
'Faith, you were born in 2003'
>>> glory = Student(first_name ="Glory", last_name = "Wachira", age =21, country="Kenya", code = 2)
>>> glory.year_of_birth()
'Glory, you were born in 2003'
>>> """
     
      