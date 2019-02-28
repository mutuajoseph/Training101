# # Task 1 Complete
#
# myInput = input("Enter a String: ")
#
# if myInput == "Yes" or myInput=="YES" or myInput== "yes":
#      print("Yes")
# else:
#     print("No")

# # Task 2 InComplete

# def maxNumber(a,b,c):
#
#     x = int (a)
#     y = int (b)
#     z  = int (c)
#     if x > z and  x > y:
#      return a
#     elif y > x and y > z:
#      return b
#     elif z > x and z > y:
#      return c
#     else:
#         return "equal"
#
# x = int(input("Enter variable one: "))
# y = int(input("Enter variable two: "))
# z = int(input("Enter variable three: "))
#
# max = maxNumber(x,y,z)
# print(max)

# # Task 3 Complete
#
# def a(myList):
# Jose = [myList[0],myList[-1]]
# print(myList)

 # Task 4 Complete

Number = int(input("Enter a number : "))

    if Number % 4 == 0:
        print(Number," is even and a multiple of 4")
     elif Number % 2 == 0:
        print(Number," is even and a multiple of 2")
    else:
        print(Number," is an odd number")

# task 5

tuples = (1,2,3,4,5,6,7,8,9,10)

# Inorder for the list to balance as the length of the tuple increase output length then divide it by two after typecasting it
tuple1 = tuples[:int(len(tuples)/2)]
tuple2 = tuples[int(len(tuples)/2):]

print(tuple1)
print(tuple2)
