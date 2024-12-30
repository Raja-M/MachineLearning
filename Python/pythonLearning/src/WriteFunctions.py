def area(width, height):
    return width * height

result = area(5, 10)
print(result)

def max(x, y):
    if x > y:
        return x
    return y

print(max(8, 4))

def reverse(s):
    result = ""
    for c in s:
        result = c + result
    return result
print(reverse("Hewo"))

def find_evens(num):
    result = []
    for n in range(num):
        if n % 2 == 0:
            result.append(n)
    return result
print(find_evens(10))
