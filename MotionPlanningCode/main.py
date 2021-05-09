import MotionPlanningCode.renderer as renderer
import MotionPlanningCode.collision as collision
import MotionPlanningCode.vector as vector
import json
import pyglet
import random
from pyglet.window import key, mouse


# Reading JSON file, plotting objects, returning settings
# O(len("obstacles"))
def read_file():
    # Loading JSON file
    with open('obstacles.json') as json_file:
        data = json.load(json_file)
    # Plotting shapes
    for value in data["obstacles"].values():
        if value["type"] == "circle":
            renderer.add_circle(position=value["position"], radius=value["radius"], color=value["color"])
        elif value["type"] == "triangle":
            renderer.add_triangle(vertices=value["vertices"], color=value["color"])
    # Function returning: width, height and k
    return data["settings"]["width"], data["settings"]["height"], data["settings"]["k"], data["settings"]["point num"]


# plotting random points all over screen.
# O(num)
def generate_all_points(num=100):
    for x in range(num):
        random_x = random.randint(0, width)
        random_y = random.randint(0, height)
        renderer.add_point(position=(random_x, random_y), color=[0, 0, 0])


# comparing every point to every point and making a line between the k closest ones
# O(len(renderer.points) * (len(renderer.points) + (k + 1)))
def knn(k=5):
    for point in renderer.points:
        pos_dist = []
        for compare_point in renderer.points:
            pos_dist.append((compare_point.position, vector.get_distance(point.position, compare_point.position)))

        pos_dist.remove(min(pos_dist, key=lambda x: x[1]))  # value is 0, because compared to itself.

        for i in range(k):
            closest_pos = pos_dist.pop(pos_dist.index(min(pos_dist, key=lambda x: x[1])))[0]  # pop smallest distance
            renderer.add_segment(start=point.position, end=closest_pos, color=[0.8, 0.8, 0.8])


# if any segment contains a specific point, it means the other side of the segment is neighbor.
# O(len(renderer.points) * len(renderer.segments))
def add_neighbors_to_points():
    for point in renderer.points:
        for segment in renderer.segments:
            if point.position == segment.start:
                point.neighbors.append(segment.end)
            elif point.position == segment.end:
                point.neighbors.append(segment.start)


# after a_star is finished. Returning points in right orders.
# O(len(came_from))
def reconstruct_path(came_from, current):  # n is number of elements in come_from. O(n)
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.insert(0, current)  # Add element on first position
    return total_path


# Calculation the shortest path in a web containing multiple connected lines.
# O(len(renderer.points) * len(renderer.segments))
def a_star(start, goal, h=vector.get_distance):
    open_set = [start]
    came_from = {}
    g_score = {}
    f_score = {}
    for point in renderer.points:
        g_score[point.position] = float('inf')
        f_score[point.position] = float('inf')
    g_score[start] = 0
    f_score[start] = h(start, goal)

    while open_set:
        # Smallest value in open_set
        current = min(open_set, key=f_score.get)
        if current == goal:
            return reconstruct_path(came_from, current)

        open_set.remove(current)

        # Finding index where point.position == current position
        for x, point in enumerate(renderer.points):
            if point.position == current:
                index = x
                break

        for neighbor in renderer.points[index].neighbors:
            tentative_g_score = g_score[current] + h(start, goal)
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + h(neighbor, goal)
                if neighbor not in open_set:
                    open_set.append(neighbor)
    return []


# Plotting the path lines.
# O(len(path))
def make_path_lines(path):
    for x in range(len(path) - 1):
        renderer.add_segment(start=path[x], end=path[x + 1], color=[0, 0, 1])


# O(1)
if __name__ == '__main__':
    width, height, k, point_num = read_file()
    window = pyglet.window.Window(width=width, height=height)
    # Randomizing points
    generate_all_points(num=point_num)
    collision.point_circle_collision()
    collision.point_triangle_collision()

    # global variables
    start_point = (0, 0)
    end_point = (0, 0)
    place_start_point = True


# Drawing next fame.
@window.event
def on_draw():
    window.clear()
    renderer.draw()


# user presses mouse to place start and end point
# O(1)
@window.event
def on_mouse_press(x, y, button, modifiers):
    global start_point, end_point, place_start_point
    # Place start_point
    if button == pyglet.window.mouse.LEFT and place_start_point:
        renderer.add_point(position=(x, y), color=[0, 0, 1])
        start_point = (x, y)
        place_start_point = False  # ready to place end_point

    # Place end_point
    elif button == pyglet.window.mouse.LEFT and not place_start_point:
        renderer.add_point(position=(x, y), color=[1, 0, 0])
        end_point = (x, y)
        place_start_point = True  # ready to place start_point again

    # Checking so new point not colliding
    collision.point_circle_collision()
    collision.point_triangle_collision()


# user presses space bar to calculate shortest past between start and end point
# O(1)
@window.event
def on_key_press(symbol, modifiers):
    # remove old segments
    if symbol == key.SPACE:
        renderer.segments.clear()
    knn(k)  # connecting new lines
    collision.segment_triangle_collision()
    collision.segment_circle_collision()
    add_neighbors_to_points()
    path = a_star(start=start_point, goal=end_point)
    print(path)
    make_path_lines(path)  # Plotting the path lines


pyglet.app.run()
