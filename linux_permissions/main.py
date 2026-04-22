from manim import *
from elements import *


class scene_1(Scene):
    """
    presentation of Linux permissions
    """
    def construct(self):
        ## create stuff
        intro, example, p_sets = frame_1()
        intro.scale(0.5).center()
        example.scale(0.4).next_to(intro, DOWN, aligned_edge=LEFT)
        # Split into chunks: [-rw] [r--] [r--]
        user = example[0:4]
        group = example[4:7]
        other = example[7:10]
        big_example = Text(
            permissions_example,
            font="Noto Sans Mono",
            weight=BOLD
        ).scale(2.5)

        # --- STEP 1: show stuff ---
        self.add(grid, Dot())
        self.play(Create(intro))

        # --- STEP 2: Pause for effect ---
        self.wait(5)

        big_example.center

        self.play(
            FadeOut(intro),
            Transform(example, big_example)
        )

        self.wait(1)

        # --- STEP 4: Highlight permission groups ---

        # Create highlight boxes
        user_box = SurroundingRectangle(user, color=YELLOW, buff=0.2)
        group_box = SurroundingRectangle(group, color=BLUE, buff=0.2)
        other_box = SurroundingRectangle(other, color=GREEN, buff=0.2)

        labels = [
            Text("user").next_to(user_box, DOWN),
            Text("group").next_to(group_box, DOWN),
            Text("other").next_to(other_box, DOWN),
        ]

        # Animate each group one by one
        for box, label in zip(
            [user_box, group_box, other_box],
            labels
        ):
            self.play(Create(box), FadeIn(label))
            self.wait(1.5)
            self.play(FadeOut(box), FadeOut(label))

        self.wait()