"""create the custom errors using class"""


class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class GardenManager:
    """
    the GardenManager class has a methods that
    add_plant, water_plants and check_plant_health
    """
    def __init__(self):
        self.plants = []

    def add_plant(self, plant):
        """if the plant_name is empty the method raise a PlantError"""
        try:
            if plant == "":
                raise PlantError("adding plant: Plant name cannot be empty!")
            self.plants = self.plants + [plant]
            print(f"Added {plant} successfully")
        except PlantError as Error:
            print(f"Error {Error}")

    def water_plants(self):
        """if the plant_name is None the method raise a PlantError"""
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant is None:
                    raise WaterError("Cannot water None - invalid plant!")
                print(f"Watering {plant} - success")
        except WaterError as Error:
            print(f"Error {Error}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant, water, sun):
        """check the health of the plant by check the watring and sun hours"""
        try:
            if water > 10:
                raise ValueError(f"Water level {water}"
                                 " is too high (max 10)")
            elif water < 1:
                raise ValueError(f"Water level {water}"
                                 " is too low (min 1)")
            elif sun < 2:
                raise ValueError(f"Sunlight hours {sun}"
                                 " is too low (min 2)")
            elif sun > 12:
                raise ValueError(f"Sunlight hours {sun}"
                                 " is too high (max 12)")
            else:
                print(f"{plant}: healthy (water: {water}, sun: {sun})")
        except ValueError as e:
            print(f"Error checking {plant}: {e}")


def garden_recovery(water_in_chunk, wilting):
    """a function recovry if there is any problem"""
    try:
        if water_in_chunk < 50:
            water_in_chunk = 100
            raise GardenError("GardenError: Not enough water in tank")
        elif wilting > 12:
            wilting = 10
            raise WaterError("WaterError: The plant is wilting!")
    except Exception as Error:
        print(f"Caught {Error}")
    print("System recovered and continuing...")


def test_garden_management():
    """use the function test_garden_management() to test all the cases"""
    tomato = "tomato"
    tomato_watring = 5
    tomato_sun = 8
    lettuce = "lettuce"
    lettuce_watring = 15
    lettuce_sun = 8
    some = ""
    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    manager = GardenManager()
    manager.add_plant(tomato)
    manager.add_plant(lettuce)
    manager.add_plant(some)
    print("\nWatering plants...")
    manager.water_plants()
    print("\nChecking plant health...")
    manager.check_plant_health(tomato, tomato_watring, tomato_sun)
    manager.check_plant_health(lettuce, lettuce_watring, lettuce_sun)
    print("\nTesting error recovery...")
    garden_recovery(30, 8)
    print("\nGarden management system test complete!")


test_garden_management()
