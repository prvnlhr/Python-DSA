# S = int(input())
# E = int(input())
# W = int(input())
#
# while S < E:
#     ans = ((S - 32) * 5) / 9
#     integralAns = int(ans)
#     print(S, " ", integralAns)
#     S = S + W



def printTable(start,end,step):
    while start < end:
        ans = ((start - 32) * 5) / 9
       	integralAns = int(ans)
       	print(start, " ", integralAns)
        start = start + step



s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)





