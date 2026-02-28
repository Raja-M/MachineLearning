tuple1 = ("abc", 34, True, 40, "male")
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))
print(type(mytuple))
thistuple = tuple(("apple", "banana", "cherry"))
print(mytuple[1])
print(mytuple[-1])
print(mytuple[1:])
y = list(mytuple)
y[1] = "kiwi"
x = tuple(y)

y = list(mytuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

fruits = ("apple", "banana", "cherry")#packing a tuple
(green, yellow, red) = fruits #unpacking a tuple
print(green)
print(yellow)
print(red)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

del thistuple