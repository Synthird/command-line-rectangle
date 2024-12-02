width_string: str = ""


def ask_question(question: str, prompt: str):
    print(f"--- {question}? ---")
    try:
        return int(input(f"{prompt}: "))
    except:
        print("Cannot print a rectangle!")
        print("Probably because you entered:")
        print("a) Decimals\nb) Letters\nc) Symbols\nd) Spaces between numbers")
        raise SystemExit


width: int = ask_question("What is the width of the rectangle", "Width")
height: int = ask_question("What is the height of the rectangle", "Height")

for _ in range(width):
    width_string = width_string + "."

for _ in range(height):
    print(width_string)
