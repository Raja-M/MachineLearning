import sys
import datetime

a = int( input( "Input an integer : "))

n1 = int( "%s" % a)
n2 = int ( "%s%s" % (a, a ))
n3 = int ( "%s%s%s" % (a, a, a))

print ( n1, n2, n3)
print ( n1 + n2 + n3 )

############################################
# exam_date = ( 11, 23, 2025)
# print(" The exam will start from : %i / %i / %i" % exam_date)
# fileName = input( "Enter file name : ")
#
# f_extns = fileName.split(".")
#
# print( f_extns[-1])
############################################
# values = input("Input some numbers with comma-separated numbers : ")
#
# list = values.split(",")
#
# tuple = tuple(list)
#
# print(" List : " , list)
# print (" Tuple : ", tuple)
#
# tuple1 = ( 1, 3, 8)
# list.append(100)
# tuple.__add__(tuple1)
#
# print(" List2 : " , list)
# print (" Tuple2 : ", tuple)

############################################
# firstName = input("Enter your first name :")
#
# lastName = input ("Enter your last name :")
#
# print("Hello "+ lastName + " " + firstName )
#
# fullName = firstName + " " + lastName
#
# print( len(fullName))
# reverseName = ""
# for i in range(len(fullName) - 1 , -1, -1) :
#     reverseName = reverseName + fullName[i]
#
# print( reverseName)

############################################
# print ( " version Info")
# print ( sys.version_info)
#
# now = datetime.datetime.now()
# print (f"Current date and time : { now.strftime("%Y-%m-%d %H:%M:%S") } " )

############################################
# def tree(n):
#     leaves(n)
#     trunk(n)
#
# def leaves(n):
#     for i in range(n):
#         space = " " * (n - i - 1)
#         leaf = "*" * (2 * i + 1)
#         print(space + leaf)
#         print(f"i : {i}" )
#
# def trunk(n):
#     for i in range(n):
#         space = " " * (n - 1)
#         leaf = "*"
#         print(space + leaf)
#
# tree(5)