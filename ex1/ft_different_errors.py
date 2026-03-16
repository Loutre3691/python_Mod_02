def garden_operations(error_type: str) -> None:
    if error_type == "value":
        int("abc")

    elif error_type == "zero":
        10 / 0

    elif error_type == "file":
        open("missing.txt")

    elif error_type == "key":
        plants = {"plant": 5}
        plants["missing_plant"]
# Write a function `garden_operations()` that demonstrates common
# Python errors:
# • ValueError: when invalid data is given (for example "abc" instead
# of a number)
# • ZeroDivisionError: when dividing by zero
# • FileNotFoundError: when trying to open a file that does not exist
# • KeyError: when trying to access a key that is not in a dictionary


def test_error_types() -> None:
    print("\033[1;31mTesting ValueError...\033[0m")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("\033[1;31mTesting ZeroDivisionError...\033[0m")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("\033[1;31mTesting FileNotFoundError...\033[0m")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("\033[1;31mTesting KeyError...\033[0m")
    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")

    print("\033[1;31mTesting multiple errors together...\033[0m")
    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
# • Show each error type
# • Catch each error and explain what happened
# • Show that the program continues after each error
# • Show how to catch multiple errors with one except block


if __name__ == "__main__":
    print("\033[1;32m=== Garden Error Types Demo ===\n\033[0m")
    test_error_types()
    print("\033[1;32m\nAll error types tested successfully!\033[0m")
