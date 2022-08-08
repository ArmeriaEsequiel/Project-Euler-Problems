import numpy as np

def get_diagonal(flattenMatrix,positionCounter):
    positionCounter = positionCounter
    maxPosition = 4
    bound = len(flattenMatrix)-1
    diagonalProduct = 1
    while(positionCounter <= bound):
        diagonalProduct = diagonalProduct * flattenMatrix[positionCounter]
        positionCounter = positionCounter + maxPosition
    return(diagonalProduct)


def get_diagonal_mirror(flattenMatrix,positionCounter):
#    s = 1
#    i = columPosition
#    j = rowPosition + 3
#    for k in range(i,i-4,-1):
#        print("k es {}".format(k))
#        s = A[][k]
#    for k in range(rowPosition,j):
#        print("k es {}".format(k))
        #print("j es {}".format(j))
##       print("j-k es {}".format(j-k))
#        print(" es {}".format(columPosition-k))
#        s = A[k][i]
#        i = i -1
#        print("s es {}".format(s))
#        print("-----------------------------------")
#    return(s)
    positionCounter = positionCounter
    maxPosition = 2
    notFished = True
    bound = len(flattenMatrix)-1
    DiagonalMirrorProduct = 1
    while(positionCounter < bound):
        if(positionCounter %3 == 0):
            return( DiagonalMirrorProduct * flattenMatrix[positionCounter])    
        DiagonalMirrorProduct = DiagonalMirrorProduct * flattenMatrix[positionCounter]
        positionCounter = positionCounter + maxPosition
    return(DiagonalMirrorProduct)







def get_right(flattenMatrix,positionCounter):
    loopbound = positionCounter+2
    maxbound = len(flattenMatrix)-1
    rightProd = 1
#    print("PositionCounter es {}".format(positionCounter))
    while(positionCounter <= loopbound and positionCounter <= maxbound):
        rightProd = rightProd * flattenMatrix[positionCounter]
        positionCounter += 1
    return(rightProd)


def get_down(flattenMatrix,positionCounter):
    verticalProd = 1
    maxPosition = 3
    bound = len(flattenMatrix)-1
    while(positionCounter <= bound):
        verticalProd = verticalProd * flattenMatrix[positionCounter]
        positionCounter = positionCounter + maxPosition
    return(verticalProd)


#A = [[1,2,3,2],[4,5,6,2],[7,8,9,2],[2,2,2,2]]
A = np.array([[1,2,3],[4,5,6]])
flattenMatrix = A.flatten()
#print(len(flattenMatrix))
maxDown = 0
maxDiagonal = 0
maxRight = 0
maxMirror = 0

for i in range(0,len(flattenMatrix)):
    maxDown = max(maxDown, get_down(flattenMatrix,i))
    #print("maxDown es {} en poisition {}".format(maxDown,i))
    maxDiagonal = max(maxDiagonal, get_diagonal(flattenMatrix,i))
    #print("maxDiagonal es {} en poisition {}".format(maxDiagonal,i))
    maxRight = max(maxRight,get_right(flattenMatrix,i))
    #print("maxRight es {} en poisition {}".format(maxRight,i))
    maxMirror = max(maxMirror,get_diagonal_mirror(flattenMatrix,i))
    #print("maxMirror es {} en poisition {}".format(maxMirror,i))
    #print("-------------------------------------------------------------")
result = max(maxDown,maxDiagonal,maxMirror,maxRight)
print(result)

#f = get_down(flattenMatrix,3)
#f = get_diagonal(flattenMatrix,2)
#f = get_right(flattenMatrix,2)
#f = get_diagonal_mirror(flattenMatrix,2)
#print(f)
