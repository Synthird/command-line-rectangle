width_string: str = ""


def ask_length_of(length: str) -> int:
    print(f"--- What is the {length} of the rectangle? ---")
    try:
        number: int = int(input(f"{length.capitalize()}: ").replace(" ", ""))

        if number > -1:
            return number
        else:
            raise ValueError
    except:
        print(f"!!! Cannot print a rectangle due to the {length}! !!!")
        print("Probably because you entered:")
        print("a) Decimals")
        print("b) Letters")
        print("c) Symbols")
        print("d) A negative number")
        print("e) You exited the program")
        raise SystemExit


width: int = ask_length_of("width")
height: int = ask_length_of("height")

if height > 0:
    for _ in range(width):
        width_string = f"{width_string}."

if width > 0:
    for _ in range(height):
        print(width_string)
