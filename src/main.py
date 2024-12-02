width_string: str = ""


def ask_question(prompt: str):
    print(f"--- What is the {prompt} of the rectangle? ---")
    try:
        return int(input(f"{prompt.capitalize()}: "))
    except:
        print("Cannot print a rectangle!")
        print("Probably because you entered:")
        print("a) Decimals\nb) Letters\nc) Symbols\nd) Spaces between numbers")
        raise SystemExit


width: int = ask_question("width")
height: int = ask_question("height")

for _ in range(width):
    width_string = f"{width_string}."

for _ in range(height):
    print(width_string)
