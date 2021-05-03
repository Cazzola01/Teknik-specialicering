import MotionPlanningCode.vector as vector
import MotionPlanningCode.renderer as renderer


def segment_triangle_check(segment, triangle):
    segment_vector = vector.create_vector(segment.start, segment.end)
    segment_normal = vector.get_normal_vector(segment_vector)

    a = triangle.vertices[0]
    b = triangle.vertices[1]
    c = triangle.vertices[2]

    p1 = vector.create_vector(segment.start, a)
    p2 = vector.create_vector(segment.start, b)
    p3 = vector.create_vector(segment.start, c)

    ab = vector.create_vector(a, b)
    bc = vector.create_vector(b, c)
    ca = vector.create_vector(c, a)

    n1 = vector.get_normal_vector(ab)
    n2 = vector.get_normal_vector(bc)
    n3 = vector.get_normal_vector(ca)

    a_segment_start = vector.create_vector(a, segment.start)
    a_segment_end = vector.create_vector(a, segment.end)
    b_segment_start = vector.create_vector(b, segment.start)
    b_segment_end = vector.create_vector(b, segment.end)
    c_segment_start = vector.create_vector(c, segment.start)
    c_segment_end = vector.create_vector(c, segment.end)

    if vector.dot_product(segment_normal, p1) >= 0\
            and vector.dot_product(segment_normal, p2) >= 0\
            and vector.dot_product(segment_normal, p3) >= 0\
            or vector.dot_product(segment_normal, p1) <= 0\
            and vector.dot_product(segment_normal, p2) <= 0\
            and vector.dot_product(segment_normal, p3) <= 0:
        return False

    elif vector.dot_product(n1, a_segment_start) < 0 < vector.dot_product(n1, a_segment_end)\
            or vector.dot_product(n1, a_segment_start) > 0 > vector.dot_product(n1, a_segment_end):
        return True
    elif vector.dot_product(n2, b_segment_start) < 0 < vector.dot_product(n2, b_segment_end)\
            or vector.dot_product(n2, b_segment_start) > 0 > vector.dot_product(n2, b_segment_end):
        return True
    elif vector.dot_product(n3, c_segment_start) < 0 < vector.dot_product(n3, c_segment_end)\
            or vector.dot_product(n3, c_segment_start) > 0 > vector.dot_product(n3, c_segment_end):
        return True
    else:
        return False


# O(len(renderer.triangles) * len(renderer.segments))
def segment_triangle_collision():
    for triangle in renderer.triangles:
        for segment in list(renderer.segments):
            if segment_triangle_check(segment, triangle):
                renderer.segments.remove(segment)


# returns True/False if the parameters collide
# O(1)
def segment_circle_check(segment, circle):
    ab = vector.create_vector(segment.start, segment.end)
    ba = vector.create_vector(segment.end, segment.start)
    v1 = vector.dot_product(ab, vector.create_vector(segment.start, circle.position))
    v2 = vector.dot_product(ba, vector.create_vector(segment.end, circle.position))

    if v1 > 0 and v2 > 0:
        o = vector.orthogonal_projection(vector.create_vector(segment.start, circle.position), ab)
        distance = vector.get_vector_length(vector.create_vector(vector.create_vector(segment.start, circle.position), o))

        if distance < circle.radius:
            return True
    elif v1 < 0:
        if vector.get_distance(circle.position, segment.start) < circle.radius:
            return True
    elif v2 < 0:
        if vector.get_distance(circle.position, segment.end) < circle.radius:
            return True


# O(len(renderer.circles) * len(renderer.segments))
def segment_circle_collision():
    for circle in renderer.circles:
        for segment in list(renderer.segments):
            if segment_circle_check(segment, circle):
                renderer.segments.remove(segment)


# O(len(renderer.circles) * len(renderer.points))
def point_circle_collision():
    for circle in renderer.circles:
        for point in list(renderer.points):
            distance = vector.get_distance(circle.position, point.position)
            if distance < circle.radius:
                renderer.points.remove(point)


# O(1)
def point_triangle_collision():
    for triangle in renderer.triangles:
        for point in list(renderer.points):
            a = triangle.vertices[0]
            b = triangle.vertices[1]
            c = triangle.vertices[2]

            ab = vector.create_vector(a, b)
            bc = vector.create_vector(b, c)
            ca = vector.create_vector(c, a)

            if (vector.dot_product(vector.get_normal_vector(ab), vector.create_vector(a, point.position)) >= 0)\
                    and (vector.dot_product(vector.get_normal_vector(bc), vector.create_vector(b, point.position)) >= 0)\
                    and (vector.dot_product(vector.get_normal_vector(ca), vector.create_vector(c, point.position)) >= 0):
                renderer.points.remove(point)
