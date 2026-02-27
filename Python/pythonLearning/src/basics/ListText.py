from collections import deque
from math import pi
Sample_list = ["abc", 34, True, 40, "male"]
mylist = ["apple", "berry", "cherry"]
print(len(mylist))
print(mylist[0])
print("apple" in mylist)

quantity=[1,2,3]
x=[mylist,quantity]
print(x)
print(x[0])

print(type(mylist))
print(mylist[1],mylist[-1],mylist[2:5])
mylist[2] = "strawberry"
mylist.insert(2, "watermelon")
mylist.append("orange")
mylist.extend(Sample_list)
mylist.remove("apple")
mylist.count("watermelon")
mylist.index('watermelon')
mylist.pop(1)
print("------------")
print(mylist)
#mylist.sort()
#mylist.sort(reverse = True)#decending order sort
mylist.reverse()
#queue
queue=deque(["john","rahul","michael"])
queue.append("terry")
print(queue)
queue.popleft()
print(queue)
#list comprehension
[print(x) for x in mylist]
list(map(lambda x:x**2,range(10)))
y=[str(round(pi,i)) for i in range(1,6)]
print(y)
copylist = mylist.copy()
mylist.clear()
del mylist

