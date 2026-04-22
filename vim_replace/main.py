from manim import *
from elements import *


class scene(Scene):
    """
    presentation of vim substitute command
    """

    def construct(self):
        self.add(grid, Dot())
        self.add(code_block(str=sx))
        self.wait()
        for k, v in subs.items():
            self.play(
                Create(
                    mobject=code_block(str=sx.replace(k, v)),
                    run_time=2
                )
            )
            self.wait()
