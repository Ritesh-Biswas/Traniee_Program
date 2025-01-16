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
class Student2:

    #Default Consrtuctor
    def __init__(self):
        pass

    # Parameterized Constructor
    def __init__(self,fullname):
        self.name = fullname
        print("Adding new Student in Databse")

s2 = Student2("Ritesh")
print(s2.name)
