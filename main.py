from manim import *

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8.0
config.frame_width = 14.222
grid = NumberPlane(
    x_range=[-config.frame_width / 2, config.frame_width / 2, 1],
    y_range=[-config.frame_height / 2, config.frame_height / 2, 1],
    background_line_style={
        "stroke_color": BLUE_E,
        "stroke_width": 3,
        "stroke_opacity": 0.4
    }
)
class Pith(Scene):
    def construct(self):
       # i = 3
        self.add(grid, Dot())

        rect = Rectangle(color=WHITE, height=1, width=1).to_edge(UL)
        circle = Circle(radius= 1).to_edge(DR)
        arrow = always_redraw(lambda : Line(start= rect.get_center(), end=circle.get_center()).add_tip())
        # poly = always_redraw(lambda : Star(color=PURPLE, n=i))

        self.play(Create(VGroup(rect, circle, arrow)))
        for i in range(3, 30, 3):
            self.play(rect.animate.to_edge(UR).scale(2), circle.animate.scale(2).to_edge(DL))
            self.play(rect.animate.to_edge(UL).scale(0.5), circle.animate.scale(0.5).to_edge(DR))
        self.wait()