fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)
x = "Python is "
y = "awesome"
z =  x + y
print(z)
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))




x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))



import random

print(random.randrange(1, 10))


x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


print(x)
print(y)
print(z)
print(w)



x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print(x)
print(y)
print(z)




a = "Lorem ipsum dolor sit amet,consectetur adipiscing elit,sed do eiusmod tempor incididuntut labore et dolore magna aliqua."
print(a)



a = "Hello, World!"
print(a[7])


for x in "banana":
 print(x)

for n in "courage":
 print(n)

a = "Hello, World!"
print(len(a))


b = "courage"
print(len(b))


txt = "The best things in life are free!"
print("faith" in txt)



txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")



b = "Hello, World!"
print(b[2:5])



b = "Hello, World!"
print(b[-5:-2])

