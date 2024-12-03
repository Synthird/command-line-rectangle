width_string: str = ""


def display_error() -> None:
    print("!!! Cannot print a rectangle! !!!")
    print("Probably because you entered:")
    print("a) Decimals")
    print("b) Letters")
    print("c) Symbols")
    print("d) Spaces between numbers")
    print("e) A zero")
    raise SystemExit


def ask_question(prompt: str) -> int:
    print(f"--- What is the {prompt} of the rectangle? ---")
    try:
        number: int = int(input(f"{prompt.capitalize()}: "))

        if number > 0:
            return number
        else:
            raise ValueError
    except:
        display_error()


width: int = ask_question("width")
height: int = ask_question("height")

for _ in range(width):
    width_string = f"{width_string}."

for _ in range(height):
    print(width_string)
