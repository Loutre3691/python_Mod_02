def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if plant_name in ("None", ""):
        raise ValueError("Testing empty plant name...❓💥\n\033[0;31mError: "
                         "Plant name cannot be empty!\033[0m\n")

    elif water_level < 1 or water_level > 10:
        raise ValueError(f"Testing bad water level for {plant_name}... 💧💥"
                         f"\n\033[0;31mError:"
                         f" Water level 15 is too high (max 10)\033[0m\n")

    elif sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(f"Testing bad sunlight hours for {plant_name}... "
                         f"☀️ 💥\n\033[0;31mError: "
                         f"Sunlight hours 0 is too low (min 2)\033[0m\n")

#   check plant name is not empty
#   check water level (1–10)
#   check sunlight hours (2–12)
#   raise ValueError if invalid
#   return success message if valid


def test_plant_check() -> None:
    plants = {
        "tomato 🍅": {"water": 5, "sunlight": 6},
        "": {"water": 5, "sunlight": 14},
        "carots 🥕": {"water": 15, "sunlight": 0},
        "potatoes 🥔": {"water": 1, "sunlight": 15},
    }
    for plant in plants:
        try:
            check_plant_health(
                plant,
                plants[plant]["water"],
                plants[plant]["sunlight"]
            )
            print(f"Testing good values... ✅\nPlant {plant} is healthy!\n")
        except ValueError as e:
            print(e)

#   test valid values
#   test invalid name
#   test invalid water
#   test invalid sunlight
#   catch and handle errors


if __name__ == "__main__":
    print("\033[1;32m\n=== Garden Plant Health Checker ===\n\033[0m")
    test_plant_check()
    print("\033[1;32m\n=== All error raising tests completed! ===\n\033[0m")
