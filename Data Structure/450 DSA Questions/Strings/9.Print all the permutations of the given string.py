result = []


def permutationHelper(data, i, length):
    if i == length:
        result.append(''.join(data))
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permutationHelper(data, i + 1, length)
            data[i], data[j] = data[j], data[i]


def permutation(s):
    permutationHelper(list(s), 0, len(s))


s = input()
permutation(s)
print(str(result))
