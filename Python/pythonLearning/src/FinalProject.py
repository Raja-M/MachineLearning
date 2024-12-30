def tree(n):
    leaves(n)
    trunk(n)

def leaves(n):
    for i in range(n):
        space = " " * (n - i - 1)
        leaf = "*" * (2 * i + 1)
        print(space + leaf)

def trunk(n):
    for i in range(n):
        space = " " * (n - 1)
        leaf = "*"
        print(space + leaf)

tree(5)