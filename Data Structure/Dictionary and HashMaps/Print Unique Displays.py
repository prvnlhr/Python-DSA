def uniqueChars(string):
    d = {}
    temp = ''
    for s in string:
        if s not in d:
            d[s] = 1
            # print(s,end=" ")
            temp = temp + s
        else:
            d[s] = d[s] + 1
    return temp

# Main
string = input()
print(uniqueChars(string))
