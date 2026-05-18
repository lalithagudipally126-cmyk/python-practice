#Definition
#A list is an ordered collection of items.
#You can store numbers, strings, or even other lists inside it.
#Lists are mutable → you can change, add, or remove elements.
#note
#👉 So the rule is:
#Positive indices count forward from 0.
#Negative indices count backward from -1.
#list syntax
#my_list = [item1, item2, item3, ...]
#Example
# Creating a list
my_list = [1, 2, 3, 4]

# Mixed data types
mixed = ["apple", 10, 3.14, True]

print(my_list)
print(mixed)

print("First item in my_list:", my_list[0])  # Output: 1 #positive index
print("Last item in mixed:", mixed[-1])  # Output: True #negative index

# List of emojis
emojis = ["😀", "😂", "😍", "😎", "😭", "😡", "😧", "😑", "😳", "😈"]

# Accessing from the front
print(emojis[0])   # 😀 first
print(emojis[1])   # 😂 second
print(emojis[2])   # 😍 third

# Accessing from the back
print(emojis[-1])  # 🔥 last
print(emojis[-2])  # 🎉 second last
print(emojis[-3])  # 🙏 third last

#adding items to a list
my_list.append(5)  # Adds 5 to the end of the list
print(my_list)  # Output: [1, 2, 3, 4, 5]
my_list.insert(2, 10)  # Inserts 10 at index 2
print(my_list)  # Output: [1, 2, 10, 3, 4, 5]
my_list.extend([6, 7])  # Adds multiple items to the end of the list
print(my_list)  # Output: [1, 2, 10, 3, 4, 5, 6, 7]

#removing items from a list
my_list.remove(10)  # Removes the first occurrence of 10
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7]
popped_item = my_list.pop(2)  # Removes and returns the item at index 2
print(popped_item)  # Output: 3
print(my_list)  # Output: [1, 2, 4, 5, 6, 7]
my_list.clear()  # Removes all items from the list
print(my_list)  # Output: []

#updating elements
flowers = ["rose", "tulip", "daisy"]
flowers[1] = "sunflower"  # Update the second item
print(flowers)  # Output: ['rose', 'sunflower', 'daisy']

#looping through list
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

#length of list
print(len(nums))  # Output: 5

#min and max
print(min(nums))  # Output: 1
print(max(nums))  # Output: 5

#sum of list
print(sum(nums))  # Output: 15


# Question:
# Create a list of 5 colors.
# 1. Print the first color (positive index).
# 2. Print the last color (negative index).
# 3. Change the third color to "purple".
# 4. Add a new color "black" at the end.
# 5. Print the updated list.

#list of 5 colours
c=['red','yellow','green','violet','blue']
print(c)
#Print the first color (positive index).
print(c[0])
# Print the last color (negative index).
print(c[-1])
#Change the third color to "purple".
c[2]='purple'
print(c)
#Add a new color "black" at the end.
c.append('black')
print(c)

# Start with this list:
colors = ["red", "yellow", "green", "purple", "black"]
# 1. Remove "yellow" using remove()
# 2. Remove the last item using pop()
# 3. Print the updated list
colors.remove("yellow")
print(colors)
colors.pop(-1)
print(colors)


# Start with this list of animals:
animals = ["dog", "cat", "rabbit", "parrot"]
# 1. Insert "elephant" at the beginning of the list.
# 2. Insert "tiger" at index 2.
# 3. Replace the last animal with "lion".
# 4. Print the updated list.
animals.insert(0,"elephant")
animals.insert(2,"tiger")
animals.pop(-1)
animals.append("lion")
print(animals)


# Start with this list of fruits:
fruits = ["apple", "banana", "cherry", "mango"]
# 1. Loop through the list and print each fruit.
# 2. Print "I like ___" for each fruit.
# 3. Print the length of the list at the end.
for i in fruits:
    print(i)
for j in fruits:
    print("i like",j)
print(len(fruits))

# Start with this list of numbers:
numbers = [5, 10, 15, 20, 25]
doubled=[]
# 1. Loop through the list and print each number doubled.
# 2. Store all doubled numbers in a new list called doubled.
# 3. Print the new list.
for k in numbers:
    t=k*2
    print(t," " ,end="")
    doubled.append(t)
print(doubled)


# index(value)
# Finds the position of the first occurrence of a value.
letters = ["a", "b", "c", "b"]
print(letters.index("b"))  # Output: 1

# count(value)
# Counts how many times a value appears in the list.
letters = ["a", "b", "a", "c", "a"]
print(letters.count("a"))  # Output: 3

# sort()
# Sorts the list in ascending order (numbers or strings).
number = [3, 1, 4, 2]

# Sort in ascending (default)
number.sort()
print(number)   # [1, 2, 3, 4]

# Sort in descending
number.sort(reverse=True)
print(number)   # [4, 3, 2, 1

# Start with this list:
letters = ["a", "b", "c", "d", "b", "e"]
# 1. Find the index of the first "b".
# 2. Find the index of "d".
# 3. Print both results.
print("index of b:",letters.index("b"), ", index of d:",letters.index("d"))
# 4. Count how many times "b" appears.
# 5. Count how many times "c" appears.
# 6. Print both counts.
print("b appears:",letters.count("b"),"times",
", c appears:",letters.count("c"),"times")

# Start with this list:
nums = [42, 7, 19, 3, 25]
# 1. Sort the list in ascending order.
nums.sort()
# 2. Print the sorted list.
print(nums)
# 3. Add another number.
nums.append(50)
# 4. Sort the list in descending order.
nums.sort(reverse=True)
# 5. Print the sorted list.
print(nums)
# 6. Reverse the list.
nums.reverse()
# 7. Print the reversed list.
print(nums)



