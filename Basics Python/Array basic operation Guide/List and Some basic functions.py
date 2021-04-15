# 1 : CREATING AN ARBITRARY ARRAY
# let say we have array of size 5 and we want to create other array of same size and copy all elements
arr1 = [1, 2, 3, 4, 5]

# arr2 = [None]*len(arr1)
# arr_name = [initialise value = None for null] * size
# here we took size == len(arr) = arr1 size

# for i in range(len(arr1)):
# arr2[i]  = arr1[i]
# print("arr1 :" ,arr2)

# 2 : CREATING ARRAY AND TAKE USER INPUT FOR ELEMENTS:
# arr = list([int(i) for i in input().strip().split()])

# 3 : TRAVERSING ARRAY IN REVERSE ORDER
arr3 = [1, 2, 3, 4, 5]
print("reverse traverse", end=" : ")
for i in arr3[::-1]:
    print(i, end=" ")

# or using range_____________________
print()
print("reverse traverse using range", end=" : ")
for i in range(len(arr3) - 1, -1, -1):
    print(arr3[i], end=" ")
#
#
# ____2D Array___:
rows = int(input())
cols = int(input())

# 1.take matrix type input:
mat1 = [[int(i) for i in input().strip().split()] for x in range(rows)]
# 1 2 3
# 4 5 6
# 7 8 9
# OR
#
# 2.this take line wise input:
mat2 = [[int(input()) for x in range(cols)] for y in range(rows)]
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
#
# OR
#
# 3.take input in one line:
b = input().split()
mat3 = [[int(b[cols * i + j]) for j in range(cols)] for i in range(rows)]
# 1 2 3 4 5 6 7 8 9 10 11 12

# print("mat1:", mat1)
print("mat2:", mat2)
