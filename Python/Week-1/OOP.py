#-------------------------------OOPS in Python------------------------------
#--> First is starts with PROCEDURAL Coding
#--> Then we get to know about Funtions concept to get more reusabiliyt and decrease the Redundancy 

#Class -> Objects

#----Class->It is a blueprint for creating an Objects
#creating the Class
# class Student:
#     name="karan Kumar"

#creating object (instances)
# s1 = Student()
# print(s1.name)

#----Constructor->It is basically a [__init__] funtion. This __init__ funtion invoked during the object creation
#               ->When we dont dclare any init funtion then the python automatically create and execute it 
#               ->Construtor always take the arguments or parameter which is known as self paramete
#               ->self means the new/ currently object we are creating, like 'khud ko'
#creating own init funtion
# class Student2:

#     #Default Consrtuctor
#     def __init__(self):
#         pass

#     # Parameterized Constructor
#     def __init__(self,fullname):
#         self.name = fullname
#         print("Adding new Student in Databse")

# s2 = Student2("Ritesh")
# print(s2.name)

#----Attribute->It can be nay data or any valuse or any varaiable like name, fullname etc
#             ->Two Types of Attributes i.e 1.)Class.atr 2.)obj.atr
#             ->Class.atr-> Common for all the objects. Owned by Class and commone for all the objects
#             ->Obj.at-> Also know as Instance Atrribute, Which is differnet and vary from object to object
#                     -> For this we used slef.name,fullname etc
#example
# class Student_data():
#     college = "Chandigarh Unverity"#Class atr
#     print("Univerisyt Name is :-",college)
#     def __init__(self,name):
#         self.name = name#Obj atrr
#         print("Name is :-",name)

# s1 = Student_data("Ritesh")
# print(s1.name,s1.college)
# s2 = Student_data("Sankalp")
# print(s2.name, s2.college)

#----Methods->Class had two things i.e data & methods
#           ->Data means Attributes
#           ->Methos means what you can doen with that
# class Student3:
#     university = "Chandigarh University"
#     def __init__(self, name):
#         self.name = name

#     def welcome(self):#We had ve to declare self, if we use it or not we have to declare it 
#         print("Welcome Students...",self.name)

# s1 = Student3("Ritesh")
# s1.welcome()

#----Static Method->These Method dont use SELF parameter 
#                 -> It works only in Class Level
#                 -> We used @staticmethod -> this is also known as decorator

class Student4:
    university = "Chandigarh University"
    def __init__(self, name):
        self.name = name
    @staticmethod
    def hello():
        print("Hello MF") 

    def welcome(self):#We had ve to declare self, if we use it or not we have to declare it 
        print("Welcome Students...",self.name)

s1 = Student4("RItesh")
s1.hello()