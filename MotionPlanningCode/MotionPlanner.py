import json
from MotionPlanningCode.Renderer import Renderer
import pyglet
import random
import time

def reciveData():
    with open('obstaclesCircles.json') as json_file:
        data = json.load(json_file)
        # print(data)

def GenerateAllPoints(num=100):
    for x in range(num):
        random_x = random.randint(0, 800)
        random_y = random.randint(0, 800)
        tuplePoint = (random_x, random_y)
        id = "point" + str(x)
        renderer.add_render_object("Point", [tuplePoint], id, [0, 0, 0])

def GetDistance(vector1, vector2):
    x1 = vector1[0]
    y1 = vector1[1]

    x2 = vector2[0]
    y2 = vector2[1]

    distance = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5) #pytagoras sats
    return distance

def CircleCollision():
    #Searshing for Circle
    render_objects = renderer.get_render_object()
    remove_keys = []
    for key1 in render_objects:
        value1 = render_objects[key1]
        if value1["type"] == "Circle":
    #Searshing for Point
            for key2 in render_objects:
                value2 = render_objects[key2]
                if value2["type"] == "Point":
    #Calculating distance
                    distance = GetDistance(value1['vertices'][0], value2['vertices'][0]) #GetDistance(origo_Circle, origo_Point)
                    circle_radius = value1['radius']
                    if distance < circle_radius:
                        remove_keys.append(key2)
    for key in remove_keys:
        renderer.remove_render_object(key)

def CreateVector(a,b):
    return [b[0]-a[0],b[1]-a[1]] #[x1-x2, y1-y2]

def GetNormalVector(a):
    return [-a[1], a[0]] #[-y,x]

def DotProduct(a,b):
    return a[0]*b[0]+a[1]*b[1]

def GetVectorLength(v):
    distance = (v[0] ** 2 + v[1] ** 2) ** 0.5  # pytagoras sats
    return distance

def VectorMultiplication(v, k):
    return [v[0]*k, v[1]*k]

def TriangleCollision():
    render_objects = renderer.get_render_object()
    #Searshing for Circle
    remove_keys = []
    for key1 in render_objects:
        value1 = render_objects[key1]
        if value1["type"] == "Triangle":
    #Searshing for Point
            for key2 in render_objects:
                value2 = render_objects[key2]
                if value2["type"] == "Point":
                    point = value2['vertices'][0]
                    triangle_points = value1['vertices']

                    A = triangle_points[0]
                    B = triangle_points[1]
                    C = triangle_points[2]

                    AB = CreateVector(A, B)
                    BC = CreateVector(B, C)
                    CA = CreateVector(C, A)

                    if (DotProduct(GetNormalVector(AB), CreateVector(A, point)) >= 0)\
                            and (DotProduct(GetNormalVector(BC), CreateVector(B, point)) >= 0)\
                            and (DotProduct(GetNormalVector(CA), CreateVector(C, point)) >= 0):
                        #print("inside!")
                        remove_keys.append(key2)
                    else:
                        #print("outside!")
                        pass
    for key in remove_keys:
        renderer.remove_render_object(key)

def KNN(K):
    render_objects = renderer.get_render_object()
    all_points = []
    #Finding all points, putting them in all_points list
    for key2 in render_objects:
        value2 = render_objects[key2]
        if value2["type"] == "Point":
            found_point = value2['vertices'][0]
            all_points.append(found_point)

    for x, check_point in enumerate(all_points): #Starting on point 1
        distance_and_point_list = []
        for point in all_points: #checking distance form point 1 compered to point n
            distance_and_point_list.append([GetDistance(check_point, point), point]) #distance, position
        distance_and_point_list = sorted(distance_and_point_list, key=lambda x: x[0])
        distance_and_point_list = distance_and_point_list[1:] #removing first element, which is 0, becuse compared to itself.
        distance_and_point_list = distance_and_point_list[:K] #Just the 5 first points
        for y, point in enumerate(distance_and_point_list):
            renderer.add_render_object("Line", [check_point, point[1]], "line" + str(x) + str(y), [0, 0, 0])

def SegmentTriangelCollision():
    render_objects = renderer.get_render_object()
    remove_keys = []
    for key1 in render_objects:
        value1 = render_objects[key1]
        if value1["type"] == "Triangle":
            # Searshing for Point
            for key2 in render_objects:
                value2 = render_objects[key2]
                if value2["type"] == "Line":
                    if lineSegmentCheck(value2, value1):
                        remove_keys.append(key2)
    for key in remove_keys:
        renderer.remove_render_object(key)

def lineSegmentCheck(line, triangle):

    #1. Seeing if points are on the right/left side of the segment.
    #Making Normal line
    oneSegmentPoint = line['vertices'][0]
    lineVector = CreateVector(oneSegmentPoint, line['vertices'][1])
    lineNormal = GetNormalVector(lineVector)

    #Making triangle vectors from origin, seeing if 90 degress
    triangle_points = triangle['vertices']
    A = triangle_points[0]
    B = triangle_points[1]
    C = triangle_points[2]
    p1 = CreateVector(oneSegmentPoint, A)
    p2 = CreateVector(oneSegmentPoint, B)
    p3 = CreateVector(oneSegmentPoint, C)

    AB = CreateVector(A, B)
    BC = CreateVector(B, C)
    CA = CreateVector(C, A)

    n1 = GetNormalVector(AB)
    n2 = GetNormalVector(BC)
    n3 = GetNormalVector(CA)

    ALine0 = CreateVector(A, line['vertices'][0])
    ALine1 = CreateVector(A, line['vertices'][1])
    BLine0 = CreateVector(B, line['vertices'][0])
    BLine1 = CreateVector(B, line['vertices'][1])
    CLine0 = CreateVector(C, line['vertices'][0])
    CLine1 = CreateVector(C, line['vertices'][1])

    if (DotProduct(lineNormal, p1) >= 0) \
            and (DotProduct(lineNormal, p2) >= 0) \
            and (DotProduct(lineNormal, p3) >= 0) \
            or (DotProduct(lineNormal, p1) <= 0) \
            and (DotProduct(lineNormal, p2) <= 0) \
            and (DotProduct(lineNormal, p3) <= 0):
                return False
    elif (DotProduct(n1, ALine0) < 0 and DotProduct(n1, ALine1) > 0) or (DotProduct(n1, ALine0) > 0 and DotProduct(n1, ALine1) < 0):
        return True
    elif (DotProduct(n2, BLine0) < 0 and DotProduct(n2, BLine1) > 0) or (DotProduct(n2, BLine0) > 0 and DotProduct(n2, BLine1) < 0):
        return True
    elif (DotProduct(n3, CLine0) < 0 and DotProduct(n3, CLine1) > 0) or (DotProduct(n3, CLine0) > 0 and DotProduct(n3, CLine1) < 0):
        return True
    else:
        return False

def Ortogonalprojection(u, v):
    k = DotProduct(u, v) / GetVectorLength(v)**2
    return VectorMultiplication(v, k)

def lineCircleCollision():
    render_objects = renderer.get_render_object()
    renderer.add_render_object("Line", [[100,400], [400,300]], "line9999", [0, 0, 0])
    line = render_objects["line9999"]
    circle = render_objects["circle1"]

    A = line['vertices'][0]
    B = line['vertices'][1]
    midPoint = circle['vertices'][0]
    radius = circle["radius"]

    AB = CreateVector(A, B)
    BA = CreateVector(B, A)
    v1 = DotProduct(AB, CreateVector(A, midPoint))
    v2 = DotProduct(BA, CreateVector(B, midPoint))

    if v1 > 0 and v2 > 0:
        #inside do the Ortogonalprojektionsvector.
        linePoint2midPoint = CreateVector(A, midPoint)
        o = Ortogonalprojection(AB, linePoint2midPoint)
        aaaa = GetVectorLength(CreateVector(AB, o))

        if aaaa < radius:
            print("collision!")
    elif v1 < 0:
        if GetDistance(midPoint, B) < radius:
            print("collision!")
    elif v2 < 0:
        if GetDistance(midPoint, A) < radius:
            print("collision!")



window = pyglet.window.Window(width=800, height=800)
renderer = Renderer(window.width,window.height) #Lin window created

#type, vertices, id, color
renderer.add_render_object("Circle", [(200,600), 100], "circle", [1,0,0])
renderer.add_render_object("Circle", [(200,300), 100], "circle1", [1,0,0])
#renderer.add_render_object("Triangle", [[300, 300], [700, 300], [700, 700]], "triangle1", [1,0,0])
renderer.add_render_object("Triangle", [[300, 300], [700, 300], [700, 700]], "triangle500", [1, 0, 0])
renderer.add_render_object("Point", [(700, 701)], "point500", [0, 0, 0])

GenerateAllPoints(num=100)

#print(renderer.get_render_object())
CircleCollision()
TriangleCollision()
#KNN(5)

SegmentTriangelCollision()
lineCircleCollision()
print(renderer.render_objects)
@window.event
def on_draw():
    window.clear()
    renderer.draw()

pyglet.app.run()


