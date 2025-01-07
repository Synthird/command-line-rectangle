width_string: str = ""


def exit_with_message(message: str) -> None:
	print(message)
	raise SystemExit


def ask_length_of(length: str) -> int:
	print(f"--- What is the {length} of the rectangle? ---")

	try:
		return int(input(f"{length.capitalize()}: ").replace(" ", ""))
	except ValueError:
		exit_with_message("Please enter a whole number without any decimals....")
	except KeyboardInterrupt:
		exit_with_message("\nYou exited the program!")


width: int = ask_length_of("width")
height: int = ask_length_of("height")

if height > 0:
	for _ in range(width):
		width_string = f"{width_string}."

if width > 0:
	for _ in range(height):
		print(width_string)
