def check_temperature(temp_str: str) -> int:
    """Handle the exceptions using try and except"""
    try:
        temp = int(temp_str)
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None

    try:
        if temp > 40:
            raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!\n")
            return temp

    except Exception as Error:
        print(f"Error: {Error}\n")
        return None


def test_temperature_input() -> None:
    """Test the function check_temperature with all values"""
    print("=== Garden Temperature Checker ===\n")

    temperature = "25"
    print(f"Testing temperature: {temperature}")
    check_temperature(temperature)

    temperature = "abc"
    print(f"Testing temperature: {temperature}")
    check_temperature(temperature)

    temperature = "100"
    print(f"Testing temperature: {temperature}")
    check_temperature(temperature)

    temperature = "-50"
    print(f"Testing temperature: {temperature}")
    check_temperature(temperature)

    print("All tests completed - program didn't crash!")


test_temperature_input()
