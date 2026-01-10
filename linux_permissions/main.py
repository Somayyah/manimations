from manim import *
from elements import *

class linux_permissions(Scene):

    def construct(self):
        self.add(grid, Dot())
        intro, example, p_sets = frame_1()
        self.play(
            Create(
                VGroup(
                    intro.scale(0.3).to_edge(UL, buff=0.3),
                    example.scale(0.3).next_to(intro, DOWN, buff=0.3, aligned_edge=LEFT),
                    [p.next_to(example, DOWN, aligned_edge=LEFT) if i == 0 else p.next_to(p_sets[i-1], RIGHT, aligned_edge=UP) for i, p in enumerate(p_sets)],
                )
            )
        )
        self.wait()
