#while loop for strings
#prints the string
text = "lalitha"          # our string
i = 0                     # i starts as the index (position in the string)
#i goes from index 0 to index 6 which is the length of the string.
# loop runs as long as i is less than the length of the string
while i < len(text):
    #print(text[i])
    #prints in vertical format without end=
    # print the character at position i
    print(text[i], end="")   # end="" prevents new line
    #prints in horizontal
    i += 1   # move to the next index (important to avoid infinite loop)
text1 = input("\nEnter your string: ")
j = 0
while j < len(text1):
    print(text1[j], end="")
    j += 1   # loop ends naturally when j == len(text1)

# second task starts after the first loop finishes
word = input("\nEnter another string: ")
k = 0
vowels = "aeiou"
count = 0

while k < len(word):
    if word[k] in vowels:
        count += 1
    k += 1

print("Number of vowels:", count)
