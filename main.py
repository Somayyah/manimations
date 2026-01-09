from manim import *

class Pith(Scene):
    def construct(self):
       sq = Square(
        side_length=5, stroke_color=GREEN, fill_opacity=0.75
        )
       self.play(Create(sq), run_time = 3)
       self.wait()

class Testing(Scene):
    def construct(self):
        name = Tex("Sumaiiaa").to_edge(UL, buff=0.5)
        sq = Square(side_length=0.5).shift(LEFT*3)
        tri = Triangle().scale(0.6).to_edge(DR)

        self.play(Write(name))