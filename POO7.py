#Crie uma hierarquia de classes representando formas geométricas. 
#Comece com uma classe base chamada"Forma" e, em seguida, crie classes derivadas como
#"Círculo"e"Retângulo"que herdem da classe base. Adicione métodos para calcular área e perímetro em cada classe derivada.

import math

class Shape:
    def __init__(self):
        self.area = 0
        
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def Calculate_area(self):
        self.area = math.pi * self.radius**2
    
    def Calculate_perimeter(self):
        return 2* math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self,length, width):
        super().__init__()
        self.length = length
        self.width = width

    def Calculate_area(self):
        self.area = self.length * self.width

    def Calculate_perimeter(self):
        return 2 * self.length * self.width
    
class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def Calculate_area(self):
        self.area = self.side ** 2

    def Calculate_perimeter(self):
        return 4 * self.side
    
class Triangle(Shape):
    def __init__(self, height, base):
        super().__init__()
        self.height = height
        self.base = base
    
    def Calculate_area(self):
        self.area = self.base * self.height / 2

    def Calculate_perimeter(self):
        return 2 * (self.base + self.height)
    
circle = Circle(radius=6)
circle.Calculate_area()
print(f"The area of Circle is: {circle.area:.2f}")
print(f"The perimeter of circle is: {circle.Calculate_perimeter():.2f}")

rectangle = Rectangle(length=6, width=4)
rectangle.Calculate_area()
print(f"The area of Rectangle is: {rectangle.area}")
print(f"The perimeter of Rectangle is {rectangle.Calculate_perimeter()}")
square = Square(side=4)
square.Calculate_area()
print(f"The area of Square is: {square.area}")
print(f"The perimeter of Square is: {square.Calculate_perimeter()}")

triangle = Triangle(base=5, height=10)
triangle.Calculate_area()
print(f"The area of Triangle is: {triangle.area}")
print(f"The perimeter of Triangle is: {triangle.Calculate_perimeter()}")
