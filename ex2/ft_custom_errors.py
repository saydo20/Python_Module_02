"""create the classes GardenError, PlantError and WaterError"""


class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


"""use the classes to make our own errors"""


def test_custom_errors() -> None:
    try:
        print("=== Custom Garden Errors Demo ===")
        print("\nTesting PlantError...")
        """catch all the errors and make them print a custom masseges"""
        try:
            raise PlantError("The tomato plant is wilting!")
        except PlantError as e:
            print(f"Caught PlantError: {e}")

        print("\nTesting WaterError...")
        try:
            raise WaterError("Not enough water in the tank!")
        except WaterError as e:
            print(f"Caught WaterError: {e}")

        print("\nTesting catching all garden errors...")
        try:
            raise PlantError("The tomato plant is wilting!")
        except GardenError as e:
            print(f"Caught a garden error: {e}")

        try:
            raise WaterError("Not enough water in the tank!")
        except GardenError as e:
            print(f"Caught a garden error: {e}")

        print("\nAll custom error types work correctly!")
    except Exception as Error:
        print(f"invalid : {Error}")


test_custom_errors()
