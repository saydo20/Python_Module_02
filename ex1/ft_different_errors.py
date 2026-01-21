def garden_operations(error: object, value: any) -> None:
    if error is ValueError:
        value = int(value)
    elif error is ZeroDivisionError:
        value /= 0
    elif error is FileNotFoundError:
        open(value, "r")
    elif error is KeyError:
        d = {"plant": "Rose", "age": 45}
        print(d[value])
    else:
        value += "abc"
        colors = ["red", "green", "blue"]
        colors[value]


def test_error_types() -> None:
    print("\nTesting ValueError...")
    try:
        garden_operations(ValueError, "abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations(ZeroDivisionError, 1337)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print("\nTesting FileNotFoundError...")
    try:
        try:
            garden_operations(FileNotFoundError, "missing.txt")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'")
        print("\nTesting KeyError...")
    except Exception as Error:
        print(f"caught {Error}")
    try:
        garden_operations(KeyError, 9)
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
    print("\nTesting multiple errors together...")
    try:
        garden_operations(None, 100)
    except Exception:
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


test_error_types()
