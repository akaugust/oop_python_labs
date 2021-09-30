class Rectangle:
    """Has attributes length and width, provides methods that calculate the perimeter and the area of the rectangle"""

    def __init__(self, length=1, width=1):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        """Length getter"""
        return self.__length

    @length.setter
    def length(self, len):
        """Length setter"""
        if not isinstance(len, float) or len <= 0.0 or len > 20.0:
            raise ValueError("Wrong length!")
        self.__length = len

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, wid):
        """Width setter"""
        if not isinstance(wid, float) or wid <= 0.0 or wid > 20.0:
            raise ValueError("Wrong width!")
        self.__width = wid

    def rectangle_area(self):
        """Returns area of rectangle"""
        return self.__width * self.__length

    def rectangle_perimeter(self):
        """Returns perimeter of rectangle"""
        return 2 * (self.__length + self.__width)


if __name__ == "__main__":
    first = Rectangle()
    first.length = 5.75
    print(first.length)
    print(first.width)
    print(first.rectangle_area())
    print(first.rectangle_perimeter())
