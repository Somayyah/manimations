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

parts = [
    ":",
    "[range]",
    "s/",
    "{pattern}",
    "/",
    "{replacement}",
    "/",
    "[flags] [count]",
]

replacements = {
    1: "%", # [range]
    3: r"^\*\+", # {pattern}
    5: r"\=len(submatch(0))", # {replacement}
    7: "", # [flags] [count]
}