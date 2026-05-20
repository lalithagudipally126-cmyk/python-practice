#Definition
#A set is an unordered collection of unique items.
#You cannot have duplicates inside a set.
#Sets are mutable → you can add or remove elements.
#note
#👉 So the rule is:
#No indexing (like lists) because sets are unordered.
#set syntax
#my_set = {item1, item2, item3, ...}
#Example
# Creating a set
my_set = {1, 2, 3, 4}

# Mixed data types
mixed = {"apple", 10, 3.14, True}

print(my_set)
print(mixed)

# Duplicates are removed automatically
dup = {1, 2, 2, 3, 3, 4}
print(dup)  # Output: {1, 2, 3, 4}

#adding items to a set
my_set.add(5)  # Adds 5 to the set
print(my_set)  # Output: {1, 2, 3, 4, 5}
my_set.update([6, 7])  # Adds multiple items
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

#removing items from a set
my_set.remove(5)  # Removes 5 (error if not found)
print(my_set)  # Output: {1, 2, 3, 4, 6, 7}
my_set.discard(10)  # Safe remove (no error if not found)
print(my_set)  # Output: {1, 2, 3, 4, 6, 7}
popped_item = my_set.pop()  # Removes a random item
print(popped_item)
print(my_set)
my_set.clear()  # Removes all items
print(my_set)  # Output: set()

#looping through set
nums = {1, 2, 3, 4, 5}
for num in nums:
    print(num)

#length of set
print(len(nums))  # Output: 5

#min and max
print(min(nums))  # Output: 1
print(max(nums))  # Output: 5

#sum of set
print(sum(nums))  # Output: 15


# Question:
# Create a set of 5 colors.
# 1. Print the set.
# 2. Add "black" to the set.
# 3. Remove "green".
# 4. Print the updated set.

#set of 5 colours
c = {"red","yellow","green","violet","blue"}
print(c)
#Add a new color "black"
c.add("black")
print(c)
#Remove "green"
c.remove("green")
print(c)


# Start with this set:
colors = {"red", "yellow", "green", "purple", "black"}
# 1. Remove "yellow" using remove()
# 2. Remove "black" using discard()
# 3. Print the updated set
colors.remove("yellow")
print(colors)
colors.discard("black")
print(colors)


# Start with this set of animals:
animals = {"dog", "cat", "rabbit", "parrot"}
# 1. Add "elephant" to the set.
# 2. Add "tiger" to the set.
# 3. Replace "parrot" with "lion".
animals.add("elephant")
animals.add("tiger")
animals.remove("parrot")
animals.add("lion")
print(animals)


# Start with this set of fruits:
fruits = {"apple", "banana", "cherry", "mango"}
# 1. Loop through the set and print each fruit.
# 2. Print "I like ___" for each fruit.
# 3. Print the length of the set at the end.
for i in fruits:
    print(i)
for j in fruits:
    print("I like", j)
print(len(fruits))


# Start with this set of numbers:
numbers = {5, 10, 15, 20, 25}
doubled = set()
# 1. Loop through the set and print each number doubled.
# 2. Store all doubled numbers in a new set called doubled.
# 3. Print the new set.
for k in numbers:
    t = k*2
    print(t," ",end="")
    doubled.add(t)
print(doubled)


#union, intersection, difference, symmetric_difference
a = {1, 2, 3}
b = {3, 4, 5}

print("union:", a.union(b))                # {1, 2, 3, 4, 5}
print("intersection:", a.intersection(b))  # {3}
print("difference a-b:", a.difference(b))  # {1, 2}
print("difference b-a:", b.difference(a))  # {4, 5}
print("symmetric difference:", a.symmetric_difference(b)) # {1, 2, 4, 5}


# Start with this set:
letters = {"a", "b", "c", "d", "b", "e"}
# 1. Count how many times "b" appears (convert to list).
letters_list = list(letters)
print("b appears:", letters_list.count("b"))
# 2. Check membership
print("c in letters?", "c" in letters)
print("z in letters?", "z" in letters)


# Start with this set:
nums = {42, 7, 19, 3, 25}
# 1. Print sorted list of nums (ascending).
print(sorted(nums))
# 2. Add another number.
nums.add(50)
# 3. Print sorted list of nums (descending).
print(sorted(nums, reverse=True))
