def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        """
        raise the ValueError and pass a custom massage depend on the value
        """
        if plant_name == "":
            raise ValueError("Plant name cannot be empty!")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level}"
                             " is too high (max 10)")
        elif water_level < 1:
            raise ValueError(f"Water level {water_level}"
                             " is too low (min 1)")
        elif sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             " is too low (min 2)")
        elif sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             " is too high (max 12)")
        else:
            """Returns a success message if everything is okay"""
            return f"Plant '{plant_name}' is healthy!"
    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks():
    """test the function with all the cases"""
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    print(check_plant_health("tomato", 2, 6))
    print("\nTesting empty plant name...")
    check_plant_health("", 4, 6)
    print("\nTesting bad water level...")
    check_plant_health("Carrot", 15, 8)
    print("\nTesting bad sunlight hours...")
    check_plant_health("Rose", 8, 0)
    print("\nAll error raising tests completed!")


test_plant_checks()
