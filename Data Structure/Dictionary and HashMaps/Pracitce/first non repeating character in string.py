# W3resources sol: optimised by storing index of elements:
def first_non_repeating_character(str1):
    char_order = []
    ctr = {}
    for c in str1:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1
            char_order.append(c)
    for c in char_order:
        if ctr[c] == 1:
            return c
    return None


# 100% my sol:
def nonRepeatingChar(string):
    m = {}
    for i in string:
        if i in m:
            ele = i
            m[ele] = m[ele] + 1
        else:
            ele = i
            m[ele] = 1
    for ele in m:
        if m[ele] == 1:
            return ele


string = input()
print(first_non_repeating_character(string))
