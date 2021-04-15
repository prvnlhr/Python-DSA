def ArraySpecialSum(n, arr):
    sum = 0

    for i in range(len(arr)):

        sum = sum + arr[i]
        print("sum",i, sum)
        if sum >= 10:
            print(sum)
            digit1 = sum % 10
            sum = sum // 10
            print(sum, digit1)
            sum = sum + digit1

    return sum




n = int(input())
arr = [int(i) for i in input().split()]
print(ArraySpecialSum(n, arr))
