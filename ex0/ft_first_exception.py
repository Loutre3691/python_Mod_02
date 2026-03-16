def check_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"\033[0;31mError\033[0m: '{temp_str}' is not a valid"
                         f" number\n")

    if temp > 40:
        raise ValueError(f"\033[0;31mError\033[0m: {temp}°C is too hot for"
                         f" plants (max 40°C)\n")
    elif temp < 0:
        raise ValueError(f"\033[0;31mError\033[0m: {temp}°C is too cold "
                         f"for plants (min 0°C)\n")
    return temp


def test_temperature_input() -> None:
    tests = ["25", "abc", "100", "-50"]

    for test in tests:
        print(f"Testing temperature: {test}")
        try:
            temp = check_temperature(test)
            print(f"Temperature {temp}°C is perfect for plants!\n")

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    print("\033[1;32m=== Garden Temperature checker ===\n\033[0m")
    test_temperature_input()
    print("\033[4;32mAll tests completed - program didn't crash!\033[0m")
