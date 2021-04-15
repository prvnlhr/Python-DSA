flag = True
while flag:
    n = int(input())
    if n==1 :
        a = int(input())
        b = int(input())
        print(a+b)
    if n==2:
        a = int(input())
        b = int(input())
        print(a-b)
    if n==3:
        a = int(input())
        b = int(input())
        print(a*b)
    if n==4:
        a = int(input())
        b = int(input())
        print(int(a//b))
    if n==5:
        a = int(input())
        b = int(input())
        print(int(a%b))
    if n==6:
        flag = False
    if(n > 6):
        print("Invalid Operation")
