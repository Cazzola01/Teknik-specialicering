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
    return [b[0]-a[0], b[1]-a[1]]  # [x1-x2, y1-y2]


# rotate vector 90 degrees
def get_normal_vector(a):  # O(1)
    return [-a[1], a[0]]  # [-y,x]


def dot_product(a, b):  # O(1)
    return a[0]*b[0]+a[1]*b[1]


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
                print("inside!")
                renderer.points.remove(point)

def get_vector_length(v): #O(1)
    distance = (v[0] ** 2 + v[1] ** 2) ** 0.5  # pytagoras sats
    return distance


# Increases the length on both axis
def vector_scaling(v, k):  # O(1)
    return [v[0]*k, v[1]*k]


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




def segment_triangle_collision():
    for triangle in renderer.triangles:
        for segment in list(renderer.segments):
            if lineSegmentCheck

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
    generate_all_points(num=100)
    point_circle_collision()
    point_triangle_collision()
    knn(k=5)

@window.event
def on_draw():
    window.clear()
    renderer.draw()


pyglet.app.run()