from big_ol_pile_of_manim_imports import *

class MovingPoint(GraphScene):
    CONFIG = { 
        'graph_origin': ORIGIN
    }

    def construct(self): 
        self.setup_axes()
        point = Dot(self.coords_to_point(0, 0))
        self.add(point)
        self.add(ContinuallyMove(point))
        self.wait(3)


class ContinuallyMove(UpdateFromFunc):

    def update_mobject(self, dt): 
        new_point = point + RIGHT*dt
        self.point.shift(new_point)

    def __init__(self, point):
        self.point = point
        UpdateFromFunc.__init__(self, self.point, self.update_mobject)
