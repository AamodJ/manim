from big_ol_pile_of_manim_imports import *
"""Update for newer version of manim"""
class Parabolas(GraphScene): 
    CONFIG = {
        'x_min': -10,
        'y_min': -10,
        'x_max': 10,
        'y_max': 10,
        'function1': lambda x: 2 * x**2,
        'function2': lambda x: 0.125 * x**2,
        'graph_origin': ORIGIN
    }

    def construct(self):
        self.setup_axes()

        func1_graph = self.get_graph(self.function1, BLUE)
        func1_label = self.get_graph_label(func1_graph, label='2x^{2}')

        func2_graph = self.get_graph(self.function2, GREEN)
        func2_label = self.get_graph_label(func2_graph, label='0.125x^{2}')

        point_on_func1 = Dot(self.coords_to_point(1, self.function1(1)))
        point_on_func2 = Dot(self.coords_to_point(3, self.function2(3)))

        self.play(ShowCreation(func1_graph), ShowCreation(func1_label))
        self.play(ShowCreation(point_on_func1))
        self.wait(1)

        self.play(Transform(func1_graph, func2_graph), Transform(func1_label, func2_label), \
                            Transform(point_on_func1, point_on_func2))
        self.wait(1)