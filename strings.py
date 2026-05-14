#a string is a sequence of characters.
#strings are immutable, meaning they cannot be changed after they are created.
#strings can be created using single quotes, double quotes, or triple quotes.
#single quotes
string1 = 'Hello, World!'
#double quotes
string2 = "Hello, World!" 
#triple quotes
string3 = '''Hello, World!'''
print(string1)
print(string2)
print(string3)

# Concatenation of strings
a = "hello"          # define first string
b = "world"          # define second string
print(a + " " + b)   # + joins strings, " " adds a space → hello world

# String formatting using f-strings
name = "lalitha"       # variable storing a name
age = 19            # variable storing an age
# f-string lets you insert variables directly inside {}
print(f"My name is {name} and I am {age} years old.")
# Output → My name is lalitha and I am 19 years old.

# String methods
s = "hello, world!"  # define a string

print(s.upper())     # converts all letters to uppercase → HELLO, WORLD!
print(s.lower())     # converts all letters to lowercase → hello, world!
print(s.title())     # capitalizes each word → Hello, World!

# split() breaks string into list using separator (here ", ")
print(s.split(", ")) # → ['hello', 'world!']

# replace() substitutes one substring with another
print(s.replace("world", "Python"))  # → hello, Python!
s = "Hello World 123"

# 1. isalpha() → checks if all characters are letters
print(s.isalpha())   # False (because of space and numbers)

# 2. isdigit() → checks if all characters are digits
print("123".isdigit())   # True

# 3. isalnum() → checks if all characters are letters or digits
print("Hello123".isalnum())   # True

# 4. isspace() → checks if string contains only whitespace
print("   ".isspace())   # True

# 5. capitalize() → makes first character uppercase
print("python".capitalize())   # Python

# 6. swapcase() → swaps uppercase ↔ lowercase
print("PyThOn".swapcase())   # pYtHoN

# 7. startswith() → checks if string begins with substring
print(s.startswith("Hello"))   # True

# 8. endswith() → checks if string ends with substring
print(s.endswith("123"))   # True

# 9. index() → returns position of substring (error if not found)
print(s.index("World"))   # 6

# 10. rfind() → finds last occurrence of substring
print("banana".rfind("a"))   # 5
