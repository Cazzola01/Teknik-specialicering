import json
from MotionPlanningCode.Renderer import Renderer
import pyglet
import random

with open('obstaclesCircles.json') as json_file:
    data = json.load(json_file)

print(data)

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

renderer.add_render_object("Circle", [(200,600), 100], "circle", [1,0,0])
renderer.add_render_object("Point", GenerateRandomTuplePoints(pointNum=100), "points", [0,0,0])

@window.event
def on_draw():
    window.clear()
    renderer.draw()
    label.draw()

pyglet.app.run()


