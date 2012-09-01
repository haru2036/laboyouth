import random
def binarysearch(weights):
    #print weights
    weightsum=0
    weightlist=[]
    for i,x in enumerate(weights):
        weightlist.append(weightsum)
        weightsum+=x

    random1=random.randint(0,weightsum)
    #print weightlist
    weightlen=len(weightlist)
    num2=weightlen
    num1=0
    #print random1
    while (num2-num1)!=1:
        mid=(num1+num2)/2
        #print mid,weightlist[mid]
        if random1<weightlist[mid]:
            num2=mid
        else:
            num1=mid
       # print num1,num2
    return num1


