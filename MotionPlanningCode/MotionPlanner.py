import json
from MotionPlanningCode.Renderer import Renderer
import pyglet
import random
from pyglet.window import key, mouse

def reciveData():
    with open('obstaclesCircles.json') as json_file:
        data = json.load(json_file)
        # print(data)

def GenerateAllPoints(num=100):
    for x in range(num):
        random_x = random.randint(0, 700)
        random_y = random.randint(0, 700)
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
            renderer.add_render_object("Line", [check_point, point[1]], "line" + str(x) + str(y), [0.8, 0.8, 0.8])

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

def SegmentCircleCollision():
    render_objects = renderer.get_render_object()
    remove_keys = []
    for key1 in render_objects:
        value1 = render_objects[key1]
        if value1["type"] == "Circle":
            # Searshing for Point
            for key2 in render_objects:
                value2 = render_objects[key2]
                if value2["type"] == "Line":
                    if SegmentCircleCollisionCheck(value2, value1):
                        remove_keys.append(key2)
    for key in remove_keys:
        renderer.remove_render_object(key)
def SegmentCircleCollisionCheck(line, circle):

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
        o = Ortogonalprojection(linePoint2midPoint, AB)
        distanceSegmnetCircle = GetVectorLength(CreateVector(linePoint2midPoint, o))

        if distanceSegmnetCircle < radius:
            return True
    elif v1 < 0:
        if GetDistance(midPoint, B) < radius:
            return True
    elif v2 < 0:
        if GetDistance(midPoint, A) < radius:
            return True

def AddNeigborToPoint():
    render_objects = renderer.get_render_object()
    for key1 in render_objects:
        point = render_objects[key1]
        if point["type"] == "Point":
            # Searshing for Point
            for key2 in render_objects:
                line = render_objects[key2]
                if line["type"] == "Line":
                    if point['vertices'][0] == line['vertices'][0]: #The lines first point is at the same position
                        point["neighbors"].append(line['vertices'][1]) #The other point on the line.
                    elif point['vertices'][0] == line['vertices'][1]:  # The lines first point is at the same position
                        point["neighbors"].append(line['vertices'][0])  # The other point on the line.

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys(): #loop every cameFrom
        current = cameFrom[current]
        total_path.insert(0, current) #Add element on fist position
    return total_path


def AStar(start, goal, h=GetDistance):


    render_objects = renderer.get_render_object()

    node_and_neighbors = {} #pointpos: [neighborpos, neighborpos] (700,700): [(600,600),(500,500)]
    for point_key in render_objects:
        point = render_objects[point_key]
        if point["type"] == "Point":
            node_and_neighbors[point['vertices'][0]] = point["neighbors"]

    #Just for Debug
    #start = list(node_and_neighbors.keys())[0]
    #goal = list(node_and_neighbors.keys())[-1]
    print("start:", start, "goal:", goal)

    openSet = [start]
    cameFrom = {} #List positions in order

    gScore = {} #{b:5} Den totala kostnaden att komma till b, inte garanterat.
    fScore = {} #how short a path from start to finish
    for point_key in node_and_neighbors:
            gScore[point_key] = float('inf')
            fScore[point_key] = float('inf')

    gScore[start] = 0
    fScore[start] = h(start, goal)

    while openSet:
        #Smallest value in openset
        current = min(openSet, key=fScore.get)

        if current == goal:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        for neighbor in node_and_neighbors[current]:
            tentative_gScore = gScore[current] + h(current, neighbor)
            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + h(neighbor, goal)
                if neighbor not in openSet:
                    openSet.append(neighbor)
    return []

def MakePathLines(path):
    for x in range(len(path) - 1):
        renderer.add_render_object("Line", [path[x], path[x + 1]], "pathLine" + str(x), [0,0, 1])
        #pass




window = pyglet.window.Window(width=800, height=710)
renderer = Renderer(window.width,window.height) #Lin window created

#type, vertices, id, color
renderer.add_render_object("Circle", [(200,600), 100], "circle", [1,0,0])
renderer.add_render_object("Circle", [(200,300), 100], "circle1", [1,0,0])
renderer.add_render_object("Triangle", [[300, 300], [700, 300], [600, 600]], "triangle500", [1, 0, 0])

num_points = 100
GenerateAllPoints(num=num_points)
CircleCollision()
TriangleCollision()

start_point = ()
end_point = ()
click_num = 0

@window.event
def on_draw():
    window.clear()
    renderer.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    global num_points, start_point, end_point, click_num
    if button == pyglet.window.mouse.LEFT and click_num == 0:
        renderer.add_render_object("Point", [(x, y)], "startpoint" + str(num_points), [0, 0, 1])
        start_point = (x, y)

        num_points += 1
        click_num += 1

    elif button == pyglet.window.mouse.LEFT and click_num == 1:
        renderer.add_render_object("Point", [(x, y)], "startpoint" + str(num_points), [1, 0, 0])
        end_point = (x, y)

        num_points += 1
        click_num = 0
    CircleCollision()
    TriangleCollision()

@window.event
def on_key_press(symbol, modifiers):
    global renderer
    render_objects = renderer.render_objects
    remove_keys = []

    if symbol == key.SPACE:
        #Remove all lines
        for key1 in render_objects:
            point = render_objects[key1]
            if point["type"] == "Line":
                remove_keys.append(key1)
    for key1 in remove_keys:
        renderer.remove_render_object(key1)
    CircleCollision()
    TriangleCollision()
    KNN(5)  # Spara punkt och denns grannar. [punkt, [grannar]]
    SegmentTriangelCollision()
    SegmentCircleCollision()
    AddNeigborToPoint()
    path = AStar(start=start_point, goal=end_point)
    print(path)
    MakePathLines(path)



pyglet.app.run()


