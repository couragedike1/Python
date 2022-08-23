

#string
first_name  = "Courage"
print(f"hello {first_name}")
print(first_name[2])
print(first_name[0:2])
print(first_name.title())
print(first_name.upper())
print(first_name.lower())
print(first_name.replace('!'  , '.'))
print(first_name.isalnum())
print(first_name.islower())
print(first_name.swapcase())


#Declaring  Functions 
x = 25
y  = 25

if y<x:
   print(" x is greeter than y")
elif x==y:
    print("x is equal to  y")
else:
    print("  y is greater than x ")


price = [23.5,4,2.3,9.0]
price.sort()
price.append(39)
print(price)
print(type(price))
print(price.index(4))
print(max(price))
print(min(price))
print(len(price))

scores = (2.4, 6.9, 3.6, 8.3, 2.0, 4.5)
print(scores[4])

#Tuples

tuple1 = (2.4,6.9,3.6,8.3,2.0,4.5)
tuple2 = (1, 2,3,4,5,6)

new_tuple = tuple1 +  tuple2

print(new_tuple)
del new_tuple

#Set

colour = set(["yellow", "blue", "purple"])
game = {"football",  "javeline", "car_racing", "swimming"}
mycolour= set(["Green", "yellow","pink", "purple"])

print(len(colour))
print(game)
print(tuple1 +  tuple2)
print(colour.union(game))
print(colour & mycolour)
print(colour - mycolour)
print(colour ^ mycolour)


#Dict

employee1 =  {"Name":"courage",
              "age"  :  "30",
              "job"  :  "devpos",
              "city" : "lagos",
              "email":"hp44real@yahoo.com"}
employee1["phone"] = "123456789"

print(employee1)

print(employee1["Name"])

print(employee1["age"])
print(employee1.get("job"))

#Merge Two Dictionaries

D1 = {"name": "courage",
      "age":"30",
      "job": "data scientist"}
D2 = {"name": "sonia",
      "age": "25",
      "job": "banker"}
D1.update(D2)
X = D1.pop("age")
#D2.clear()

print(D1)
print(D2)
              

#While loop

x = 1
while x < 10:
    print (x)
    x= x+1


#Functions

def  hello():
    print("Hello World")

hello()

def my_function():
    print("Hello from a function")

my_function()


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def hello(name):
    print("hello,  " + name)
hello("Courage")
hello("Sonia")



#Passing two argument


def func(name , job):
    print(name, "is a", job)

func("Courage", "developer")
func("Sonia" , "maker")
func("nathan", "businessman")
func("Chi", "farmer" )


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")



#Default Parameter Value


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
my_function("Nigeria")

#Passing a List as an Argument

def my_function(food):
  for x in food:
    print(x)

x  = ["apple", "banana", "cherry"]

my_function(x)

#Return Values

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


def sum(a, b):
    return a + b
x = sum(5,7)

print(x)


#Recursion

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(10)

#Variable Length Arguments (*args and **kwargs)
def print_arguments(*args):
    print(args)

print_arguments(1,54,60,8,98,12)



def print_argument(**kwargs):
    print(kwargs)
print_argument(name="bobs", age=25, job="Analyst")



#Return Multiple Values

def func(a,b):
    return a+b, a-b
result = func(20,10)
print(result)

#Docstring

help(hello)



