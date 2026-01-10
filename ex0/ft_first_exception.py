def check_temperature(temp_str):
    """handel the exceptions by using try and except"""
    try:
        """convert the temp_str into int to use it"""
        temp_str = int(temp_str)
        """handel if the value is : 0 <= value <= 40"""
        if temp_str > 40:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)\n")
            return None
        elif temp_str < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)\n")
            return None
        else:
            print(f"Temperature {temp_str}°C is perfect for plants!\n")
            return temp_str
    except Exception:
        """catch the valueError"""
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None


def test_temperature_input():
    """test the function chack_temperature with all the values"""
    print("=== Garden Temperature Checker ===\n")
    temperature = 25
    print(f"Testing temperature: {temperature}")
    check_temperature(temperature)

    temperature = "abc"
    print(f"Testing temperature: {temperature}")
    check_temperature(temperature)

    temperature = 100
    print(f"Testing temperature: {temperature}")
    check_temperature(temperature)

    temperature = -50
    print(f"Testing temperature: {temperature}")
    check_temperature(temperature)
    """print a messege that mean the program didn't crash"""
    print("All tests completed - program didn't crash!")


test_temperature_input()
