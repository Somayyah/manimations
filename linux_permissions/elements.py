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

ls_output = """> ls -l 
total 136
-rw-r--r-- 1 watari watari     46 Dec 30 22:34 README.md"""
permissions_example = "-rw-r--r--"
permission_sets = ["user", "group", "other"]
bits = ["d", "r", "w", "x", "-", "s", "t"]

def frame_1():
    intro = Code(
        code_string=ls_output,
        tab_width=4,
        formatter_style="fruity",
        background="window",
        language="bash",
        paragraph_config={"font_size": 50, "font": "Noto Sans Mono"},
        add_line_numbers=False,
    )

    example = Text(
        permissions_example,
    )

    p_sets = [Text(i) for i in permission_sets]

    return [intro, example, p_sets]
