# from big_ol_pile_of_manim_imports import *
from manimlib.imports import *

class s(ThreeDScene):
    CONFIG = {
        "plane_kwargs": {
            "color": RED_B
        },
        "point_charge_loc": 0 * RIGHT + 0 * UP + 0 * OUT,
    }
    def construct(self):
        self.set_camera_orientation(0, -np.pi/2)
        sphere = Sphere()
        plane = NumberPlane(**self.plane_kwargs)
        plane.add(plane.get_axis_labels())
        self.play(ShowCreation(plane))
        self.wait(0.1)
        self.move_camera(0.8*np.pi/2, -0.45*np.pi)
        self.begin_ambient_camera_rotation()
        self.play(ShowCreation(sphere))
        self.wait(4)

class ExampleThreeD(ThreeDScene):
    CONFIG = {
        "plane_kwargs" : {
            "color" : RED_B
        },
        "point_charge_loc" : 0*RIGHT+0*UP+0*OUT,
        }
    def construct(self):
        self.set_camera_orientation(0, -np.pi/2)
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)
 
        field2D = VGroup(*[self.calc_field2D(x*RIGHT+y*UP) for x in np.arange(-9,9,1) for y in np.arange(-5,5,1)])

        field3D = VGroup(*[self.calc_field3D(x*RIGHT+y*UP+z*OUT) for x in np.arange(-9,9,1) for y in np.arange(-5,5,1) for z in np.arange(-5, 5, 1)])

 
        self.play(ShowCreation(field3D))
        self.wait()
        self.move_camera(0.8*np.pi/2, -0.45*np.pi)
        self.begin_ambient_camera_rotation()
        self.wait(6)
 
    def calc_field2D(self,point):
        x,y,z = point
        Rx,Ry,RZ = self.point_charge_loc
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**2
        return Vector(efield).shift(point)

    def calc_field3D(self,point):
        x,y,z = point
        #Rx,Ry, Rz = self.point_charge_loc
        #r = math.sqrt((x-Rx)**2 + (y-Ry)**2 + (z - Rz)**2)
        efield = np.array((-y,x,z))/math.sqrt(x**2+y**2+z**2)
        return Vector(efield).shift(point)