#-------------------------------------------------------List Comprehension-------------------------------------------------------
# squares = [x**2 for x in range(10)]
# print("This is for List",squares)

#--------------------------------------------------------------------

#-------------------------------------------------------Generator Expressions-------------------------------------------------------
# squares_gen = (x**2 for x in range(10))
# print("This is for Generator Expressions")
# for num in squares_gen:
#     print(num)

#--------------------------------------------------------------------

#-------------------------------------------------------Iterators and Iteratabels-------------------------------------------------------

#Iterable: Any object thats can loop over eg: list, strings
#Iterator: Any object with __iter__() and __next__() methods

# nums = [7,5,6,3]

# it = iter(nums)
# print(it.__next__()) #--> It gives me the next value i.e 7
# print(it.__next__()) #--> It will give 5

#Creating Own Interator
#Like we are creating to print 10 valuse from 1 to 10

# class TopTen:
#     def __init__(self): #This is use to define your counter and where you want to start
#         self.num = 1
#     def __iter__(self): #It will give you the object of iterator
#         return self
#     def __next__(self):

#         if self.num <= 10:
#             val = self.num
#             self.num +=1

#             return val
#         else:
#             raise StopIteration
        
# values = TopTen()

# for i in values:
#     print(i)

#--------------------------------------------------------------------

#-------------------------------------------------------Decorators-------------------------------------------------------

#Decorators: Is basically you can change the behaviuor of the existing function at the compile time itself

# def div(a,b):
#     print (a/b)
# #But here let suppose we want that Demoninator should always greater than numenarator
# # We can do it by modifying the div(a,b) but what if you want to don't have access of that file or you dont want to chenage it
# #In that case we use Decorators

# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#             return func(a,b)
    
#     return inner
# div2 = smart_div(div)

# div2(2,4) #Traditionaly it should give 0.5 but now it with 2.0

#--------------------------------------------------------------------

#-------------------------------------------------------Context Manager-------------------------------------------------------

#Context Manager : It is a constructor that basically allow you to manage resource efficiently.
#It handles SETUP, CLEANUP actions automatically.

# There is two type -> 1. Built-in, 2. Custom

#Its practically use in Database Connection and FIle Handling

#----------------Built-In--------------------
#
# with sqllit3.connect("example.db") as connection:
#     make_conne = connection.db
#
#
# with open("hello.txt","w") as file:
#     file.write("Fuck you marco")

#----------------Custom Context Manager--------------------
#__enter__() -> Runs at the start ('with' block)
#__exit__() -> Runs at the end for cleanup

#--------------------------------------------------------------------

#-------------------------------------------------------OOPs in Python-------------------------------------------------------

#--> Basic Class and Objects

#Self -> Is act as this keyword, it is used to setup the telephone line between my_car and Car
#__int__ -> is used for arguments, also know as constructor
# class Car:
#     def __init__(self,brand, model):
#         self.brand = brand
#         self.model = model
# my_car=Car("Toyota","Corlloa")
# print(my_car.brand)

#--> Class Method(adding new func) and Self
# class Car:
#     def __init__(self,brand, model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"

# my_car=Car("Toyota","Corlloa")
# print(my_car.brand)
# print(my_car.full_name())

#--> Inheritance
# class Car:
#     def __init__(self,brand, model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand,model) #Super is used t get the already declare barnd and models
#         self.battery_size = battery_size
# my_tesla = ElectricCar("tesla","Model S","85kmWh")
# print(my_tesla.brand)

#--> Encapsulation
# class Car:
#     def __init__(self,brand, model):
#         self.__brand = brand
#         self.model = model

#     def get_brand(self):
#         return self.__brand + "!"    

#     def full_name(self):
#         return f"{self.__brand} {self.model}"

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand,model) #Super is used t get the already declare barnd and models
#         self.battery_size = battery_size

# my_car = Car("Honda","City")
# print(my_car.__brand)

##'__VariableName' menas that it made a priveate, now you can only acces it with class but not able to acces it with the objects.
## Now we only have to acces it with get_brand method to acces the brand name

#--> Polymorphism

class Car:
    def __init__(self,brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"    

    def full_name(self):
        return f"{self.__brand} {self.model}"
    def fuel_type(self):
        return "Petrol or Disel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model) #Super is used t get the already declare barnd and models
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"


my_car = Car("Honda","City")
my_eCar = ElectricCar("tesla","Motor M", "120kWh")
print(my_car.fuel_type())
print(my_eCar.fuel_type())
