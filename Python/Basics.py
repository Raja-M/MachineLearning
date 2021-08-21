#!/usr/bin python

import re

print( 'Hello world!');
'''
x = int(input("Please Enter an integer : " ))
print( type(x))
print( type('Raja'))
print( isinstance(  ('Raja'), str) )
'''
#

#Python's principal types can be categorized into the following: numeric, sequences,
#   mappings, classes, instances, exceptions.
#import builtins							
#dir(builtins)							
#							
#int	        integer	point					
#float	    floating numbers					
#complex	    complex						
#bool	    booleans						
#str	        strings	array	of	bytes			
#bytes	    fixed of bytes				
#bytearray	array						
#object	    objects						
#function	functions	item	sequence	(arrays)			
#list	    ordered	order	item	sequence	(fixed	arrays)	
#tuple	    fixed	collection	of	key/value	pairs	(hashes)	
#dict	    unordered	collection	of	unique	items		
#set	        unordered	objects					
#file	    File						
#							
#							
# '__build_class__'							
# '__debug__'							
# '__doc__'							
# '__import__'							
# '__loader__'							
# '__name__'							
# '__package__'							
# '__spec__'							
# 'abs'							
# 'all'							
# 'any'							
# 'ascii'							
#'ArithmeticError'							
# 'AssertionError'							
# 'AttributeError'							
# 'BaseException'							
# 'bin'							
# 'BlockingIOError'							
# 'bool'							
# 'breakpoint'							
# 'BrokenPipeError'							
# 'BufferError'							
# 'bytearray'							
# 'bytes'							
# 'BytesWarning'							
# 'callable'							
# 'ChildProcessError'							
# 'chr'							
# 'classmethod'							
# 'compile'							
# 'complex'							
# 'ConnectionAbortedError'							
# 'ConnectionError'							
# 'ConnectionRefusedError'							
# 'ConnectionResetError'							
# 'copyright'							
# 'credits'							
# 'delattr'							
# 'DeprecationWarning'							
# 'dict'							
# 'dir'							
# 'divmod'							
# 'Ellipsis'							
# 'enumerate'							
# 'EnvironmentError'							
# 'EOFError'							
# 'eval'							
# 'Exception'							
# 'exec'							
# 'exit'							
# 'False'							
# 'FileExistsError'							
# 'FileNotFoundError'							
# 'filter'							
# 'float'							
# 'FloatingPointError'							
# 'format'							
# 'frozenset'							
# 'FutureWarning'							
# 'GeneratorExit'							
# 'getattr'							
# 'globals'							
# 'hasattr'							
# 'hash'							
# 'help'							
# 'hex'							
# 'id'							
# 'ImportError'							
# 'ImportWarning'							
# 'IndentationError'							
# 'IndexError'							
# 'input'							
# 'int'							
# 'InterruptedError'							
# 'IOError'							
# 'IsADirectoryError'							
# 'isinstance'							
# 'issubclass'							
# 'iter'							
# 'KeyboardInterrupt'							
# 'KeyError'							
# 'len'							
# 'license'							
# 'list'							
# 'locals'							
# 'LookupError'							
# 'map'							
# 'max'							
# 'MemoryError'							
# 'memoryview'							
# 'min'							
# 'ModuleNotFoundError'							
# 'NameError'							
# 'next'							
# 'None'							
# 'NotADirectoryError'							
# 'NotImplemented'							
# 'NotImplementedError'							
# 'object'							
# 'oct'							
# 'open'							
# 'ord'							
# 'OSError'							
# 'OverflowError'							
# 'PendingDeprecationWarning'							
# 'PermissionError'							
# 'pow'							
# 'print'							
# 'ProcessLookupError'							
# 'property'							
# 'quit'							
# 'range'							
# 'RecursionError'							
# 'ReferenceError'							
# 'repr'							
# 'ResourceWarning'							
# 'reversed'							
# 'round'							
# 'RuntimeError'							
# 'RuntimeWarning'							
# 'set'							
# 'setattr'							
# 'slice'							
# 'sorted'							
# 'staticmethod'							
# 'StopAsyncIteration'							
# 'StopIteration'							
# 'str'							
# 'sum'							
# 'super'							
# 'SyntaxError'							
# 'SyntaxWarning'							
# 'SystemError'							
# 'SystemExit'							
# 'TabError'							
# 'TimeoutError'							
# 'True'							
# 'tuple'							
# 'type'							
# 'TypeError'							
# 'UnboundLocalError'							
# 'UnicodeDecodeError'							
# 'UnicodeEncodeError'							
# 'UnicodeError'							
# 'UnicodeTranslateError'							
# 'UnicodeWarning'							
# 'UserWarning'							
# 'ValueError'							
# 'vars'							
# 'Warning'							
# 'WindowsError'							
# 'ZeroDivisionError'							
# 'zip'							

#isinstance() is better than type() because it can check for inheritance relationships.
#if x <  0:
#        print( 'Entered negative vaule')
#elif ( x == 1 ):
#        print( 'Single')
#else:
#        print('More')
#
#words = [ 'cat', 'window', 'defenestrate']
#
#for w in words:
#        print(w, len(w))
#
#for i in range(5):
#	print("I :" , i)
#
#for i in (range(5,20, 4)):
#	print("I :", i)
#
#
#for n in range(2,10):
#	for x in range(2,n):
#		if n%x == 0:
#			print(n, 'equals' , x , ' * ' , n/x )
#			break
#	else:
#		print(n, 'is a prime number')
#	
'''	
fruit = ['Apple', 'Orange', 'Banana', 'Watermelon']
color = ['red', 'orange', 'yellow', 'green', 'blue']
for f, c in zip(fruit, color):
    print(f'The {f} is {c}')
'''
#
#for n in range(2,10):
#	if n % 2 == 0:
#		print('Found an even number ', n)
#		continue
#	print('Found odd number ', n)	
#
#def fib(n):
#	"""Print a Fibonacci series up to n."""
#	""""#even functions without a return statement do return a value, albeit a rather boring one. This value is called None (it’s a built-in name). """
#	a,b = 0,1
#	while (a < n ):
#		print(a,  end=' ')
#		a, b = b, a+b
#	
#
#fib(100)
#
#def ask_ok(prompt, retries=4, reminder = 'Plees try again !'):
#	while True:
#		ok = input(prompt)
#		if ok in ('y', 'ye', 'yes'):
#			return True
#		elif (ok in ('n','no', 'nop', 'nope')):
#			return False
#		retries = retries - 1
#		if retries < 0:
''' 
    A defaultdict() is a collection that instead of raising a KeyError when an invalid key is
    requested, it will invoke a user-provided function and return a value from that
    function. That returned value is stored in the dictionary.
    Example:'

from collections import defaultdict
str1 = 'hi'
class TestCls:
    pass
    def __init__(self):
        pass
    def __call__(self):
         return 'Hi'
d5 = defaultdict(TestCls())
d5['greet1'] = 'hello'
print(d5['greet1'], d5['greet2'])
print(  d5['greet2'])

#			raise ValueError('In valid user response')
#		print( reminder )
#
#ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
'''
'''
class MyContextManager(object):
    def __enter__(self):
        print('in enter')
        return 'foo'
    def __exit__(self, typ, value, traceback):
        print('in exit')

with MyContextManager() as obj1, MyContextManager() as obj2:
         print(obj1)
         print(obj2)
    


global_y = 10
def change_global_y():
    global global_y
    global_y = 20
change_global_y()
print(global_y) # 20 

lst = [1, 2, 3]

lst *= 3
print(lst)


'''
'''
class Contact:
    def __init__( self, name='', address='', email=''):
        self.name = name
        self.address = address
        self.email = email
        
    @property
    def email(self):
        return self._email
   
    @email.setter
    def email(self, email):
        self._email = ''
        if '@' in email:
            self._email = email
            
#super().__init__(name, address, phones)    
        
        
c = Contact('John smith', email='Raja@' )

print(c.name )
print(c.email )

'''
'''

def find ( pattern, search_str):
    if re.match( pattern, search_str ):
        print(f' Begins with {pattern}')
    else:
        print(f'{pattern} not found at begninig')
        
    
    if re.search(pattern, search_str):
        print(f' Contains {pattern}')
    else:
        print(f'{pattern} not found within')
        
    
speech = 'This is just becoming as Lion'

find('This', speech)
'''
'''
#?, * zero or more + one or more.
pattern = r'''
(\(+\d{3}\)+)+ # optional area code, parentheses optional
[-\s.]? # opt. separator: dash, space, or period
\d{3} # 3-digit prefix
[-\s.] # separator: dash, space, or period
\d{4} # final 4-digits
'''

phones = [
'123-456-7890',
'800 555 4400',
'(123) 456-7890',
'123.456.7890',
'123-4567',
'reallywrong',
'1234-456-7890'
]


valid = [ph for ph in phones if re.match(pattern, ph, re.VERBOSE)]
print(f'Valid phones: {valid}')

'''
python3 -m venv my_env
source ./my_env/bin/activate
'''


