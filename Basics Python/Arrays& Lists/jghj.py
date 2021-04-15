import sys

def rotateArray(a, b):
    ret = []
    if len(a) == 1:
        return a
    for i in range(len(a)):
        if i + b < len(a):
            ret.append(a[i + b])
    # for j in range(b):
    # ret.append(a[j])
    return ret

# a = [ 14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77, 35 ]
a = [1]
# a = [1, 2, 3, 4, 5]
# b = 56
b = 1
print(rotateArray(a, b))
