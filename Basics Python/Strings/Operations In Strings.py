# Split:
str = "My name is Praveen"
li = str.split(' ', 2)
print(li)

# Replace:
str1 = 'This is a test1 String'
print(str1)
newStr1 = str1.replace('test1', 'test2')
print(newStr1)

# Find:
str = 'Finding in String '
index = str.find('Stri')
# // Also we can specify the part of string where to find
# index = str.find('Stri', startIndex , endIndex)
print(index)
# Upper / lower case
str3 = "demo case"
ans = str3.upper()
print(ans)
ans2 = str3.lower()
print(ans2)

# startswith()
str4 = 'I am Starting With I am'
ans3 = str4.startswith('I am')
ans4 = str4.startswith('I amo')
print(ans3, ans4)
# //Also we can provide part of string
ans5 = str4.startswith('Sta', 5, 21)
ans5 = str4.startswith('Sta', 5,)
print(ans5)
