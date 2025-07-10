
def vector_multiplication(v1,k):
    # Delcaration of vector
    x1,y1 = v1

    multiplication = (v1[0]*k,v1[1]*k)
    return multiplication

result = vector_multiplication((-3, 5),-2)
# is a mistake because the funtion is being asigned, no executed
# result = vector_mutiplication
print("The result of multiplication between the vector 1 (-3, 5) and scaled -2 is: ",result)

def linear_combination(v1,v2,k1,k2):
    x1, y1 = v1
    x2, x2 = v2
    multiplication_v1 = ((k1*v1[0]),k1*v1[1])
    multiplication_v2 = ((k2*v2[0]),k2*v2[1])
    sum = ((multiplication_v1[0]+multiplication_v2[0]),(multiplication_v1[1]+multiplication_v2[1]))
    return sum

v1=(1,4)
v2=(-2,3)
k1=3
k2=-1

result_2=linear_combination(v1,v2,k1,k2)
print(f"{v1}*{k1} + {v2}*{k2} = {result_2}")
