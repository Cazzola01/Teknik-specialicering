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
    #executor = ProcessPoolExecutor(max_workers=3)
    with ProcessPoolExecutor() as executor:
        for x in range(100):
            pass
            #task1 = executor.submit(task)


if __name__ == '__main__':
    main()
    window = pyglet.window.Window(width=666, height=666)
    renderer = Renderer(window.width, window.height)
    #time.sleep(4)
    

@window.event
def on_draw():
    window.clear()
    renderer.draw()