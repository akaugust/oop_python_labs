import sys

if len(sys.argv) == 2:
    """Checks whether command line has any arguments except script name."""

    user_input = sys.argv[1]
    formula_flag = True
    operators = ['+', '-']
    result, previous_element, current_element = None, None, None
    """Variables used for check."""

    for current_element in user_input:
        if not(current_element.isdigit() or (current_element in operators and previous_element.isdigit())):
            formula_flag = False
            break
        previous_element = current_element
    """Checks whether user`s input is a correct formula."""

    if formula_flag and current_element not in operators:
        result = eval(user_input)
        print("result =", (formula_flag, result))
    else:
        print("result = (False, None)")
    """Calculates the result if user`s input is a correct entry and prints the result."""

else:
    print("result = (False, None)")
    """Printed, if command line doesn't have any arguments except script name."""
