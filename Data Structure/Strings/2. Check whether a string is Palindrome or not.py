def palindromeOrNot(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return 'NOT PALINDROME'
        i = i + 1
        j = j - 1
    return 'IT IS PALINDROME'


s = input()
ans = palindromeOrNot(s)
print(ans)
