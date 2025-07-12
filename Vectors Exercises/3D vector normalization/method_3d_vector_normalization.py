import math

def vector_normalization_3d(vector):
    x1,y1,z1 = vector

    module = math.sqrt(math.pow(x1,2)+math.pow(y1,2)+math.pow(z1,2))
    divided_vector = (vector[0]/module,vector[1]/module,vector[2]/module)
    return divided_vector


vector = (3, 4, 0)
example = vector_normalization_3d(vector)
print(f"Vector {vector} - normalized vector {example}")

# Explanation about the topic in spanish with VideoGames
# https://youtu.be/BApEahU_eFI?si=QKAmNdTENxJ2Ew1j
