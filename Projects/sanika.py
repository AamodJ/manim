#from big_ol_pile_of_manim_imports import *
from manimlib.imports import *

class hello(Scene):
    def construct(self) :


        #img = ImageMobject('nikka.jpg')
        #img.scale(2)  # Resize to be twice as big

        #elf.play(ShowCreation(img))  # Display the image
        text = ['Hello', 'Sanika', ':3']
        t = TextMobject(*text)
        t.set_color_by_gradient("#33ccff","#ff00ff")
        t.shift(3*DOWN)
        self.wait(1)
        self.play(Write(t))
        self.wait(1)
        