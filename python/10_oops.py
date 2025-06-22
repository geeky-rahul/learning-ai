# Question 1: create a car class with attribute brand and model. Then create an instance of this class
# Question 2: Add a method that display full name of the car (brand and model)
# Question 4: Encapsulation-> Modify the Car class to encapsulate the model attribute, making it private, and provide a getter method for it
# Question 5: Polymorphism-> Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviours
# Question 6: Add a class variable to Car that keeps track of the number of cars created.
# Question 7: Add a static method to the Car class that returns a general description of a car
# Question 8: Use a property decorator in the Car class to make the brand attribute read-only

class Car:
    total_car = 0
    def __init__(self, brand, model): # function inside class is known as method
        self.__brand = brand # varible inside class is known as attribute
        self.__model = model
        Car.total_car += 1
     
    @property   
    def brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
        
       
my_car = Car("Toyota","Corolla")
# my_car.brand = "city" # it change the brand name to city
print(my_car.brand)
# print(my_car.__model) # not accessable
print(my_car.full_name())
print(Car.general_description())


# Question 3: Inheritance-> Create an ElectricCar class that inherits form the Car class and has an additional attribute battery_size
# Question 9: class inheritance and isinstance() Function-> Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"
    
my_new_car = ElectricCar("Tesla", "Model S", "85kWh")

print(isinstance(my_new_car, Car))
print(isinstance(my_new_car, ElectricCar))

print(my_new_car.full_name())

safari = Car("Tata", "Safari")
print(safari.fuel_type())
print(Car.total_car)


# Question 10: Multiple Inheritance-> Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance
class Battery:
    def battery_info(self):
        return "This is Battery"

class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricCar2(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar2("Tesla","Model F")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())