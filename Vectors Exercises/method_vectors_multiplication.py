
def vector_mutiplication(v1,k):
    # Delcaration of vector
    x1,y1 = v1

    multipication = (v1[0]*k,v1[1]*k)
    return multipication

result = vector_mutiplication((-3, 5),-2)
# is a mistake because the funtion is being asigned, no executed
# result = vector_mutiplication
print("The result of multiplication between the vector 1 (-3, 5) and scaled -2 is: ",result)