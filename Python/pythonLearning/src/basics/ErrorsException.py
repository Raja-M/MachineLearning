import sys
#syntax errors

#while True print('Hello world')

#exceptions
#10 * (1/0)
#ZeroDivisionError
# 4 + spam*3
# NameError
# '2' + 2
# TypeError

#try-except-else
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
#raise
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
