def water_plants(plant_list) -> None:
    print("Opening watering system")
    """TypeError when the plant is None"""
    try:
        for plant in plant_list:
            if plant is None:
                raise TypeError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except TypeError as Error:
        """catch this error and print custom massage"""
        print(f"Error: {Error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """test the function with all the cases"""
    try:
        print("=== Garden Watering System ===")
        print("\nTesting normal watering...")
        plants = ["tomato", "lettuce", "carrots"]
        water_plants(plants)
        print("Watering completed successfully!")
        plants = ["tomato", None, "carrots",]
        print("\nTesting with error...")
        water_plants(plants)
        print("\nCleanup always happens, even with errors!")
    except Exception:
        print("\ninvalid!\n")


test_watering_system()
