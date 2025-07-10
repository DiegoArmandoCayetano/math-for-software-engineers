import math
from calculate_angle_between_vectors import calculate_dot_product
from method_vectors_multiplication import linear_combination
def projection_of_one_vector_onto_another(v1,v2):
    x1, y1 = v1
    x2, y2 = v2

    # step 1 / dot_product

    # step 2 / squared modulus of v2

    squared_modulus_of_v2 = abs(math.pow(v2[0],2)+math.pow(v2[1],2))
    first_operation = (calculate_dot_product(v1,v2),squared_modulus_of_v2)
    #scalar_multiplication_scalar_by_vector = ((first_operation*v2[0]),(first_operation*v2[1]))
    #return scalar_multiplication_scalar_by_vector
    
    result = (linear_combination(first_operation,first_operation,v2[0],v2[1]))
    return result

result = projection_of_one_vector_onto_another((2,3),(1,4))
print(result)