class WaterException(Exception):
    pass


def water_plants(plant_list) -> None:
    print("🔓 Opening watering system")
    try:
        for plant in plant_list:
            try:
                test_watering_system(plant)
            except WaterException as e:
                print(e)
    finally:
        print("🔒 Closing watering system (cleanup)")


def test_watering_system(plant: str) -> None:
   if plant
   print("💧 \033[0;34mTesting normal watering\033[0m 💧")
        # print(f"Watering {plant}")
    
    
    print(" \033[0;31mTesting with error...\033[0m💥\n")
   raise WaterException ("\033[031m Cleanup always happens, even with "
                                 "errors!\033[0m \n")



if __name__ == "__main__":
    print("\033[1;32m\n=== Garden Watering System ===\n\033[0m")
    plant_list = ["tomato 🍅", "lettuce 🥬", "carrots 🥕"]
    water_plants(plant_list)
    AttributeError("Cleanup always happens, even with errors!")
    print("\033[092m\nWatering completed successfully!\033[0m ✅\n")

# block finally pour nettoyer qune erreur se produise ou pas
# ecrire une fonction water_plants(plant_list):
#     ouvre un system darosage (just print)
#     passe en revu chaque plante de la liste
#     arrose chaque plant(JUST PRINT)
#     ferme toujours le system darrosage (FINALLY) block
#      gere les erreur si le nom dune plante est invalide
#
# creer une fonction test_watering_system()
#   arrosage normal avec la bonne list de plant
#   arrosage avec une mauvaise liste de plant (a cause dune erreur)
#   utilise try / except/ finally structure