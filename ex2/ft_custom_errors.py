class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass
# create a class with Exception in first class and the other follow the first
#
# Exception
#    │
#    └── GardenError
#           │
#           ├── PlantError
#           └── WaterError


def error_garden(temperature: int, liter: int) -> None:
    if temperature > 40 and liter < 2:
        raise GardenError(
            "Caught a garden error: The tomato plant is wilting!\n"
            "Caught a garden error: Not enough water in the tank!\n"
        )
    elif temperature > 40:
        raise PlantError("Caught PlantError: The tomato plant is wilting!\n")

    elif liter < 2:
        raise WaterError("Caught WaterError: Not enough water in the tank!\n")
# fonction for three class conditions with raise


if __name__ == "__main__":
    print("\033[1;32m=== Custom Garden Errors Demo ===\n\033[0m")
    print("\033[0;32m🌱 Testing PlantError...\033[0m")
    try:
        error_garden(41, 5)
    except PlantError as e:
        print(e)

    print("\033[0;36m💧 Testing WaterError...\033[0m")
    try:
        error_garden(30, 1)
    except WaterError as e:
        print(e)

    print("\033[0;31m⚠️  Testing catching all garden errors...\033[0m")
    try:
        error_garden(41, 1)
    except GardenError as e:
        print(e)

    print("\033[1;32mAll custom error types work "
          "correctly!\033[0m")
