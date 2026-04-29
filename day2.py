#REVISION OF DAY1
a= 10
print("a",a)
b =int(input("enter any number:"))
#int(input()) because otherwise input only returns string values
#we cannot add c=a+b if input() returns string because a is int
print("b =", b)
c=a+b
print("c",c)
print(f"a={a}, b={b}, c={c}")
#actual study 
#if, if-else, if-elif-else conditions
#must give 4 spaces after if, or will get error because of indention block
if b<=10:
   print("b is less than or equal to 10")
if c<20:
    print("c is less than 20")
else:
    print("c is greater than 20")
d=2*c
if d>20:
    print("d is greater than 20")
elif d<20:
 print("d is less than 20")
else:
    print("d is equal to 20")
# for loop
# ✅ Iterables (work in for loops):
# strings, lists, tuples, sets, dictionaries, range()

# ❌ Not Iterables (won't work directly):
# integers, floats, booleans, None

# For integers → use range(n) to make a sequence of numbers
# Example: for i in range(5): print(i)   # 0,1,2,3,4

# For floats → not iterable directly. Convert to range or list if needed.
# Example: for i in range(int(3.14)): print(i)   # 0,1,2

# For booleans → not iterable. Use them only in conditions (if True/False).
# Example: if True: print("yes")

# For None → not iterable. It's just a placeholder for "nothing".
# Example: if value is None: print("empty")
#for loop no.1
n=20 #0-19
m=2
for o in range(n):
    if o%m==0:
      print("n=",o)
# for loop no.2
i=int(input("enter a value below 20, it will print numbers until the given number from 0:"))
#in python input() only accepts one string 
for j in range(i):
   print("n =", j)
   