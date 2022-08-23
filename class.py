class MyClass:
  x = 5
  y = 6
  n = 1
  sonia = 25
print(MyClass)
p1 = MyClass()
print(p1.x)
print(p1.y)
print(p1.n)
print(p1.sonia)


#The __init__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)



class car:
    wheel = 4
    def __init__(self,colour,style):
        self.colour = colour
        self.style = style
        
c = car("style","colour")

print(c.style)
print(c.colour)

c.style = "suv"
print(c.style)


#Object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


#
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

