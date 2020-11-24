import pyglet
from MotionPlanningCode.Renderer import Renderer
from pyglet.window import key
import json

class MotionPlanner(pyglet.window.Window):

    def __init__(self):
        width = 1280 #ersätt med kod för att ladda in width
        height = 720#ersätt med kod för att ladda in height
        super(MotionPlanner, self).__init__(height=height, width=width, resizable=True)
        self.renderer = Renderer(width, height)
        self.set_minimum_size(100, 100)

    def on_draw(self):
        self.renderer.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_key_press(self, symbol, modifiers):
        pass



if __name__ == "__main__":
    app = MotionPlanner()
    pyglet.app.run()