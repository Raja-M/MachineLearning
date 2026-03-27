#string format
import math
import json
year=2016
event="Referendum"
print(f"result of the {year} {event}")

s="hello world."

print(str(s))
print(repr(s)) 

print(f'the value of pi is approcimately{math.pi:.3f} .')

print('we are the {} who say "{}!"'.format('knights',"ni"))

#convert values '!a' is ascii(),'!s' is str(),'!r' is repr()
animals='eels'
print(f'my hovercraft is full of {animals}.')
print(f'my hovercraft is full of {animals!r}.')

x=[1,'simple','list']
json.dumps(x)

# with open("samplefile","+r") as f:
#     read_data=f.read()#or
#     read_data=f.readline()#or read single line
#     read_data=f.readlines()#read entire line
#     f.write("this is a test")
#     f.tell()
#     f.seek(5)
