import math
import decimal
from decimal import *
def GeoSum(k):

    if(k==0):
        return 1



    ans = GeoSum(k-1)+ 1/Decimal(math.pow(2,k))
    return ans




k = int(input())
print(GeoSum(k))
