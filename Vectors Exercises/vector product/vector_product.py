
def vector_product(v1,v2):

    x1,y2,z1 = v1
    x2,y2,z2 = v2
    
    a = (v1[1]*v2[2])-(v1[2]*v2[1])
    b = (v1[2]*v2[0])-(v1[0]*v2[2])
    c = (v1[0]*v2[1])-(v1[1]*v2[0])
    multiplication = (a,b,c)
    return multiplication


v1 = (1,0,0)
v2 = (0,1,0)
example = vector_product(v1,v2)
print(f"Vector product v1 {v1} - v2 {v2} = {example}")
