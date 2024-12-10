width_string: str = ""


def ask_length_of(prompt: str) -> int:
    print(f"--- What is the {prompt} of the rectangle? ---")
    try:
        number: int = int(input(f"{prompt.capitalize()}: "))

        if number > -1:
            return number
        else:
            raise ValueError
    except:
        print("!!! Cannot print a rectangle! !!!")
        print("Probably because you entered:")
        print("a) Decimals")
        print("b) Letters")
        print("c) Symbols")
        print("d) Spaces between numbers")
        print("e) A negative number")
        print("f) You exited the program")
        raise SystemExit


width: int = ask_length_of("width")
height: int = ask_length_of("height")

if height > 0:
    for _ in range(width):
        width_string = f"{width_string}."

if width > 0:
    for _ in range(height):
        print(width_string)
