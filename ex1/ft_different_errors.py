def garden_operations(value, error, dic):
    """check fo each error an try to catch it"""

    """try to cast the value into int"""
    if error == ValueError:
        try:
            a = int(value)
        except ValueError:
            print("Caught ValueError: invalid literal for int()\n")

        """
        try to devide normal number by the value to chack the ZeroDivisionErro
        """

    elif error == ZeroDivisionError:
        try:
            a = 2 / value
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero\n")
        """try to open the file and catch the FileNotFoundError"""
    elif error == FileNotFoundError:
        try:
            f = open(value, "r")
            f.close()
        except FileNotFoundError:
            print(f"Caught FileNotFoundError: No such file '{value}'\n")
        """try to access a value with a non exist key to catch the KeyError"""
    elif error == KeyError:
        try:
            """try to put a non exists value in a variable"""
            a = dic[value]
            a = a
        except KeyError:
            print(f"Caught KeyError: 'missing\\{value}'\n")
    else:
        print("Caught an error, but program continues!\n")


def test_error_types():
    """test all the errors """
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    garden_operations("abc", ValueError, None)
    print("Testing ZeroDivisionError...")
    garden_operations(0, ZeroDivisionError, None)
    print("Testing FileNotFoundError...")
    garden_operations("missing.txt", FileNotFoundError, None)
    print("Testing KeyError...")
    garden = {
        "name": "Rose",
        "age": 20
    }
    garden_operations("_plant", KeyError, garden)
    print("Testing multiple errors together...")
    garden_operations(None, None, None)
    print("All error types tested successfully!")


test_error_types()
