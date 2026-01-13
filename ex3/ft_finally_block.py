def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                "Watering " + plant
            print(f"Watering {plant}")
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print("Watering completed successfully!")
    plants = ["tomato", None, "carrots",]
    print("\nTesting with error...")
    water_plants(plants)
    print("\nCleanup always happens, even with errors!")


test_watering_system()
