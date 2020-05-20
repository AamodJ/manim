import math
from manimlib.imports import *

"""
Fix the code. It doesn't give a correct graph 
"""


class ExampleApproximation(GraphScene):
    CONFIG = {
        "function": lambda x: 1 / (1 - x),
        "function_color": BLUE,
        "taylor": [lambda x: 1, lambda x: x,
                   lambda x: 1 + x + x**2,
                   lambda x: 1 + x + x**2 + x**3,
                   lambda x: 1 + x + x**2 + x**3 + x**4,
                   lambda x: 1 + x + x**2 + x**3 + x**4 + x ** 5,
                   lambda x: 1 + x + x**2 + x**3 + x**4 + x ** 5 + x ** 6],
        "center_point": 0,
        "approximation_color": GREEN,
        "x_min": -10,
        "x_max": 10,
        "y_min": -10,
        "y_max": 10,
        "graph_origin": ORIGIN,
        "x_labeled_nums": range(-10, 11, 2),
        "y_labeled_nums": range(-10, 11, 2)

    }


    def construct(self):
        self.setup_axes(animate=True)


        func_graph = self.get_graph(self.function, self.function_color)
        #func_label = self.get_graph_label(func_graph, label='e^{x}')
        approx_graphs = [self.get_graph(f,self.approximation_color) for f in self.taylor]
        #taylor_labels = [self.get_graph_label(approx_graphs[i] for i in range(len(approx_graphs)))]
        

        term_num = [TexMobject("n = " + str(n), aligned_edge=TOP) for n in range(0, 8)]
        [t.to_edge(BOTTOM, buff=SMALL_BUFF) for t in term_num]

        term = TexMobject("")
        term.to_edge(BOTTOM, buff=SMALL_BUFF)

        approx_graph = VectorizedPoint(self.input_to_graph_point(self.center_point, func_graph))

        self.play(ShowCreation(func_graph))
        for n, graph in enumerate(approx_graphs):
            self.play(Transform(approx_graph, graph, run_time=1.5), Transform(term,term_num[n]))
            # self.wait(0.1)