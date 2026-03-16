class WaterException(Exception):
    pass


def water_plants(plant_list) -> None:
    try:
        for plant in plant_list:
            if plant in ("None", ""):
                raise WaterException("Error: Cannot water None - "
                                     "invalid plant!")
            print(f"Watering {plant}")
    except WaterException as e:
        print(e)
    finally:
        print("🔒 Closing watering system (cleanup)")


def test_watering_system() -> None:
        print("\033[0;34m💧Testing normal watering...💧\033[0m")
        print("🔓 Opening watering system")
        good_plants = ["tomato 🍅", "lettuce 🥬", "carrots 🥕"]
        water_plants(good_plants)
        print("\033[0;34mWatering completed successfully! ✅\033[0m\n")

        print(" \033[0;31m\nTesting with error...\033[0m💥")
        print("🔓 Opening watering system")
        bad_plants = ["tomato 🍅", "None", "carrots 🥕"]
        water_plants(bad_plants)
        print("\nCleanup always happens, even with errors!\n")


if __name__ == "__main__":
    print("\033[1;32m\n=== Garden Watering System ===\n\033[0m")
    test_watering_system()

# finally block to clean up whether an error happens or not
#
# write a function water_plants(plant_list):
#     open a watering system (just print)
#     go through each plant in the list
#     water each plant (just print)
#     always close the watering system (finally block)
#     handle errors if a plant name is invalid
#
# create a function test_watering_system()
#     normal watering with a good plant list
#     watering with a bad plant list (causes an error)
#     use try / except / finally structure
