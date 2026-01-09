from manim import *


class Pith(Scene):
    def construct(self):
        sq = Square(side_length=5, stroke_color=GREEN, fill_opacity=0.75)
        self.play(Create(sq), run_time=3)
        self.wait()


class Testing(Scene):
    def construct(self):
        name = Tex("Sumaiiaa").to_edge(UL, buff=0.5)
        sq = Square(side_length=0.5, fill_color=BLUE, fill_opacity=0.5).shift(LEFT * 3)
        tri = Triangle().scale(0.6).to_edge(DR, buff=0.5)

        self.play(Write(name))
        self.play(DrawBorderThenFill(sq), run_time=2)
        self.play(Create(tri))
        self.wait()

        self.play(name.animate.to_edge(UR), run_time=2)
        self.play(sq.animate.scale(2), tri.animate.to_edge(DL), run_time=3)


class Getters_n_Setters(Scene):
    def construct(self):
        rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)
        circle = Circle().to_edge(DOWN)
        arrow = always_redraw(
            lambda: Line(start=rect.get_center(), end=circle.get_center()).add_tip()
        )
        self.play(Create(VGroup(rect, circle, arrow)))
        self.wait()
        self.play(rect.animate.to_edge(UR), circle.animate.to_edge(DL), run_time=2)
