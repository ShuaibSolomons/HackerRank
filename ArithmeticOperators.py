##############################
# Author: Shu'aib Solomons
# Date: 25/02/2019
##############################

def InputOperations(a, b):
    answer = []

    addish = a+b
    answer.append(addish)

    subtract = a-b
    answer.append(subtract)

    multi = a*b
    answer.append(multi)
    
    return answer


if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    answer = InputOperations(a,b)
    for i in range(len(answer)):
        print(answer[i])

