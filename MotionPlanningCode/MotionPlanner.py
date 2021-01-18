import json
from MotionPlanningCode.Renderer import Renderer
import pyglet
import random

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

def CircleCollision(render_objects):
    #Searshing for Circle
    for key1 in render_objects:
        value1 = render_objects[key1]
        if value1["type"] == "Circle":
    #Searshing for Point
            for key2 in render_objects:
                value2 = render_objects[key2]
                if value2["type"] == "Point":
    #Calculating distance
                    distance = GetDistance(value1['vertices'][0], value2['vertices'][0]) #GetDistance(origo_Circle, origo_Point)
                    circle_radius = value1['vertices'][1]
                    if distance < circle_radius:
                        renderer.remove_render_object(key2)

def CreateVector(a,b):
    return [b[0]-a[0],b[1]-a[1]] #[x1-x2, y1-y2]

def GetNormalVector(a):
    return [-a[1], a[0]] #[-y,x]

def DotProduct(a,b):
    return a[0]*b[0]+a[1]*b[1]

def TriangleCollision(render_objects):

    renderer.add_render_object("Triangle", [[300, 300], [700, 300], [700, 700]], "triangle500", [1,0,0])
    renderer.add_render_object("Point", [(600, 500)], "point500", [0, 0, 0])

    point = render_objects["point500"]['vertices'][0]
    triangle_points = render_objects["triangle500"]['vertices']

    AB = CreateVector(triangle_points[0], triangle_points[1])
    BC = CreateVector(triangle_points[1], triangle_points[2])
    CA = CreateVector(triangle_points[2], triangle_points[0])

    print(DotProduct(GetNormalVector(AB), point))
    print(DotProduct(GetNormalVector(BC), point))
    print(DotProduct(GetNormalVector(CA), point))

    if (DotProduct(GetNormalVector(AB), point) >= 0) and (DotProduct(GetNormalVector(AB), point) >= 0) and (DotProduct(GetNormalVector(AB), point) >= 0):
        print("inside!")
        #renderer.remove_render_object("point500")
    else:
        print("outside!")







with open('obstaclesCircles.json') as json_file:
    data = json.load(json_file)

#print(data)

window = pyglet.window.Window(width=800, height=800)
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman', color=(0,255,255,255),
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
renderer = Renderer(window.width,window.height) #Lin window created

#type, vertices, id, color
renderer.add_render_object("Circle", [(200,600), 100], "circle", [1,0,0])
renderer.add_render_object("Circle", [(200,300), 100], "circle1", [1,0,0])
#renderer.add_render_object("Triangle", [[300, 300], [700, 300], [700, 700]], "triangle1", [1,0,0])

GenerateAllPoints(num=100)

#print(renderer.get_render_object())
#CircleCollision(renderer.get_render_object())
TriangleCollision(renderer.get_render_object())

@window.event
def on_draw():
    window.clear()
    renderer.draw()
    label.draw()

pyglet.app.run()


