# solved by me:
# trick to solve this question is that for a particular element in array we have to find all the +1 Consecutive
# as well as -1 Consecutive . we can use a map to find Consecutive element O(1).
# after find all the Consecutive chain of element we will maintain the count and if it is larger the maxCount
# we will update maxCount
# now let say we got two chains for two different elements of same count the will we return chain whose start occurs
#  first in input arr. we can do this by find the index of start and comparing ti with the previous chain start.
def longestConsecutiveSubsequence(arr):
    m = {l[i]: i for i in range(len(l) - 1, -1, -1)}
    visited = {}
    start, end = l[0], l[0]
    startM = start
    endM = end
    maxCount = 0
    index = len(arr)

    # startM, endM = start, end
    for num in l:
        count = 0
        if num not in visited:
            visited[num] = True
            start, end = num, num
            while start - 1 in m:
                start -= 1
                visited[start] = True
                count = count + 1
            while end + 1 in m:
                end += 1
                visited[end] = True
                count = count + 1
            # print("start:", start, "end:", end)
            startIndex = arr.index(start)

            # print("i", startIndex, "index:", index, "count:", count, "maxCount:", maxCount)
            if count > maxCount:
                maxCount = count
                startM = start
                endM = end
            if count == maxCount:
                if startIndex <= index:
                    index = startIndex
                    startM = start
                    endM = end
            # print("startM:", startM, "endM:", endM)
            # print()

    return startM, endM


n = int(input())
l = list(int(i) for i in input().strip().split(' '))
start, end = longestConsecutiveSubsequence(l)
print(start, end)
# for num in range(start, end + 1):
#     print(num)
