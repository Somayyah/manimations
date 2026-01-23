from manim import *
from elements import *


class linux_permissions(Scene):

    def construct(self):
        # self.add(grid, Dot())
        intro, example, p_sets = frame_1()
        intro.scale(0.5).to_edge(UP, buff=2).to_edge(LEFT, buff=1)
        example.scale(0.3).next_to(intro, DOWN, aligned_edge=LEFT)

        for i in [intro, example]:
            self.play(Create(i))

        # for p in [
        #     (
        #         p.next_to(example, DOWN, aligned_edge=LEFT)
        #         if i == 0
        #         else p.next_to(p_sets[i - 1], RIGHT, aligned_edge=UP)
        #     )
        #     for i, p in enumerate(p_sets)
        # ]:
        #     self.play(Create(p))

        self.wait()
