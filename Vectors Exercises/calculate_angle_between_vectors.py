import math

def calculate_dot_product(v1,v2):
   x1, y1 = v1
   x2, y2 = v2

   dot_product = ( (v1[0]*v2[0]) + (v1[1]*v2[1]) )
   return dot_product

def calculate_angle_between_vectors(v1,v2):
   
   '''x1, y1 = v1
   x2, y2 = v2

   dot_product = ( (v1[0]*v2[0]) + (v1[1]*v2[1]) )'''

   sum_exponent_v1 = (math.pow(v1[0],2))+(math.pow(v1[1],2))
   sum_exponent_v2 = (math.pow(v2[0],2))+(math.pow(v2[1],2))

   module_v1 = math.sqrt(sum_exponent_v1)
   module_v2 = math.sqrt(sum_exponent_v2)

   cos = (calculate_dot_product(v1,v2)/(module_v1*module_v2))
   angle_cos=math.acos(cos)
   degree=angle_cos*(180/math.pi)
   return degree

v1=(2,3)
v2=(4,-1)
result = calculate_angle_between_vectors(v1,v2)
print(f"Angle between vectors {v1} and {v2} = {result}")
