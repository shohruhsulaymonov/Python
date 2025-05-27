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
class Shape:
    pass

                    
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return round(pow(self.radius, 2)*3.14, 2)

    def get_perimeter(self):
        return round(2*3.14*self.radius, 2)

class Square(Shape):
    def __init__(self, size):
        self.size = size

    def get_area(self):
        return self.size**2

    def get_perimeter(self):
        return self.size*4

    def get_diagonal(self):
        return self.size*pow(2,0.5)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.sides = f'{a = }, {b = }, {c = }'

    def get_area(self, height, base):
        return height*base * 0.5

    def get_perimeter(self):
        return self.a + self.b + self.c

cyrcle = Circle(3.14)
print(cyrcle.get_perimeter())

sqware = Square(10)
print(sqware.get_diagonal())

threeangle = Triangle(4, 5, 7)
print(threeangle.get_area(6, 10))
print(threeangle.get_perimeter())
print(threeangle.sides)
#5
#6
#7
#8
class Cart:
    items = dict()
    def __init__(self):
        pass

    def add_item(self, product: str, price: float):
        if product in self.items:
            print(f'You already have {product} in your cart!')
        self.items[product] = price
    
    def remove_item(self, product):
        if product in self.items:
            self.items.pop(product)
        else:
            print('You do not have this product in your cart!')

    def my_items(self):
        if self.items:
            print('Items in your cart:')
            n = 1
            for item in self.items.keys():
                print(f'{n}. ' + item)
                n += 1
        else:
            print("You don't have anytihing in your cart, yet")

    def total_price(self):
        return sum(self.items.values())
    
    def clear_cart(self):
        return self.items.clear()
#9
#10
#11
