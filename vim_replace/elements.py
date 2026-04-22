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
        "stroke_opacity": 0.4,
    },
)

sx = ':[range]s/{pattern}/{replacement}/[flags] [count]'
subs = {
    "[range]": '%', 
    '{pattern}': "^\*\+", 
    "{replacement}": "\=len(submatch(0))",
    "[flags] [count]": ""
}

def code_block(str):
    return Code(code_string=str, add_line_numbers=False).scale(1.1)