import sys
import operator

operators = {
    'add': operator.add,
    'sub': operator.sub,
    'mul': operator.mul,
    'truediv': operator.truediv
}
"""Dictionary for operators."""

if len(sys.argv) == 4 and sys.argv[1] in operators and sys.argv[2].isdigit() and sys.argv[3].isdigit():
    """Checks whether command line has 4 arguments."""

    try:
        print(operators[sys.argv[1]](int(sys.argv[2]), int(sys.argv[3])))
        """Prints calculated input."""
    except ZeroDivisionError:
        print("Division on zero!")

else:
    print("Wrong input!")
    """Printed, if command line has wrong number of arguments."""
