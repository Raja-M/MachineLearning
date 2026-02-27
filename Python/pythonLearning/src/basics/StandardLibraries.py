import os
os.getcwd()
# os.chdir('/Users/HP/Desktop')
# os.system('mkdir today')
# dir(os)
# help(os)

import shutil
# shutil.copyfile("data.db",'archive.db')
# shutil.move('/build/executables', 'installdir')

import glob #making file lists from directory wildcard searches
glob.glob('*.py')

import sys#command line arguments
print(sys.argv)
sys.stderr.write('Warning, log file not found starting a new one\n')
sys.exit()#terminate a script

# import argparse

# parser = argparse.ArgumentParser(
#     prog='top',
#     description='Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)

import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

'tea for too'.replace('too', 'two')

import math
math.cos(math.pi / 4)
math.log(1024, 2)

import random
random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)   
random.randrange(6)   

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
statistics.median(data)
statistics.variance(data)

from datetime import date
now = date.today()
print(now)

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)
import zlib#Data Compression
s = b'witch which has which witches wrist watch'
print(len(s))#41
t = zlib.compress(s)
print(len(t))#37
zlib.decompress(t)
zlib.crc32(s)#32-bit Cyclic Redundancy Check (CRC) checksum

from timeit import Timer#Performance Measurement
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
 
Timer('a,b = b,a', 'a=1; b=2').timeit()

import reprlib #similar to repr()
reprlib.repr(set('supercalifragilisticexpialidocious'))

import pprint #adds line breaks and indentation
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)

import textwrap #formats paragraphs of text 
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))

import locale#accesses a database of culture specific data formats
locale.setlocale(locale.LC_ALL, 'English_United States.1252')

conv = locale.localeconv()  #x = 1234567.8 get a mapping of conventions

locale.format_string("%d", x, grouping=True)#'1,234,567'

locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True)#$1,234,567.80'

from string import Template

t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')

import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
print([heappop(data) for i in range(3)] )

from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)
round(.70 * 1.05, 2)