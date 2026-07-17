book = {
"Title" : "Atomic Habits",
"Author": "James Clear",
"Price": 799
}
print(book["Title"])
book["page"]=320
book["Price"]=699
del book["Author"],
print(book)
x = {
    "name" : "a",
    "branch" : "b",
    "age": 0
}
x["college name"]="c"
x["age"] = x["age"] + 1
del x["branch"],
print(x["name"])
print(x["college name"])
print(x["age"])
print(x)
inventory = {
    "Apple": 20,
    "Banana": 15,
    "Orange": 10
}
print(inventory["Apple"])
inventory["Mango"] = 25
inventory["Banana"] =+ 15 #assigns positive value 10 to Banana
inventory["Banana"] += 10
# adds 10 to the value in Banana
del inventory["Orange"]
inventory["Strawberry"] = 11
inventory.popitem()
inventory.pop("Mango")
inventory['kiwi'] = 40
inventory.get("Apple")
print(inventory.items())
print(inventory.keys())
print(inventory.values())
if 'kiwi' in inventory.keys():
 print(inventory)
for key,value in inventory.items():
    if value <= 30:
        print(key, "the count is less than 30")
word = "banana"
frequency = {
    
}
for i in word:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)
marks = {
    "Math": 90,
    "Science": 85,
    "English": 78
}
print(marks["Science"])
marks["Social"] : 88
marks["English"] += 5
if marks["Math"] > 80:
    print("excellent in math!")
print(marks)
cart = {
    "Milk": 2,
    "Bread": 1,
    "Eggs": 12
}
cart.pop("Bread")
cart["Butter"] : 1
cart["Milk"] += 1
del cart["Eggs"]
print(cart.items())
cart.popitem()
print(cart)
products = {
    "Mouse": 700,
    "Keyboard": 1500,
    "Monitor": 12000,
    "USB": 300,
    "Headphones": 2500
}
for key,value in products.items():
    if value > 1000:
        print(key, value)
sentence = "python is fun python is powerful"
words = sentence.split()
print(words)
frequency1 ={
    
}
for i in words:
    if i in frequency1:
        frequency1[i] += 1
    else:
        frequency1[i] = 1
print(frequency1)
students = {
    "Aman": 82,
    "Priya": 95,
    "Rahul": 88,
    "Sneha": 91
}
students = {
    "Aman": 82,
    "Priya": 95,
    "Rahul": 88,
    "Sneha": 91
}
highest_marks = 0
topper = ""
for key,value in students.items():
    if value > highest_marks:
        highest_marks = value
        topper = key
print("topper is",topper, "with",highest_marks, "marks")
