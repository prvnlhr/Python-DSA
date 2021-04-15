def lonfges(l):
    m = {l[i]: i for i in range(len(l) - 1, -1, -1)}
    visited = {}
    start, end = l[0], l[0]
    startM, endM = start, end
    for num in l:
        if num not in visited:
            visited[num] = True
            start, end = num, num
            while start - 1 in m:
                start -= 1
                visited[start] = True
            while end + 1 in m:
                end += 1
                visited[end] = True
            if (endM - startM + 1 < end - start + 1) or (
                    (endM - startM + 1 == end - start + 1) and (m[start] < m[startM])):
                startM, endM = start, end
    return startM, endM
