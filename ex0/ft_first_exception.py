def check_temperature(temp_str: int) -> None:    
    if temp_str > 40:
        raise print(f"\033[0;31mError\n\033[0m: {temp_str}°C is too hot for plants (max 40°C")
    elif temp_str < 0:
        raise print(f"\033[0;31mError\n\033[0m: {temp_str}°C is too cold for plqnts (min 0°C)")
    else:
        print(f"\033[1;36mTemperature {temp_str} is perfect for plant!\033[0m")

def test_temperature_input(temp_str: str) -> None:
    print(f"Testing temperature: {temp_str}")
    try:
       temp = int(temp_str)
    except:
        print(f"\033[0;31mError\033[0m: '{temp_str}' is not a valid number")
        return
    try:
        check_temperature(temp_str)
    except:
        print("\033[1;31mERROR\n\033[0m")
        return

# def test_temperature_input() -> None:
if __name__ == "__main__":

    print("\033[1;32m=== Garden Temperature checker ===\n\033[0m")
    test = ["25", "abc", "100", "-50"]
    for t in test:
        test_temperature_input(t)
    print("\033[4;32mAll tests completed - program didn't crash!\033[0m")
