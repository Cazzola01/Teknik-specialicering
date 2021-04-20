from pyglet.gl import *
import math

class Renderer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

        #Storing geometric shapes classes
        self.points = []
        self.segments = []
        self.circles = []
        self.triangles = []

    class Point():
        def __init__(self, position, color):
            self.position = position
            self.color = color

    class Segment():
        def __init__(self, start, end, color):
            self.start = start
            self.end = end
            self.color = color

    class Circle():
        def __init__(self, position, radius, color):
            self.start = position #{x: , y:}
            self.end = radius
            self.color = color
            self.vertices = []  # For rendering

            self.add_vertices()

        def add_vertices(self):
            for x in range(360):
                self.vertices.append((self.position[0]+math.cos(math.radians(x))*self.radius,
                                      self.position[1]+math.sin(math.radians(x))*self.radius))

    class Triangle():
        def __init__(self, edge_0_position, edge_1_position, edge_2_position, color):
            self.edge_0_position = edge_0_position
            self.edge_1_position = edge_1_position
            self.edge_2_position = edge_2_position
            self.color = color

    def addPoint(self, position, color):
        self.points.append(self.Point(position, color))

    def addSegment(self, start, end, color):
        self.segments.append(self.Segment(start, end, color))

    def addCircle(self, position, radius, color):
        self.circles.append(self.Circle(position, radius. color))

    def addTriangle(self, edge_0_position, edge_1_position, edge_2_position):
        self.triangles.append(self.Triangle(edge_0_position, edge_1_position, edge_2_position))

    def add_render_object(self, type, vertices, id, color):
        self.render_objects[id] = {}
        self.render_objects[id]["type"] = type
        if type == "Circle":
            # vertices always stores center-point as first element in list and radius as second element
            center = vertices[0]
            radius = vertices[1]
            #A circle has a center-point and radius
            self.render_objects[id]["vertices"] = [center]
            self.render_objects[id]["radius"] = radius
            for i in range(360):
                self.render_objects[id]["vertices"].append((center[0]+math.cos(math.radians(i))*radius,
                                                            center[1]+math.sin(math.radians(i))*radius))
        elif type == "Quad":
            #A quad is rendered as two trangles where the diagonals are overlapping
            self.render_objects[id]["vertices"] = [vertices[0], vertices[1], vertices[2],
                                                   vertices[0], vertices[2], vertices[3]]
        else:
            self.render_objects[id]["vertices"] = vertices
            self.render_objects[id]["neighbors"] = [] #neigburs for Astar
        self.render_objects[id]["color"] = color

    def draw(self):
        glClearColor(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        for obj in self.render_objects.values():
            if obj["type"] == "Triangle" or obj["type"] == "Quad":
                glBegin(GL_TRIANGLES)
                for vertex in obj["vertices"]:
                    rgb = obj["color"]
                    glColor3f(rgb[0], rgb[1], rgb[2])
                    glVertex2f(vertex[0], vertex[1])
                glEnd()
            elif obj["type"] == "Circle":
                glBegin(GL_TRIANGLE_FAN)
                for vertex in obj["vertices"]:
                    rgb = obj["color"]
                    glColor3f(rgb[0], rgb[1], rgb[2])
                    glVertex2f(vertex[0], vertex[1])
                glEnd()
            elif obj["type"] == "Point":
                glPointSize(4)
                glBegin(GL_POINTS)
                for vertex in obj["vertices"]:
                    rgb = obj["color"]
                    glColor3f(rgb[0], rgb[1], rgb[2])
                    glVertex2f(vertex[0], vertex[1])
                glEnd()
            elif obj["type"] == "Line":
                glBegin(GL_LINES)
                for vertex in obj["vertices"]:
                    rgb = obj["color"]
                    glColor3f(rgb[0], rgb[1], rgb[2])
                    glVertex2f(vertex[0], vertex[1])
                glEnd()
    def get_render_object(self):
        return self.render_objects