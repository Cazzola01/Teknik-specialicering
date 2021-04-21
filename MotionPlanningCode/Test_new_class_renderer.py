from MotionPlanningCode.Renderer import Renderer
import pyglet

window = pyglet.window.Window(width=800, height=800)
renderer = Renderer()

renderer.add_point(position=(300, 300), color=[0.7, 0.7, 0])
renderer.add_circle(position=(400, 400), radius=100, color=[0.5, 0, 0])
renderer.add_segment(start=(200, 200), end=(400, 170), color=[0, 0, 1])
renderer.add_triangle(vertex_0_position=(100, 100), vertex_1_position=(150, 170), vertex_2_position=(200, 70),
                      color=[0.5, 0.5, 0.5])


@window.event
def on_draw():
    window.clear()
    renderer.draw()


pyglet.app.run()
