from MotionPlanningCode.Renderer import Renderer
import pyglet
import random
from pyglet.window import key, mouse


def generate_all_points(num=100):
    for x in range(num):
        random_x = random.randint(0, width)
        random_y = random.randint(0, height)
        renderer.add_point(position=(random_x, random_y), color=[0, 0, 0])


def get_distance(vector1, vector2):  # Just calculation. O(1)
    x1 = vector1[0]
    y1 = vector1[1]

    x2 = vector2[0]
    y2 = vector2[1]

    distance = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)  # pytagoras sats
    return distance


def point_circle_collision():
    for circle in renderer.circles:
        for point in list(renderer.points):
            distance = get_distance(circle.position, point.position)
            if distance < circle.radius:
                renderer.points.remove(point)


# Takes two positions and returns a the vector between the points
def create_vector(a, b):  # O(1)
    return [b[0] - a[0], b[1] - a[1]]  # [x1-x2, y1-y2]


# rotate vector 90 degrees
def get_normal_vector(a):  # O(1)
    return [-a[1], a[0]]  # [-y,x]


def dot_product(a, b):  # O(1)
    return a[0] * b[0] + a[1] * b[1]


def point_triangle_collision():
    for triangle in renderer.triangles:
        for point in list(renderer.points):
            a = triangle.vertices[0]
            b = triangle.vertices[1]
            c = triangle.vertices[2]

            ab = create_vector(a, b)
            bc = create_vector(b, c)
            ca = create_vector(c, a)

            if (dot_product(get_normal_vector(ab), create_vector(a, point.position)) >= 0) \
                    and (dot_product(get_normal_vector(bc), create_vector(b, point.position)) >= 0) \
                    and (dot_product(get_normal_vector(ca), create_vector(c, point.position)) >= 0):
                renderer.points.remove(point)


def get_vector_length(v):  # O(1)
    distance = (v[0] ** 2 + v[1] ** 2) ** 0.5  # pytagoras sats
    return distance


# Increases the length on both axis
def vector_scaling(v, k):  # O(1)
    return [v[0] * k, v[1] * k]


# comparing every point to every point and making a line between the k closest ones
def knn(k=5):
    for point in renderer.points:
        distance_and_point_list = []
        for compare_point in renderer.points:
            distance_and_point_list.append([get_distance(point.position, compare_point.position), compare_point])
        distance_and_point_list = sorted(distance_and_point_list, key=lambda x: x[0])
        distance_and_point_list = distance_and_point_list[1:]  # removing first element, which is 0, compared to itself
        distance_and_point_list = distance_and_point_list[:k]  # Just the 5 first points
        for distance_and_point in distance_and_point_list:
            renderer.add_segment(start=point.position, end=distance_and_point[1].position, color=[0.8, 0.8, 0.8])


def segment_triangle_check(segment, triangle):
    segment_vector = create_vector(segment.start, segment.end)
    segment_normal = get_normal_vector(segment_vector)

    a = triangle.vertices[0]
    b = triangle.vertices[1]
    c = triangle.vertices[2]

    p1 = create_vector(segment.start, a)
    p2 = create_vector(segment.start, b)
    p3 = create_vector(segment.start, c)

    ab = create_vector(a, b)
    bc = create_vector(b, c)
    ca = create_vector(c, a)

    n1 = get_normal_vector(ab)
    n2 = get_normal_vector(bc)
    n3 = get_normal_vector(ca)

    a_segment_start = create_vector(a, segment.start)
    a_segment_end = create_vector(a, segment.end)
    b_segment_start = create_vector(b, segment.start)
    b_segment_end = create_vector(b, segment.end)
    c_segment_start = create_vector(c, segment.start)
    c_segment_end = create_vector(c, segment.end)

    if dot_product(segment_normal, p1) >= 0 and dot_product(segment_normal, p2) >= 0 and dot_product(segment_normal,
                                                                                                     p3) >= 0 \
            or dot_product(segment_normal, p1) <= 0 and dot_product(segment_normal, p2) <= 0 and dot_product(
        segment_normal, p3) <= 0:
        return False

    elif dot_product(n1, a_segment_start) < 0 < dot_product(n1, a_segment_end) or dot_product(n1,
                                                                                              a_segment_start) > 0 > dot_product(
            n1, a_segment_end):
        return True
    elif dot_product(n2, b_segment_start) < 0 < dot_product(n2, b_segment_end) or dot_product(n2,
                                                                                              b_segment_start) > 0 > dot_product(
            n2, b_segment_end):
        return True
    elif dot_product(n3, c_segment_start) < 0 < dot_product(n3, c_segment_end) or dot_product(n3,
                                                                                              c_segment_start) > 0 > dot_product(
            n3, c_segment_end):
        return True
    else:
        return False


def segment_triangle_collision():
    for triangle in renderer.triangles:
        for segment in list(renderer.segments):
            if segment_triangle_check(segment, triangle):
                renderer.segments.remove(segment)


def vector_multiplication(v, k):  # O(1)
    return [v[0] * k, v[1] * k]


def orthogonal_projection(u, v):
    k = dot_product(u, v) / get_vector_length(v) ** 2
    return vector_multiplication(v, k)


def segment_circle_check(segment, circle):
    ab = create_vector(segment.start, segment.end)
    ba = create_vector(segment.end, segment.start)
    v1 = dot_product(ab, create_vector(segment.start, circle.position))
    v2 = dot_product(ba, create_vector(segment.end, circle.position))

    if v1 > 0 and v2 > 0:
        o = orthogonal_projection(create_vector(segment.start, circle.position), ab)
        distance = get_vector_length(create_vector(create_vector(segment.start, circle.position), o))

        if distance < circle.radius:
            return True
    elif v1 < 0:
        if get_distance(circle.position, segment.start) < circle.radius:
            return True
    elif v2 < 0:
        if get_distance(circle.position, segment.end) < circle.radius:
            return True


def segment_circle_collision():
    for circle in renderer.circles:
        for segment in list(renderer.segments):
            if segment_circle_check(segment, circle):
                renderer.segments.remove(segment)


# if any segment contains a point, it means the other side of the segment is neighbor
def add_neighbors_to_points():
    for point in renderer.points:
        for segment in renderer.segments:
            if point.position == segment.start:
                point.neighbors.append(segment.end)
            elif point.position == segment.end:
                point.neighbors.append(segment.start)


def reconstruct_path(came_from, current):  # n is number of elements in come_from. O(n)
    total_path = [current]
    while current in came_from.keys():  # loop every came_from
        current = came_from[current]
        total_path.insert(0, current)  # Add element on first position
    return total_path


def a_star(start, goal, h=get_distance):
    open_set = [start]
    came_from = {}
    g_score = {}
    f_score = {}
    for point in renderer.points:
        g_score[point.position] = float('inf')
        f_score[point.position] = float('inf')
    g_score[start] = 0
    f_score[start] = h(start, goal)

    while open_set:
        # Smallest value in open_set
        current = min(open_set, key=f_score.get)
        if current == goal:
            return reconstruct_path(came_from, current)

        open_set.remove(current)

        # Finding index where point.position == current position
        for x, point in enumerate(renderer.points):
            if point.position == current:
                index = x
                break

        for neighbor in renderer.points[index].neighbors:
            tentative_g_score = g_score[current] + h(start, goal)
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + h(neighbor, goal)
                if neighbor not in open_set:
                    open_set.append(neighbor)
    return []


if __name__ == '__main__':
    width = 800
    height = 800
    window = pyglet.window.Window(width=width, height=height)
    renderer = Renderer()

    # Add objects
    renderer.add_circle(position=(200, 600), radius=100, color=[1, 0, 0])
    renderer.add_triangle(vertex_0_position=(300, 300), vertex_1_position=(700, 300), vertex_2_position=(700, 700),
                          color=[1, 0, 0])
    renderer.add_triangle(vertex_0_position=(100, 100), vertex_1_position=(300, 100), vertex_2_position=(700, 200),
                          color=[1, 0, 0])
    generate_all_points(num=500)
    point_circle_collision()
    point_triangle_collision()
    knn(k=5)
    segment_triangle_collision()
    segment_circle_collision()
    add_neighbors_to_points()
    print(a_star(renderer.points[0].position, renderer.points[1].position, h=get_distance))


@window.event
def on_draw():
    window.clear()
    renderer.draw()


pyglet.app.run()
