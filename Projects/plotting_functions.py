from big_ol_pile_of_manim_imports import *

class Functions(GraphScene) :
    CONFIG = {
        'x_min': -10, 
        'x_max': 10, 
        'y_min': -1.5, 
        'y_max': 1.5, 
        'x_labeled_nums': range(-10, 11, 2),
        'function_color': RED,  
        'graph_origin': ORIGIN, 
        'axes_color': GREEN
    }
    
    def construct(self) :
        self.setup_axes(animate=True)
        
        func_graph = self.get_graph(self.func1, self.function_color)
        func_graph2 = self.get_graph(self.func2)

        graph_lab = self.get_graph_label(func_graph, label='\\cos(x)')
        graph_lab2 = self.get_graph_label(func_graph2, label='|\\cos(x)|', x_val=-10, direction=UP)


        vert_line = self.get_vertical_line_to_graph(PI, func_graph, color=YELLOW)
        vert_line2 = self.get_vertical_line_to_graph(PI, func_graph2, color=YELLOW)




        point = Dot(self.coords_to_point(PI, self.func1(PI)))
        post_point = Dot(self.coords_to_point(PI, self.func2(PI)))



        point_label = TextMobject("x = Π")
        label_coords = self.input_to_graph_point(PI, func_graph)
        point_label.next_to(label_coords, RIGHT+DOWN)

        post_point_label = TextMobject('x = Π')
        label_coords = self.input_to_graph_point(PI, func_graph2)
        post_point_label.next_to(label_coords, RIGHT+UP)


        self.play(ShowCreation(func_graph, rate=0.5), Write(graph_lab))
        self.wait(0.1)
        self.play(ShowCreation(vert_line), Write(point_label), ShowCreation(point))
        self.wait(0.3)
        self.play(Transform(func_graph, func_graph2), Transform(graph_lab, graph_lab2), Transform(vert_line, vert_line2), Transform(point_label, post_point_label), Transform(point, post_point))
        self.wait(0.1)

    
    def func1(self, x) :
        return np.cos(x)

    def func2(self, x) :
        return abs(np.cos(x))