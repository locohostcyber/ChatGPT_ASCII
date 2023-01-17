import sys
import pyfiglet

# Check if any command-line argument is provided
if len(sys.argv) < 2:
    print("Please provide a string as command-line argument.")
    sys.exit()

# Get the input string from the command-line argument
input_string = sys.argv[1]

# Generate the ASCII art
ascii_art = pyfiglet.figlet_format(input_string)

# Print the ASCII art
print(ascii_art)
