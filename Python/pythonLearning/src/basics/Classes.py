class MyClass:
    i=1245
    def f(self):
        return "hello world"
obj=MyClass()
print(obj.i,obj.f())
# class Complex:
#     def __init__(self,realpart,imaginarypart):
#         self.r=realpart
#         self.i=imaginarypart
# x=complex(3,-4.5)
# print(x.r,x.i)

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

#inheritance
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  

class MappingSubclass(Mapping):

    def update(self,keys,values):
        for item in zip(keys, values):
            self.items_list.append(item)
            
my_instance = MappingSubclass(iterable=[]) 
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
my_instance.update(keys,values)
print(my_instance.items_list)

#Generator  
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)