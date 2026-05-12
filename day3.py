#example 1
text = "lalitha"   # our string
i = 0              # index starts at 0
while i < len(text):          # loop runs until i reaches length of string, length of the string is 7, so the loop runs till i=0 to i(index)=6
    print(text[i], end="")    # print character at position i (horizontal because of end=)
    i += 1                    # move to next index, increases i by one each time, This moves to the next character in the string.
#Without this, the loop would get stuck at the same index (infinite loop).
#example2
text2 = input("\nenter your string:")
l=0
while l < len(text2):
    print(text2[l], end="")
    l +=1

# second task starts after the first loop finishes
word = input("\nEnter another string: ")
k = 0
vowels = "aeiou"
count = 0

while k < len(word):
    if word[k] in vowels:   # check if current character is a vowel
     count += 1          # if yes, add 1 to the counter
    k += 1
#so suppose word is like bat so it checks b with a then e then i then o then u no match so next letter in word meaning, like it goes to check the next letter because of k=+1, a , a matches with a count+1
print("word:", word)
print("Number of vowels:", count)
# 🔹 Definition:
# A while loop repeats code as long as a condition is True.

# 🔹 Syntax:
#while condition:
    # code block

# 🔹 Use:
# When you don’t know exactly how many times to run,
# but want to keep going until a condition changes.
