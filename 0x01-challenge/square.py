#!/usr/bin/python3
"""
An Object representation of a Square class
"""


class Square:
    """
    A representation of square class
    """

    def __init__(self, *args, **kwargs):
        """
        initializes an instance of Square class
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Returns the perimeter of a class """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        returns the toString representation of the square class
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
