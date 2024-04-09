# ----------------------------------------------------------------------------- #
# c1_pesenteur-tir-tendu.py
#
#
# ----------------------------------------------------------------------------- #
from manim import *
from chanim import *
from manim_physics import *

import numpy as np
import random
import subprocess
import re 

from intros_videos import USE_DEFAULT_MANIM_CONFIG, CONFIG_MANIM_BACKGROUND

from manim.mobject.geometry.tips import ArrowTriangleTip,\
                                        ArrowSquareTip, ArrowSquareFilledTip,\
                                        ArrowCircleTip, ArrowCircleFilledTip

# SET BACKGROUND COLOR (get this color from extern/geometry.cpp which has been copied from host to container by ./run.sh)

#cmd = "docker exec -it my-math-tle-container  cat /manim/geometry.hpp | grep '#define BACKGROUND_CHOSEN_COLOR' | sed -e 's/^[[:space:]]*//' | cut -d ' ' -f3"
cmd = "cat  ext-geometry.hpp | grep '#define EXTERN_SCREEN_STROKE_COLOR' | sed -e 's/^[[:space:]]*//' | cut -d ' ' -f3  "
execution = subprocess.Popen([ cmd ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, err = execution.communicate(b"get background color")
rc = execution.returncode 
global BACKGROUND_CHOSEN_COLOR
BACKGROUND_CHOSEN_COLOR = output.decode()
BACKGROUND_CHOSEN_COLOR = BACKGROUND_CHOSEN_COLOR.strip()
#BACKGROUND_CHOSEN_COLOR = str( BACKGROUND_CHOSEN_COLOR )
# THE TITLE OF THIS LESSON:
TOP_MENU_LECON_TITLE_FROM_MANIM_PYTHON_FILE = "EQ PARAM DROITE"

print("\n::::::BACKGROUND_CHOSEN_COLOR:%s" % BACKGROUND_CHOSEN_COLOR )

DEMONSTRATION_SIZE = 22

LECON_TITLE=25

# https://github.com/Matheart/manim-physics

############################
#
DURATION_TO_PROCESS_TIMELINE = 1
#
#############################

DEMONSTRATION_SIZE = 22

LECON_TITLE=25

def get_arc_lines_on_function2(
    graph, plane, dx=1, line_color=WHITE, line_width=1, x_min=None, x_max=None
):

    dots = VGroup()
    lines = VGroup()
    result = VGroup(dots, lines)

    x_range = np.arange(x_min, x_max, dx)
    colors = color_gradient([BLUE_A, GREEN_B], len(x_range))

    for x, color in zip(x_range, colors):
        p1 = Dot().scale(0.7).move_to(plane.input_to_graph_point(x, graph))
        p2 = Dot().scale(0.7).move_to(plane.input_to_graph_point(x + dx, graph))
        dots.add(p1, p2)
        dots.set_fill(colors, opacity=0.8)

        line = Line(
            p1.get_center(),
            p2.get_center(),
            stroke_color=line_color,
            stroke_width=line_width,
        )
        #lines.add(line)
        lines.add(p1, p2)

    return result



# ............................................................................. #
#
#                             VIDEO 1
#
# .............................................................................. #
# use a SpaceScene to utilize all specific rigid-mechanics methods

class ProjectileParaboleTirTendu(SpaceScene):
    def construct(self):
        #self.camera.background_color = WHITE
        RUN_TIME = 3
        TRACKER_MAX_VALUE = 9.15

   
        poteau = SVGMobject("./images/projection_vecteur.svg").move_to(3*LEFT+2*UP) #path from within docker container

        #gardien = SVGMobject("/manim/images/gardien_seul.svg").next_to(LEFT)
        #basket_player = SVGMobject("/Users/whodunit/Downloads/drawing.svg").move_to(LEFT+DOWN)
        self.play( FadeIn(poteau) )
        self.wait()
         
        
