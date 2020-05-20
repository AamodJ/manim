from big_ol_pile_of_manim_imports import *
"""Update for newer version of manim"""

class DrawAnAxis(Scene):
    CONFIG = {"plane_kwargs" : {
            "x_line_frequency" : 2,
            "y_line_frequency" : 3
        }
    }
 
    def construct(self):
        my_plane = NumberPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels())
        self.add(my_plane)
        self.wait()


class SimpleField(Scene):
    CONFIG = {
        "plane_kwargs" : {
            "color" : RED
        },
    }

    def construct(self):
        plane = NumberPlane(**self.plane_kwargs) #Create axes and grid
        plane.add(plane.get_axis_labels()) #add x and y label
        self.add(plane) #Place grid on screen
 
        points = [x*RIGHT+y*UP for x in np.arange(-3,4,1) for y in np.arange(-3,4,1)] #List of vectors pointing to each grid point

        vec_field = [] #Empty list to use in for loop
        for point in points:
            field = 0.9*LEFT + 0.5*UP #Constant field up and to right
            result = Vector(field).shift(point) #Create vector and shift it to grid point
            vec_field.append(result) #Append to list

        
        draw_field = VGroup(*vec_field) #Pass list of vectors to create a VGroup
 
        self.play(ShowCreation(draw_field)) #Draw VGroup on screen


class FieldWithAxes(Scene):
    CONFIG = {
        "plane_kwargs" : {
            "color" : RED_B
         },
         "point_charge_loc" : 0*RIGHT + 0*UP,
         'x_line_frequency' : 10,
         'y_line_frequency' : 10
    }
    
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines_fade(.9)
        plane.add(plane.get_axis_labels())
        self.play(ShowCreation(plane))

        points = [x*RIGHT+y*UP for x in np.arange(-9,9,1) for y in np.arange(-5,5,1)]
        vec_field = [self.calc_field(point) for point in points]
 
        field = VGroup(*vec_field)
 
        self.play(ShowCreation(field))
        self.wait(1)


    def calc_field(self, point):
        x = point[0]
        y = point[1]
        #field = np.array((-y,x,0))/math.sqrt(x**2+y**2) #for circular field
        field = np.array(( -2*(y%2)+1 , -2*(x%2)+1 , 0 ))/3
        return Vector(field).shift(point)







