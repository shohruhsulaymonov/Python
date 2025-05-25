#1
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return round(pow(self.radius, 2)*pi, 2)
    def perimeter(self):
        return round(2*pi*self.radius, 2)
small_circle = Circle(5)
medium_circle = Circle(10)
large_circle = Circle(50)
print('The area of the cirle is:',  small_circle.area())
print('The perimeter of the cirle is:',  small_circle.perimeter())

print('The area of the cirle is:',  medium_circle.area())
print('The perimeter of the cirle is:',  medium_circle.perimeter())

print('The area of the cirle is:',  large_circle.area())
print('The perimeter of the cirle is:',  large_circle.perimeter())
#2
from datetime import date, datetime

class Person:

    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def get_age(self):
        today = date.today()
        dob = datetime.strptime(self.date_of_birth,"%Y-%m-%d").date()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        
        return age


client = Person('Nice', 'Uzbekistan', '2007-05-30')
print(client.get_age())
#3
class Calculator:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        try:
            result = self.a / self.b
            return result
        except ZeroDivisionError:
            print("Divizor CAN'T be zero")

nums = Calculator(5, 0)
print(nums.div())
#4
