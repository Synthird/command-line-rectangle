width_string: str = ""

width: int = int(input("What is the width of the rectangle:"))
height: int = int(input("What is the height of the rectangle:"))

for _ in range(width):
    width_string = width_string + "."

for _ in range(height):
    print(width_string)