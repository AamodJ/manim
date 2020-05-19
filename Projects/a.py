# from big_ol_pile_of_manim_imports import *
from manimlib.imports import *
class example(Scene) :
    def construct(self) :
        text = TextMobject('Hello Vedikaaaaaa')
        t = TextMobject(':3')
        l = VGroup(text, t)
        l.set_color_by_gradient("#33ccff", "#ff00ff")
        l[1].shift(DOWN)
        self.wait(1)
        self.play(Write(l))
        self.wait(1)