#################################
# Author: Shu'aib Solomons
# Date: 04/03/2019
#################################

def finalPrice(prices):

    nonDiscount = []
    sumAmount = 0
    
    for i in range(len(prices)):
        notDiscount = 0
        for j in range(i+1, len(prices)):
            if (prices[i]>=prices[j]):
                sumAmount += prices[i]-prices[j]
                notDiscount = 1
                break
        
        if(notDiscount == 0):
            sumAmount +=prices[i]
            nonDiscount.append(i)

    print(sumAmount)
    for i in nonDiscount:
        print(i,end = " ")


#finalPrice([5,1,3,4,6,2])
finalPrice([5,1,3,3,2,5])
