from manimlib.imports import *

class Example(Scene):
    def construct(self):
        sphere = Sphere()

        self.wait(1)
        self.add(sphere)
        self.wait(1)