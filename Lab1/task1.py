import sys

operators = ['+', '-', '*', '/']

if len(sys.argv) == 4 and sys.argv[1].isdigit() and sys.argv[2] in operators and sys.argv[3].isdigit():
    """Checks whether command line has 4 arguments."""

    try:
        print(eval(sys.argv[1] + sys.argv[2] + sys.argv[3]))
        """Prints calculated string."""
    except ZeroDivisionError:
        print("Division on zero!")

else:
    print("Wrong input!")
    """Printed, if command line has wrong number of arguments."""
