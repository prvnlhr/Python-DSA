def clamp(minWidth, maxWidth, minFontSize, maxFontSize):
    n = (maxFontSize - minFontSize)
    m = ((maxWidth / 16) - (minWidth / 16))
    slope = n / m
    print(slope)
    x = minWidth/16
    yInter = (-x * slope + minFontSize)
    

    print(f'{minFontSize}rem , {yInter}rem + {slope * 100}vw, {maxFontSize}rem')
    
minWidth = int(input())
maxWidth = int(input())
minFontSize = float(input())
maxFontSize = float(input())


clamp(minWidth, maxWidth, minFontSize, maxFontSize)







