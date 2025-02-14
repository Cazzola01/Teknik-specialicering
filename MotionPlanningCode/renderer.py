from pyglet.gl import *
import math

# Storing geometric shapes classes
points = []  # [Point(), Point(), Point()]
segments = []  # [Segment(), Segment(), Segment()]
circles = []  # [Circle(), Circle(), Circle()]
triangles = []  # [Triangle(), Triangle(), Triangle()]


class Point:
    def __init__(self, position, color):
        self.position = position
        self.neighbors = []  # [Point(), Point(), Point(), Point(), Point()]
        self.color = color


class Segment:
    def __init__(self, start, end, color):
        self.start = start
        self.end = end
        self.color = color


class Circle:
    def __init__(self, position, radius, color):
        self.position = position  # {x: , y:}
        self.radius = radius
        self.color = color


class Triangle:
    def __init__(self, vertices, color):
        self.vertices = vertices  # [(2,3), (2,3), (2,3)]
        self.color = color


# Adding classes to their list
# O(1)
def add_point(position, color):
    points.append(Point(position, color))  # adding to list


def add_segment(start, end, color):
    segments.append(Segment(start, end, color))  # adding to list


def add_circle(position, radius, color):
    circles.append(Circle(position, radius, color))  # adding to list


def add_triangle(vertices, color):
    triangles.append(Triangle(vertices, color))


# rendering all objects
# O(len(renderer.points) + len(renderer.segments + len(renderer.circles + len(renderer.triangles))
def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # circle
    for circle in circles:
        glBegin(GL_TRIANGLE_FAN)

        # Make triangles in a circle
        vertices = []
        for i in range(360):
            x = circle.position[0]
            y = circle.position[1]
            vertices.append((x + math.cos(math.radians(i)) * circle.radius,
                             y + math.sin(math.radians(i)) * circle.radius))

        glColor3f(circle.color[0], circle.color[1], circle.color[2])
        for vertex in vertices:
            x = vertex[0]
            y = vertex[1]
            glVertex2f(x, y)
        glEnd()

    # triangle
    for triangle in triangles:
        glBegin(GL_TRIANGLES)
        glColor3f(triangle.color[0], triangle.color[1], triangle.color[2])
        for vertex in triangle.vertices:
            x = vertex[0]
            y = vertex[1]
            glVertex2f(x, y)
        glEnd()

    # point
    for point in points:
        glPointSize(4)
        glBegin(GL_POINTS)
        glColor3f(point.color[0], point.color[1], point.color[2])

        x = point.position[0]
        y = point.position[1]
        glVertex2f(x, y)
        glEnd()

    # segment
    for segment in segments:
        glBegin(GL_LINES)

        glColor3f(segment.color[0], segment.color[1], segment.color[2])

        # start
        x = segment.start[0]
        y = segment.start[1]
        glVertex2f(x, y)

        # end
        x = segment.end[0]
        y = segment.end[1]
        glVertex2f(x, y)

        glEnd()
