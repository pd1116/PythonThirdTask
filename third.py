a = int(input("How many terms? "))
x,y = 0, 1
i = 0
if a <= 0:
   print("Please enter a positive integer")
elif a == 1:
   print("Fibonacci sequence upto",a," is :")
   print(x)
else:
   print("Fibonacci sequence:")
   while i < a:
       print(x)
       t = x+y
       x = y
       y = t
       i += 1
