from math import sqrt
import turtle as t
from gc import get_referrers

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def center(self, other):
        if isinstance(other, Point):
            return Point((self.x+other.x)/2,(self.y+other.y)/2)
        else:
            return NotImplemented

    def distance(self, other):
        if isinstance(other, Point):
            return self.createVector(other).distance
        else:
            return NotImplemented

    def translate(self, other):
        if isinstance(other, Vector):
            return Point(self.x+other.x,self.y+other.y)
        else:
            raise TypeError

    def createVector(self, other):
        if isinstance(other, Point):
            return Vector(self.x-other.x,self.y-other.y)
        else:
            return NotImplemented
    
    def draw(self):
        t.goto(self.x, self.y)
        t.dot()
        return

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = sqrt(self.x**2+self.y**2)

    def __str__(self):
        return "({})\n({})".format(self.x, self.y)

    def toLine(self, other):
        if isinstance(other, Point):
            endPoint = other.translate(self)
            return Line(other, endPoint)
        else:
            return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x+other.x, self.y+other.y)
        else:
            return NotImplemented
    
    def __iadd__(self, other):
        return self+other
    
    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __sub__(self, other):
        return self+(-other)
    
    def __isub__(self, other):
        return self-other

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x*other, self.y*other)
        else:
            return NotImplemented

    def __imul__(self, other):
        return self*other

    def __rmul__(self, other):
        return self*other

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self*(1/other)
        else:
            raise TypeError

class Line:
    def __init__(self, startPoint, endPoint):
        self.start = startPoint
        self.end = endPoint
        self.distance = self.toVector().distance

    def toVector(self):
        return Vector(self.start.x-self.end.x,self.start.y-self.end.y)
    
    def draw(self):
        t.goto(self.start.x, self.start.y)
        t.pd()
        t.goto(self.end.x, self.end.y)
        t.pu()
    
class Polygon:
    def __init__(self, points):
        if len(points) >= 3:
            self.sides = []
            for i in range(len(points)-1):
                self.sides.append(Line(points[i], points[i+1]))
            self.sides.append(Line(points[len(points)-1],points[0]))
        else:
            raise TypeError
    
    def draw(self):
        xSum, ySum = 0,0
        for i in self.sides:
            xSum += i.start.x
            ySum += i.start.y
        xSum /= len(self.sides)
        ySum /= len(self.sides)
        points = {}
        for i in self.sides:
            points[0] = Point(i.start.x + xSum, i.start.y + ySum)
        
        

        """ t.goto(self.sides[0].start.x, self.sides[0].start.y)
        t.pd()
        for i in self.sides:
            t.goto(i.end.x, i.end.y)
        t.pu() """

        
        

A = Point(0,100)
B = Point(-200, -300)
C = Point(400,-100)
D = Point(600, 0)

AC = Line(A,C)
ABC = Polygon([A,B,C,D])

t.speed(0)
t.pu()

ABC.draw
