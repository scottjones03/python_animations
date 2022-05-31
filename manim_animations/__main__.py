import cmd
import os
import sys
from manim_animations.vector_arrow import VectorArrow
import manim

if __name__ == "__main__":
    # os.system(r"manim render -r 256,144")
    os.system(r"manim -pql  -r 720,720 ./manim_animations/vector_arrow.py VectorArrow")
