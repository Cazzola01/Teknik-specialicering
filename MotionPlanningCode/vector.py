# Getting distance between two points with Pythagoras
# O(1)
def get_distance(vector1, vector2):
    x1 = vector1[0]
    y1 = vector1[1]

    x2 = vector2[0]
    y2 = vector2[1]

    distance = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)  # Pythagoras
    return distance


# Takes two positions and returns a the vector between the points
# O(1)
def create_vector(a, b):
    return [b[0] - a[0], b[1] - a[1]]  # [x1-x2, y1-y2]


# rotate vector 90 degrees
# O(1)
def get_normal_vector(a):  # O(1)
    return [-a[1], a[0]]  # [-y,x]


# O(1)
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1]


# Vector distance from (0,0)
# O(1)
def get_vector_length(v):
    distance = (v[0] ** 2 + v[1] ** 2) ** 0.5  # Pythagoras
    return distance


# Increases the length on both axis
# O(1)
def vector_scaling(v, k):  # O(1)
    return [v[0] * k, v[1] * k]


# O(1)
def vector_multiplication(v, k):
    return [v[0] * k, v[1] * k]


# O(1)
def orthogonal_projection(u, v):
    k = dot_product(u, v) / get_vector_length(v) ** 2
    return vector_multiplication(v, k)
