x = 10
y = 10
print(x==y)
# is keyword checks if objects refer to the same object

x =[1,2,3]
y = x
print( x is y)

#casting

x = int(1.132)
print(x)

x = str("s1")
print(x)

for x in "banana":
    print(x)

mytuple = ("apple", "banana","cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))


mylist = [1,2,35,66]
it = iter(mylist)
print(next(it))
print(next(it))


mystr = "Banana"
its = iter(mystr)
print(next(its))
print(next(its))


class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} (age is : {self.age})"
    def myfunc(self):
        print("Hello my name is: " + self.name)


p1 = Person("john",40)
print(p1.name , p1.age)
print(p1)
p1.myfunc()


class Student(Person):
    def __init(self,fname,lname):
        self.fname = fname;
        self.lname = lname
x = Student("Mike","Johnson")
print(x.name)


my_array = [7, 12, 9, 4, 11, 8]
my_array.append(100)
my_array.sort()
print(my_array)


my_array = [90,3,98,70,34,9,2,45]
min_val = my_array[0]

for i in my_array:
    if i < min_val:
        min_val = i
print("Lowest value is " , min_val)


stack = []

stack.append('A')
stack.append('B')
stack.append(10)
print(stack)

#stack = last in first out = LIFO

#peek
topElement = stack[-1]
print("PEEK : " , topElement)

#pop

poppedElement = stack.pop()
print(poppedElement)

print(stack)