class Shapes():
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides
    def area(self):
        print("I am a: " + self.name + "\n" + "I have " + self.sides + "sides")
object_shape = Shapes("shape", "so many sides")
object_shape.area()

class Circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        result = 3.14 * self.radius * self.radius
        return result
object_ball = Circle(5)
print(object_ball.area())


class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height=height
    def area(self):
        result = 12 * self.base * self.height
        return result
object_pizza = Triangle(4,10)
print(object_pizza.area())

