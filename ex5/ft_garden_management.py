"""create the custom errors using class"""


class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class GardenManager:
    """
    the GardenManager class has a methods that
    add_plant, water_plants and check_plant_health
    """
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant: str) -> None:
        """if the plant_name is empty the method raise a PlantError"""
        try:
            if plant == "":
                raise PlantError("adding plant: Plant name cannot be empty!")
            self.plants = self.plants + [plant]
            print(f"Added {plant} successfully")
        except PlantError as Error:
            print(f"Error {Error}")

    def water_plants(self) -> None:
        """if the plant_name is None the method raise a PlantError"""
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant is None:
                    raise WaterError("Cannot water None - invalid plant!")
                print(f"Watering {plant.name} - success")
        except WaterError as Error:
            print(f"Error {Error}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: str, water: int, sun: int) -> None:
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


def garden_recovery(water_in_chunk: int) -> None:
    """a function recovry if there is any problem"""
    try:
        if water_in_chunk < 50:
            water_in_chunk = 100
            raise GardenError("GardenError: Not enough water in tank")
    except Exception as Error:
        print(f"Caught {Error}")
    print("System recovered and continuing...")


class Plant:
    def __init__(self, name: str, watring: int, sun: int) -> None:
        self.name = name
        self.watring = watring
        self.sun = sun


def test_garden_management() -> None:
    try:
        """use the function test_garden_management() to test all the cases"""
        tomato = Plant("tomato", 5, 8)
        lettuce = Plant("lettuce", 15, 8)
        some = Plant("", 10, 8)
        print("=== Garden Management System ===")
        print("\nAdding plants to garden...")
        manager = GardenManager()
        manager.add_plant(tomato)
        manager.add_plant(lettuce)
        manager.add_plant(some)
        print("\nWatering plants...")
        manager.water_plants()
        print("\nChecking plant health...")
        manager.check_plant_health(tomato.name, tomato.watring, tomato.sun)
        manager.check_plant_health(lettuce.name, lettuce.watring, lettuce.sun)
        print("\nTesting error recovery...")
        garden_recovery(30)
        print("\nGarden management system test complete!")
    except Exception as Error:
        print(f"invalid : {Error}")


test_garden_management()
