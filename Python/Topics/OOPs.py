#-------------------------------------------------------OOPs in Python-------------------------------------------------------

#--> Basic Class and Objects

#Self -> Is act as this keyword, it is used to setup the telephone line between my_car and Car
#__int__ -> is used for arguments, also know as constructor

class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
my_car=Car("Toyota","Corlloa")
print(my_car.brand)

#--> Class Method(adding new func) and Self

class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car=Car("Toyota","Corlloa")
print(my_car.brand)
print(my_car.full_name())

#--> Inheritance

class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model) #Super is used t get the already declare barnd and models
        self.battery_size = battery_size
my_tesla = ElectricCar("tesla","Model S","85kmWh")
print(my_tesla.brand)

#--> Encapsulation

class Car:
    def __init__(self,brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"    

    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model) #Super is used t get the already declare barnd and models
        self.battery_size = battery_size

my_car = Car("Honda","City")
print(my_car.__brand)

#'__VariableName' menas that it made a priveate, now you can only acces it with class but not able to acces it with the objects.
# Now we only have to acces it with get_brand method to acces the brand name

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