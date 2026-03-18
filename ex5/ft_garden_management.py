class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(PlantError):
    pass


class GardenManager:
    def add_plant(self, plant: str) -> None:
        if plant in (None, ""):
            raise PlantError("\033[0;31mError adding plant: Plant name "
                             "cannot be empty!\033[0m")
        print(f"Added {plant} successfully ✅")
# Add a plant to the garden. Raise PlantError if the name is empty.

    def validate_plants(self, plants: dict) -> dict:
        valid_plants = {}
        for plant, data in plants.items():
            try:
                self.add_plant(plant)
                valid_plants[plant] = data
            except PlantError as e:
                print(e)
        return valid_plants
# Check all plants in the dictionary and return only valid ones

    def check_plant_health(
              self, plant: str, humidity: int, min_humidity: int,
              temperature: int, temp_min: int, temp_max: int) -> None:

        if humidity < min_humidity:
            healthy = "\033[0;31mnot enough humidity\033[0m"
        else:
            healthy = "\033[0;32mgood humidity\033[0m"

        if temperature >= temp_min and temperature <= temp_max:
            temp_status = "\033[0;32mperfect temperature 🌈\033[0m"
        elif temperature < temp_min:
            temp_status = "\033[0;31mtemperature too cold ❄️ \033[0m"
        else:
            temp_status = "\033[0;31mtemperature too hot 🔥\033[0m"

        if (
            humidity < min_humidity
            or temperature < temp_min
            or temperature > temp_max
        ):
            raise GardenError(f"{plant}: {healthy} -> {humidity}% "
                              f"({min_humidity}%) and {temp_status} ->"
                              f" {temperature}°C ({temp_min}°C - "
                              f"{temp_max}°C)")
        else:
            print(f"{plant}: \033[0;32mhealthy ✅ \033[0m-> {humidity}% "
                  f"({min_humidity}%), {temperature}°C ({temp_min}°C -"
                  f" {temp_max})°C")
# Check the plant's humidity and temperature, raise GardenError if outside
# safe range.

    def watering_plants(self, plants: dict) -> dict:
        new_valid_plants = {}
        try:
            for plant, data in plants.items():
                if data["humidity"] < data["min_humidity"]:
                    print(f"Watering {plant} -\033[0;32m success \033[0m💧")
                    data["humidity"] += 30
                else:
                    print(f"{plant} doest not need water")
                new_valid_plants[plant] = data
        finally:
            print("🔒Closing watering system (cleanup)")
        return new_valid_plants
# Water the plants that need it and return updated humidity levels.
#  Use finally for cleanup.


def test_garden_management() -> None:
    manager = GardenManager()
    plants = {
        "ananas 🍍":
        {"humidity": 20, "min_humidity": 85, "temp": 50, "temp_min": 20,
         "temp_max": 30},
        "coconut 🥥":
        {"humidity": 40, "min_humidity": 50, "temp": 20, "temp_min": 15,
         "temp_max": 32},
        "":
        {"humidity": 80, "min_humidity": 42, "temp": 40, "temp_min": 5,
         "temp_max": 40},
        "banana 🍌":
        {"humidity": 70, "min_humidity": 60, "temp": 10, "temp_min": 18,
         "temp_max": 24},
    }

    print("\033[1;32mAdding plants to garden...\033[0m")
    valid_plants = manager.validate_plants(plants)

    print("\033[1;37m\nchecking healthy before watering...\033[0m")
    for plant, data in valid_plants.items():
        try:
            manager.check_plant_health(
                plant,
                data["humidity"],
                data["min_humidity"],
                data["temp"],
                data["temp_min"],
                data["temp_max"]
            )
        except GardenError as e:
            print(e)

    print("\n💦\033[1;34m Watering plants...\033[0m 💦")
    print("🔓 Opening watering system")

    new_valid_plants = manager.watering_plants(valid_plants)

    print("\033[1;37m\nchecking healthy after watering...\033[0m")
    for plant, data in new_valid_plants.items():
        try:
            manager.check_plant_health(
                plant,
                data["humidity"],
                data["min_humidity"],
                data["temp"],
                data["temp_min"],
                data["temp_max"]
            )
        except GardenError as e:
            print(e)

    print("\n\033[1;37mTesting error recovery...\033[0m")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
# Main test function: add plants, check health, water, check again,
# simulate error recovery.


if __name__ == "__main__":
    print("\033[1;36m\n🌴 === Exotic Garden Management System === 🌴\n\033[0m")
    test_garden_management()
    print("\033[1;36m\n🌴🦋 === Exotic Garden management system test "
          "complete  === 🦋🌴\n\033[0m")
