############################
# Author: Shu'aib Solomons
# Date: 04/03/2019
############################

def  mergeStrings(a, b):
    mergSource = ""
    lengthA = len(a)
    lengthB = len(b)

    if lengthA>=lengthB:
        for i in range(lengthB):
            mergSource += a[i]
            mergSource += b[i]
        if(lengthA>lengthB):
            mergSource += a[lengthB:]
                
    if lengthB>=lengthA:
        for i in range(len(a)):
            mergSource += a[i]
            mergSource += b[i]
        if(lengthB>lengthA):
            mergSource += b[lengthA:]
                
    return mergSource

print(mergeStrings("abcaaaa","def"))
