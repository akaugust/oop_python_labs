class Rectangle:
    """
    Class that has attributes length and width, provides methods
    that calculate the perimeter and the area of the rectangle
    """

    def __init__(self, length=1.0, width=1.0):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        """Length getter"""
        return self.__length

    @length.setter
    def length(self, leng):
        """Length setter"""
        if not isinstance(leng, float):
            raise TypeError("Wrong type of length!")
        if leng <= 0.0 or leng > 20.0:
            raise ValueError("Wrong value of length")
        self.__length = leng

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, wid):
        """Width setter"""
        if not isinstance(wid, float):
            raise TypeError("Wrong type of width!")
        if wid <= 0.0 or wid > 20.0:
            raise ValueError("Wrong value of width!")
        self.__width = wid

    def rectangle_area(self):
        """Returns area of rectangle"""
        return self.__width * self.__length

    def rectangle_perimeter(self):
        """Returns perimeter of rectangle"""
        return 2 * (self.__length + self.__width)

    def __str__(self):
        return f"Length - {self.__length}, width - {self.__width}\n" \
               f"Area: {self.rectangle_area()}, perimeter - {self.rectangle_perimeter()}\n"


if __name__ == "__main__":

    first = Rectangle()
    first.length = 1.25
    print(first.rectangle_area())
    print(first.rectangle_perimeter())
    print(first)
