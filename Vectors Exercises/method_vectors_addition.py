
def vectors_addition(v1, v2):
    
    # Parameters as a tuple
    # v1 = (x1,y1)
    # v2 = (x2,y2)

    # Return a tuple like = (x1+x2, y1+y2)
    
    x1, y1 = v1 
    x2, y2 = v2

    # is like to say
    #x1 = v1[0]  # first value → 3
    #y1 = v1[1]  # second value → 2

    addition = (v1[0] + v2[0], v1[1] + v2[1])
    return addition


#example
a = (3,2)
b = (-1,4)

result = vectors_addition(a,b)
print("the sum te vector 1 (3,2) and vector 2 (-1,4) is:", result)