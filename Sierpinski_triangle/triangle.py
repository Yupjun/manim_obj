from manim import *
import numpy as np
import random


# https://stackoverflow.com/questions/68493050/sample-uniformly-random-points-within-a-triangle
def uniform_triangle(u, v):
    s = random.random()
    t = random.random()
    in_triangle = s + t <= 1
    p = s * u + t * v if in_triangle else (1 - s) * u + (1 - t) * v
    return p


# Sierpinski triangle
class Triangle(Scene):
    def construct(self):
        colorList = [RED, GREEN, BLUE, YELLOW]
        triangle_point = [np.array([0,3,0]),np.array([-3,-3,0]),np.array([3,-3 ,0])]
        for points in triangle_point:
            point = Point(location=points,color=np.random.choice(colorList))
            self.add(point)
        init_point = uniform_triangle(
            triangle_point[1] - triangle_point[0],
            triangle_point[2] - triangle_point[0],
                    )
        first_point = Point(location=init_point,color=np.random.choice(colorList))
        self.add(first_point)
        for nums in range(5000):
            obj = random.choice(triangle_point)
            init_point += obj
            init_point =init_point/2
            if nums%2:
                picked_color = RED
            else:
                picked_color = BLUE
            point =  Point(location=init_point,color=picked_color)
            self.add(point)
