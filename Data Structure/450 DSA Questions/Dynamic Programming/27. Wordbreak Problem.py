def wordBreak(wordList, word):
    if word == '':
        return True
    if not word:
        return True
    length = len(word)
    for i in range(1, length + 1):
        prefix = word[:i]
        if prefix in wordList and wordBreak(wordList, word[i:]):
            return True
    return False


def wordBreakDp(s, wordDict):
    dp = [False for i in range(len(s) + 1)]
    dp[0] = True
    for i in range(1, len(s) + 1):
        for word in wordDict:
            length = len(word)
            if length <= i and word == s[i - length: i]:
                dp[i] = dp[i] or dp[i - length]
    return dp[-1]


wordList = {"i", "like", "sam", "sung", "samsung", "mobile", "ice",
            "cream", "icecream", "man", "go", "mango"}

word = input()
print(wordBreak(wordList, word))
