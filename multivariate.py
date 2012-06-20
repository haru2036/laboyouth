import random
def multivariate(weights):
    weightsum=0
    for x in weights:
        weightsum+=x
    random1=random.randint(0,weightsum)
    weightsum=0
    for i,x in enumerate(weights):
        weightsum+=x
        if weightsum>random1:
            return i

    
    
w=[4,2,3]
print multivariate(w)
