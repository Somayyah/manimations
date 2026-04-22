from manim import *
from elements import *

class VimSubstitute(Scene):
    def construct(self):
        code = VGroup(*[Text(p, font="Monospace") for p in parts])
        code.arrange(RIGHT, buff=0.05)
        code.scale(0.6)

        self.play(FadeIn(code))
        self.wait()
        for idx, ntxt in replacements.items():
            old_part = code[idx]

            if ntxt == "":
                self.play(FadeOut(old_part))
                code[idx] = Text("")
            else:
                if idx == 5:
                    new_part = Text(ntxt, font="Monospace", color=YELLOW).scale(0.4)
                else:
                    new_part = Text(ntxt, font="Monospace", color=YELLOW).scale(0.6)
                new_part.move_to(old_part)

                self.play(Transform(old_part, new_part))
                code[idx] = new_part
            self.wait(0.5)
        self.play(code.animate.center().arrange(RIGHT, buff=0.05))

        self.wait(2)