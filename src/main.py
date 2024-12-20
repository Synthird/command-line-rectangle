width_string: str = ""


def exit_with_possible_reasons() -> None:
	print("!!! Cannot print dots! !!!")
	print("Probably because you entered:")
	print("a) Decimals")
	print("b) Letters")
	print("c) Symbols")
	print("d) A negative number")
	print("e) You exited the program")
	raise SystemExit


def ask_length_of(length: str) -> int:
	number: int = 0

	print(f"--- What is the {length} of the rectangle? ---")

	try:
		number = int(input(f"{length.capitalize()}: ").replace(" ", ""))
	except:
		exit_with_possible_reasons()

	if number > -1:
		return number
	else:
		exit_with_possible_reasons()


width: int = ask_length_of("width")
height: int = ask_length_of("height")

if height > 0:
	for _ in range(width):
		width_string = f"{width_string}."

if width > 0:
	for _ in range(height):
		print(width_string)
