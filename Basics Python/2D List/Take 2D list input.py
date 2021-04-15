
#space separated rows

# list input________________________________________

# 1D List_________________  __________________________________
# for integer array input:
listInt = [int(i) for i in input("Enter no of elements:").strip().split()]
# for string array input:
listStr = [i for i in input("Enter no of elements:").strip().split()]

print(list)

# 2D matrix input___________________________________________
# take row and col in one line space separated:
# str = input().split()
# n , m = int(str[0],int(str[1]))

rows = int(input())
cols = int(input())
# CONVENTIONAL WAY:_____________________
martix =[]
for i in range(rows):
    a =[]
    for j in range(cols):
         a.append(int(input()))
    martix.append(a)
print(martix)
#     OR
# USING LIST COMPREHENSION:_____________
mat1 = [[int(i) for i in input().strip().split()] for x in range(rows)]

# mat2  = [  []  for x in range(rows) ]
        # [[for i in input().strip().split()] for x in range(rows)]
        # [[ int(i) for i in input().strip().split()] for x in range(rows)]
# OR
mat2 = [[int(input()) for x in range(cols)] for y in range(rows)]

print(mat1, mat2)
