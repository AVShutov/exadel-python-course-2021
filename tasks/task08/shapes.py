from typing import NamedTuple
import abc
import math


class Point2D(NamedTuple):
    """
    A point in 2-dimensional space.
    Implemented as NamedTuple (so it is immutable), but simple class can be used instead.
    """
    x: float
    y: float

    def __str__(self):
        return f"({self.x}, {self.y})"


class Shape2D(abc.ABC):
    """
    An abstract shape in 2-dimensional space. Examples of 2D shapes are rectangle, circle, etc.
    """

    @property
    @abc.abstractmethod
    def area(self) -> float:
        """Area of the shape."""
        raise NotImplementedError

    @abc.abstractmethod
    def __contains__(self, point: Point2D) -> bool:
        """Check if the point is inside the shape.
        Support semantics like `if point in shape`"""
        raise NotImplementedError

    @abc.abstractmethod
    def __str__(self) -> str:
        """Get string representation of the shape."""
        raise NotImplementedError


class Rectangle(Shape2D):
    def __init__(self, bottom_left: Point2D, width: float, length: float):
        self.bottom_left = bottom_left
        self.width = width
        self.length = length

    def area(self) -> float:
       return self.width * self.length

    def __contains__(self, point: Point2D) -> bool:
        if ((self.bottom_left.x <= point.x <= self.bottom_left.x + self.length) and (self.bottom_left.y - self.width <= point.y <= self.bottom_left.y)):
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"Rectangle: Bottom left: {self.bottom_left}, Width: {self.width}, Length: {self.length}"


class Square(Rectangle):
    def __init__(self, bottom_left: Point2D, width: float):
        super().__init__(bottom_left, width, width)


class Circle(Shape2D):
    def __init__(self, center: Point2D, radius: float):
        self.center = center
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def __contains__(self, point: Point2D) -> bool:
        return (point.x - self.center.x)**2 + (point.y - self.center.y)**2 <= self.radius**2

    def __str__(self) -> str:
        return f"Circle: Center: {self.center.x},{self.center.y}, Radius: {self.radius}"
