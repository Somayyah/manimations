from manim import *
from elements import *


class linux_permissions(Scene):
    def frame_1(self):
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
        return {
            "intro": intro,
            "example": example,
            "p_sets": p_sets,
        }

    def construct(self):
        self.add(grid, Dot())
        elements = self.frame_1()
        self.add(
            Group(
                elements["intro"], 
                elements["example"], 
                *elements["p_sets"])
            )
