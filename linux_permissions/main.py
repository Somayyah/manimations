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

        return {
            "intro": intro,
            "permissions_bits": permissions_bits,
            "permission_sets": permission_sets,
        }

    def construct(self):
        self.add(grid, Dot())
        elements = self.frame_1()
        self.add(elements["intro"].scale(0.5).to_edge(UP).to_edge(LEFT))
