import json
from MotionPlanningCode.Renderer import Renderer
import pyglet
import random
from pyglet.window import key, mouse
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os
import time

def task():
    print("Executing our Task on Process {}".format(os.getpid()))

def main():
    executor = ProcessPoolExecutor(max_workers=3)
    with ProcessPoolExecutor() as executor:
        for x in range(100):
            task1 = executor.submit(task)

#@window.event
def on_draw():
    window.clear()
    renderer.draw()

if __name__ == '__main__':
    #main()
    window = pyglet.window.Window(width=666, height=666)
    renderer = Renderer(window.width, window.height)

    # Loading settings from Json file
    with open('obstaclesCircles.json') as json_file:
        data = json.load(json_file)

    # Add Obsticles from file. "n" is number of obsticles. O(n)
    for key1 in data["obstacles"]:
        value1 = data["obstacles"][key1]
        if value1["type"] == "Circle":
            # type, vertices, id, color
            renderer.add_render_object(value1["type"], [tuple(value1["center"]), value1["radius"]], value1["id"],                           [1, 0, 0])
        elif value1["type"] == "Triangle":
            renderer.add_render_object(value1["type"], value1["vertices"], value1["id"], [1, 0, 0])
        elif value1["type"] == "Quad":
            renderer.add_render_object(value1["type"], value1["vertices"], value1["id"], [1, 0, 0])

    on_draw()
    print("running 1 time")
    print(renderer.render_objects)
    pyglet.app.run()

print("running 5 times")
