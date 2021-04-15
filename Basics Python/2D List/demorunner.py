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
