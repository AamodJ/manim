from big_ol_pile_of_manim_imports import *

class TestScene(Scene): 
    def construct(self): 
        func = lambda x: x
        text = TextMobject('Mod')
        self.play(ShowCreation(text))
        self.wait(1)
        self.add(self.TestUpdater(func, text))


    class TestUpdater(UpdateFromAlphaFunc): 
        def __init__(self, alpha, text): 
            self.alpha = alpha
            self.text = text