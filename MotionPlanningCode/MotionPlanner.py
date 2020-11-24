import json
from MotionPlanningCode.Renderer import Renderer
import pyglet

window = pyglet.window.Window(width=800, height=800)
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman', color=(0,255,255,255),
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
renderer = Renderer(window.width,window.height)
renderer.add_render_object("Circle", [(200,600), 100], "circle", [0,0,0])
#renderer.add_render_object("Triangle", "triangle2", [[100, 100], [300, 100], [700, 200]], color=(0,255,255,128))

@window.event
def on_draw():
    window.clear()
    renderer.draw()
    label.draw()

pyglet.app.run()


