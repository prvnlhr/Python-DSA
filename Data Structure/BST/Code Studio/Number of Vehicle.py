def numberOfVehicles(districtCount, alpha1, alpha2, alpha3, alpha4, dig1, dig2, dig3, dig4):
    ans1 = 1 + ord(alpha2) - ord(alpha1)
    ans2 = 1 + ord(alpha4) - ord(alpha3)
    ans3 = (dig1 + 1) * (dig2 + 1) * (dig3 + 1) * ((dig4 + 1))
    finalANs = ans1 * ans2 * ans3 * districtCount
    return finalANs


def takeInput():
    dist = int(input())
    charString = [i for i in input().strip().split()]
    Digits = [int(j) for j in input().strip().split()]

    return dist, charString, Digits


# t = int(input())
# while t > 0:
# dist, charString, Digits = takeInput()
# print(dist,charString,Digits)
def takeInput():
    
    dist = int(input())
    charString = [i for i in input().strip().split()]
    Digits = [int(j) for j in input().strip().split()]
    return dist, Digits, charString


t = int(input())
while t > 0:
    dist, Digits, charString = takeInput()
    dig1 = Digits[0]
    dig2 = Digits[1]
    dig3 = Digits[2]
    dig4 = Digits[3]
    alpha1 = charString[0]
    alpha2 = charString[1]
    alpha3 = charString[2]
    alpha4 = charString[3]
    print(numberOfVehicles(dist, alpha1, alpha2, alpha3, alpha4, dig1, dig2, dig3, dig4))
    t = t - 1

