#print numbers 1-100
n=1
while n<101:
    print(n)
    n+=1
#print multiplication table of a number 
a=int(input("enter a number"))
m=1
while m<11:
    print(f"{a}*{m}=",a*m)
    m+=1
#sum of even numbers until 50
o=0
total=0
while o<50:
    o+=2
    total=total+o
print(total)
#reverse a string
s=input("enter your string")
i=len(s)-1
while i>=0:
   print(s[i], end="")
   i-=1
