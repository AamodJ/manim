# from big_ol_pile_of_manim_imports import *
from manimlib.imports import *
"""
Update it for newer version of manim
"""
class MovingCharge(Scene):
    CONFIG = {
        'plane_kwargs': {
            'color': RED_B
        },
        'point_charge_loc': 0*RIGHT + 0*UP,
        'always_update_mobjects': True
    }

    def construct(self): 
        plane = NumberPlane(**self.plane_kwargs)
        plane.add(plane.get_axis_labels())
        self.play(ShowCreation(plane))

        points = [x*RIGHT + y*UP for x in np.arange(-9, 9, 1) for y in np.arange(-5, 5, 1) if x != 0 or y != 0]
        field = [*[self.calc_field(point) for point in points]]

        source_charge = self.Positron().move_to(self.point_charge_loc)
        self.play(FadeIn(source_charge))
        self.play(ShowCreation(VGroup(*field)))
        self.add(ContinualChargeUpdate(source_charge))
        self.wait(3)
        

    def calc_field(self, point):
        x, y = point[:2]
        Rx, Ry = self.point_charge_loc[:2]

        r = math.sqrt((x - Rx)**2 + (y - Ry)**2)
        efield = (point - self.point_charge_loc)/r**2

        return Vector(efield).shift(point)
    

    class Positron(Circle):
        CONFIG = {
            "radius" : 0.2,
            "stroke_width" : 3,
            "color" : RED,
            "fill_color" : RED,
            "fill_opacity" : 0.5,
        }
        def __init__(self, **kwargs):
            Circle.__init__(self, **kwargs)
            plus = TexMobject("+")
            plus.scale(0.7)
            plus.move_to(self)
            self.add(plus)

class ContinualChargeUpdate(Animation):
    def __init__(self, charge):
        self.charge = charge
        Animation.__init__(self, self.charge)

    def update_mobjects(self, dt): 
        self.charge.accelaration = np.array((1, 0, 0))
        self.charge.velocity += self.charge.accelaration * dt
        
        self.charge.shift(self.charge.velocity * dt)

        