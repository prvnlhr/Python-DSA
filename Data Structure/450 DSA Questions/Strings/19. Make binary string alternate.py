# Input : str = “001”
# Output : 1
# Minimum number of flips required = 1
# We can flip 1st bit from 0 to 1
#
# Input : str = “0001010111”
# Output : 2
# Minimum number of flips required = 2
# We can flip 2nd bit from 0 to 1 and 9th
# bit from 1 to 0 to make alternate
# string “0101010101”.


# Python3 implementation of the approach.

# Function to return the minimum number of
# characters of the given binary string
# to be replaced to make the string alternating
#
# In order to find the minimum replacements,
# count the number of replacements to convert
# the string in type 1 and store it in count
# then minimum replacement will be min(count, len – count)
# where len is the length of the string. len – count is
# the number of replacements to convert the string in type 2.

def minReplacement(s, length):
    ans = 0
    for i in range(0, length):

        # If there is 1 at even index positions
        if i % 2 == 0 and s[i] == '1':
            ans += 1

        # If there is 0 at odd index positions
        if i % 2 == 1 and s[i] == '0':
            ans += 1

    return min(ans, length - ans)
