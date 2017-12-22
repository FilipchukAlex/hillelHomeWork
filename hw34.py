class Shape:


    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Shape):


    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius


    def is_point_inside_circle(self, Point):
        print((Point.x - self.x)**2 + (Point.y - self.y)**2 <= self.radius**2)





class Point(Shape):


    def __init__(self, x, y):
        super().__init__(x, y)


point1 = Point(1, 5)
circle1 = Circle(2, 4, 1)
circle1.is_point_inside_circle(point1)
