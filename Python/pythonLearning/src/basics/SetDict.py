#set
myset = {"apple", "banana", "cherry"}
print(len(myset))
set1 = {"abc", 34, True, 40, "male"}
print(type(myset))
thisset = set(("apple", "banana", "cherry")) 
print(thisset)

thisset = {"apple", "banana", "cherry"}#no indexing in set

for x in thisset:
  print(x)
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)
thisset.remove("banana")
print(thisset)
#If the item to remove does not exist, remove() will raise an error

thisset.discard("banana")
#If the item to remove does not exist, discard() will NOT raise an error

x = thisset.pop()#randomly pop data
print(x)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
thisset.clear()
del thisset
#Unlike sets, elements cannot be added or removed from a frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
#set comprehension
a={x for x in "python Learning" if x not in 'abc'}
print(a)
#dict
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict["brand"])
print(len(mydict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
print(thisdict.get("model"))
print(thisdict.keys())
thisdict["color"] = "white"
print(thisdict.values())
print(thisdict.items())
#dic comprehension
mydic={x:x**2 for x in (2,3,4)}
print(mydic)
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in thisdict")
thisdict.update({"year": 2020})

#thisdict.pop("model")
thisdict.popitem()
mydict = thisdict.copy()#or
mydict = dict(thisdict)

#del thisdict["model"]
thisdict.clear()