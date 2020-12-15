import json
from MotionPlanningCode.Renderer import Renderer
import pyglet
import random

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

def GenerateRandomTuplePoints(pointNum=100):
    randomxlist = random.sample(range(0, 800), pointNum)
    randomylist = random.sample(range(0, 800), pointNum)

    pointList = []
    for x in range(pointNum):
        tuplePoint = (randomxlist[x], randomylist[x])
        pointList.append(tuplePoint)
    return pointList

def CheckCollision(render_objects):
    all_points_pos = render_objects["points"]["vertices"]
    print(all_points_pos)

    print(render_objects)
    print(render_objects.values())

    for key in render_objects:
        value = render_objects[key]
        if value["type"] == "Circle":
            for point_pos in all_points_pos:
                # Do distance math
                x1 = point_pos[0]
                y1 = point_pos[1]
                value_pos = value["vertices"][0]
                value_radius = value["vertices"][1]
                x2 = value_pos[0]
                y2 = value_pos[1]
                distance = ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
                print(distance)
                if (distance < value_radius):
                    renderer.remove_render_object(key)
                    #pass

#type, vertices, id, color
renderer.add_render_object("Circle", [(200,600), 100], "circle", [1,0,0])
renderer.add_render_object("Point", GenerateRandomTuplePoints(pointNum=100), "points", [0,0,0])
CheckCollision(renderer.get_render_object())




@window.event
def on_draw():
    window.clear()
    renderer.draw()
    label.draw()

pyglet.app.run()


