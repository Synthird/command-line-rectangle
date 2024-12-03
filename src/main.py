width_string: str = ""


def ask_measurement(prompt: str) -> int:
    print(f"--- What is the {prompt} of the rectangle? ---")
    try:
        number: int = int(input(f"{prompt.capitalize()}: "))

        if number > 0:
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
        print("e) Only a zero")
        print("f) You exited the program")
        raise SystemExit


for _ in range(ask_measurement("width")):
    width_string = f"{width_string}."

for _ in range(ask_measurement("height")):
    print(width_string)
