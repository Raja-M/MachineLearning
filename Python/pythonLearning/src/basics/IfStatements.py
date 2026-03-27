x = int( input("Enter a number: ") )
# there is no switch statement in python but we can use if-elif-else statement to achieve the same result
if x < 0:
    print("Negative number")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

num=10
if num > 0:
    print("This is a positive number")
s
n = 3
if n % 2 == 0:
    print("this is an even number")
    print("this is in the true statement block")
else:
    print("this is an odd number")
    print("This is in the false statement block")
print("this is always printed")

n = 4
if n % 2 == 0:
    print("this is an even number")
    print("this is in the true statement block")
else:
    print("this is an odd number")
    print("This is in the false statement block")
print("this is always printed")

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not Found"
        case 418:
            return "I'm a teapot"
        case _:
            return "somthing wrong with the internet"



