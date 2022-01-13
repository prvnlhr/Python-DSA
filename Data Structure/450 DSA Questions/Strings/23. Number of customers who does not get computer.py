# 2, “ABBAJJKZKZ” should return 0
# 3, “GACCBDDBAGEE” should return 1 as ‘D’ was not able to get any computer
# 3, “GACCBGDDBAEE” should return 0
# 1, “ABCBCA” should return 2 as ‘B’ and ‘C’ were not able to get any computer.
# 1, “ABCBCADEED” should return 3

from collections import defaultdict


# SELF SOLVED PASSES 100% test cases
def countCustomers1(arr, k):
    map = defaultdict()
    count = 0
    for char in arr:

        if char in map:
            if map[char] == 0:
                count = count + 1

            elif map[char] == 1:
                k = k + 1

        elif char not in map:
            if k > 0:
                map[char] = 1
                k = k - 1
            elif k == 0:
                map[char] = 0
    return count


# SELF SOLVED PASSES 100% test cases
def countCustomers(n, seq):
    map = defaultdict()
    count = 0
    for char in seq:

        if char in map:

            if map[char] == 0:
                count = count + 1

            elif map[char] == 1:
                n = n + 1

        elif char not in map:
            if n > 0:
                map[char] = 1
                n = n - 1
            elif n == 0:
                map[char] = 0
    return count


# n = int(input())
# seq = input()

# gfg input
input = [[2, 'ABBAJJKZKZ'], [3, 'GACCBDDBAGEE'], [3, 'GACCBGDDBAEE'], [1, 'ABCBCA'], [1, 'ABCBCADEED']]

# CN input
input = [[2, [1, 2, 2, 1]], [2, [1, 3, 2, 1, 2, 3]]]

for obj in input:
    n = obj[0]
    seq = obj[1]
    print(n, seq)
    # ans = countCustomers(n, seq)
    ans = countCustomers1(seq, n)
    print(ans)
