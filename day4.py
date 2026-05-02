#reversing a string
s = "python"
i = len(s) - 1
rev = ""

while i >= 0:
    rev += s[i]
    i -= 1
print("Reversed:", rev)
# how to find a certain character in a string
# Ask the user for a string
text = input("Enter your string: ")

# Ask the user for the character to search
char = input("Enter the character to find: ")

# Start index at 0
j = 0

# Flag to track if character was found
found = False

# Loop through the entire string
while j < len(text):
    if text[j] == char:                     # check if current character matches
        print(f"Found '{char}' at position {j}")
        found = True                        # mark as found
        # no break here → keeps searching
        # if we add break then only finds the chracter for the first time and breaks, does not keep checking for the chracter. 
    j += 1                                  # move to next index

# If loop finishes without finding the character
if not found:
    print(f"Character '{char}' not found in the string.")

