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
cmd = "cat $HOME/COURSES/API_PHYSICS/geometry.hpp | grep '#define BACKGROUND_CHOSEN_COLOR' | sed -e 's/^[[:space:]]*//' | cut -d ' ' -f3"
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
DURATION_TO_PROCESS_TIMELINE = 7
#
#############################

DEMONSTRATION_SIZE = 22

LECON_TITLE=25



class RollingCar(Scene):
    def construct(self):
        # Create a horizontal axis (the road)
        road = Line(start=LEFT, end=RIGHT)

        # Load the car image
        #car_image = ImageMobject("/manim/images/voiture_rouge.png")
        #car_image.set_height(0.2)  # Adjust the size of the image if necessary

        # Position the car at the start of the road
        #car_image.move_to(road.get_start())

        # Create a dot to represent the position of the car
        car_dot = Dot(color=RED)
        car_dot.move_to(road.get_start())

        # Always redraw the car image
        #car_image.add_updater(lambda m: m.move_to(car_dot.get_center()))

        # Animate the movement of the dot along the road
        self.play(Create(road), Create(car_dot))

        # Animate the movement of the dot along the road
        self.play(MoveAlongPath(car_dot, road), run_time=2)

        # Remove the dot
        self.play(FadeOut(car_dot))

        # Remove the updater to stop redrawing the car image
        #car_image.clear_updaters()

        # Add the car image
        #self.play(Create(car_image))

        self.wait(2)