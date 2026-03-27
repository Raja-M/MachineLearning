
# hello = "Hello"
# print(len(hello))
# print(hello[0])
# print("H" in hello)
#
# fruits = ["apple", "berry", "cherry"]
# for fruit in fruits:
#     print(fruit)
#
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)
#         break
users={'hans':'active','mohan':'inactive','rekha':'active'}
for user,status in list(users.items()):
    if status=='inactive':
        del users[user]
print(users)
active_users={}
for user,status in users.items():
    if status=='active':
        active_users[user]=status
print(active_users)
#fibonacci
a=0
b=1
for num in range(10):
    print(a)
    a,b=b,a+b

