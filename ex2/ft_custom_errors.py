class GardenError(Exception):
    pass

class PlantError(GardenError):
    def __init__(self, plant, watring):
        self.plant = plant
        self.watring = watring
        super().__init__(f"The {plant} plant is wilting!")

class WaterError(GardenError):
    def __init__(self):
        super().__init__(f"Not enough water in the tank!")
try:
    plant = "tomato"
    tomato_watring = 10
    if tomato_watring > 2:
        raise PlantError(plant, tomato_watring)
except PlantError as e:
    print(f"Caught PlantError: {e}")

try:
    water_in_tank = 90
    if water_in_tank < 100:
        raise WaterError()
except WaterError as e:
    print(f"Caught WaterError: {e}")
