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

def TriangleCollision():
    renderer.add_render_object("Point", [(800,800)], "point500", [0, 0, 0])
    renderer.add_render_object("Triangle", [[300, 300], [700, 300], [700, 700]], "triangle500", [1,0,0])

    render_objects = renderer.get_render_object()
    point = render_objects["point500"]
    triangle = render_objects["triangle500"]


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

print(renderer.get_render_object())
CircleCollision(renderer.get_render_object())
TriangleCollision(renderer.get_render_object())

@window.event
def on_draw():
    window.clear()
    renderer.draw()
    label.draw()

pyglet.app.run()


