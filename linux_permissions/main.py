from manim import *
from elements import *

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

class linux_permissions(Scene):
    def frame_1(self):
        self.add(intro.scale(0.3))

    def construct(self):
        self.add(grid, Dot())
        self.frame_1()
        
        
