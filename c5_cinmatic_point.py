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


# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
# Mvt Recilign Uniforme
#
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #

class Mvt_Rec_Uni_CARS(Scene):
    def construct(self):
        LEFT_START_GREEN_CAR = 5
        RIGHT_START_RED_GREEN_CAR = 4.5
       


        tracker = ValueTracker(0)

        # Create a horizontal axis (the road)
       
        # Load the Red car image
        red_car_image = ImageMobject("/manim/images/voiture_rouge_vers_droite.png")
        v0_red,t0_red,x0_red = 1.75, 0, 0
        DOWN_START_RED_GREEN_CAR = 0.25
        red_car_image.move_to(LEFT_START_GREEN_CAR*LEFT+DOWN_START_RED_GREEN_CAR*DOWN)
        #car_image.set_height(0.2)  # Adjust the size of the image if necessary
        road_1 = DashedLine(start=LEFT_START_GREEN_CAR*LEFT+DOWN_START_RED_GREEN_CAR*DOWN, end=RIGHT_START_RED_GREEN_CAR*RIGHT+DOWN_START_RED_GREEN_CAR*DOWN, dashed_ratio=0.5, fill_color=RED)
        
        # Load the Green car image
        green_car_image = ImageMobject("/manim/images/voiture_verte_vers_droite.png")
        v0_green,t0_green,x0_green = 4, 2, 0
        DOWN_START_RED_GREEN_CAR = 0.75
        green_car_image.move_to(LEFT_START_GREEN_CAR*LEFT+DOWN_START_RED_GREEN_CAR*DOWN)
        road_2 = DashedLine(start=LEFT_START_GREEN_CAR*LEFT+DOWN_START_RED_GREEN_CAR*DOWN, end=RIGHT_START_RED_GREEN_CAR*RIGHT+DOWN_START_RED_GREEN_CAR*DOWN, dashed_ratio=0.5, fill_color=GREEN)
        # =================================== >>>>>>
        # RED CAR
        def imageRedCarUpdater(v0, x0, t0, t):
            dummy = red_car_image.move_to( (v0*(t - t0) + x0)*RIGHT + LEFT_START_GREEN_CAR*LEFT  )
            return dummy

        red_car_image = always_redraw(lambda: imageRedCarUpdater(
            v0_red,
            x0_red,
            t0_red, 
            tracker.get_value()
        ))

        # GREEN CAR
        def imageGreenCarUpdater(v0, x0, t0, t):
            delta_t = t - t0
            if delta_t < 0:
                delta_t = 0

            dummy = green_car_image.move_to( (v0*delta_t + x0)*RIGHT + LEFT_START_GREEN_CAR*LEFT + DOWN_START_RED_GREEN_CAR*DOWN )
            
            return dummy

        green_car_image = always_redraw(lambda: imageGreenCarUpdater(
            v0_green,
            x0_green,
            t0_green,
            tracker.get_value()
        ))
        # =================================== >>>>>>

        line = Line(LEFT_START_GREEN_CAR*LEFT+DOWN, RIGHT_START_RED_GREEN_CAR*RIGHT+DOWN)

        # =================================== >>>>>>

        LEFT_START_PINK_BLUE_CAR = 5
        RIGHT_START_PINK_BLUE_CAR = 6
        DOWN_START_PINK_BLUE_CAR_1 = 1.25
        # Load the Blue car image
        rose_car_image = ImageMobject("/manim/images/voiture_rose_vers_gauche.png")
        v0_rose,t0_rose,x0_rose = 2.5, 0, RIGHT_START_PINK_BLUE_CAR
        rose_car_image.move_to(RIGHT_START_PINK_BLUE_CAR*RIGHT + DOWN_START_PINK_BLUE_CAR_1*DOWN)
        #car_image.set_height(0.2)  # Adjust the size of the image if necessary
        road_3 = DashedLine(start=LEFT_START_PINK_BLUE_CAR*LEFT+DOWN_START_PINK_BLUE_CAR_1*DOWN, end=RIGHT_START_PINK_BLUE_CAR*RIGHT+DOWN_START_PINK_BLUE_CAR_1*DOWN, dashed_ratio=0.5)
        
        # Load the Pink car image
        DOWN_START_PINK_BLUE_CAR_2 = 1.75
        blue_car_image = ImageMobject("/manim/images/voiture_blueue_vers_gauche.png")
        v0_blue,t0_blue,x0_blue = 3, 2, RIGHT_START_PINK_BLUE_CAR
        blue_car_image.move_to(RIGHT_START_PINK_BLUE_CAR*RIGHT+DOWN_START_PINK_BLUE_CAR_2*DOWN)
        road_4 = DashedLine(start=LEFT_START_PINK_BLUE_CAR*LEFT+DOWN_START_PINK_BLUE_CAR_2*DOWN, end=4.5*RIGHT+DOWN_START_PINK_BLUE_CAR_2*DOWN, dashed_ratio=0.5)



        #self.play( Create(road_1), Create(road_2) , Create(road_3), Create(road_4) )
        
        self.add( line )
        # Animate the movement of the dot along the road
        
        
        # PINK CAR
        def imageRoseCarUpdater(v0, x0, t0, t):
            delta_t = t - t0
            if delta_t < 0:
                delta_t = 0
            dummy = rose_car_image.move_to( (v0*delta_t)*LEFT + x0*RIGHT + DOWN_START_PINK_BLUE_CAR_1*DOWN  )
            return dummy

        rose_car_image = always_redraw(lambda: imageRoseCarUpdater(
            v0_rose,
            x0_rose,
            t0_rose, 
            tracker.get_value()
        ))

        # BLUE CAR
        def imageBlueCarUpdater(v0, x0, t0, t):
            delta_t = t - t0
            if delta_t < 0:
                delta_t = 0

            dummy = blue_car_image.move_to( (v0*delta_t)*LEFT + x0*RIGHT + DOWN_START_PINK_BLUE_CAR_2*DOWN )
            
            return dummy

        blue_car_image = always_redraw(lambda: imageBlueCarUpdater(
            v0_blue,
            x0_blue,
            t0_blue,
            tracker.get_value()
        ))
        # ----------------------------------
        self.add( red_car_image, green_car_image, rose_car_image, blue_car_image )
        self.play(tracker.animate.set_value(4), run_time=5)
        self.wait()

# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
# Mvt Recilign Uniformement varié
#
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #

class Mvt_Rec_Uni_Varie_CARS(Scene):
    def construct(self):
        LEFT_START_GREEN_CAR = 5
        RIGHT_START_RED_GREEN_CAR = 4.5
       


        tracker = ValueTracker(0)

        # Create a horizontal axis (the road)
       
        # Load the Red car image
        red_car_image = ImageMobject("/manim/images/voiture_rouge_vers_droite.png")
        gamma_red, v0_red,t0_red,x0_red = 2, 1.75, 0, 0
        DOWN_START_RED_GREEN_CAR = 0.25
        red_car_image.move_to(LEFT_START_GREEN_CAR*LEFT+DOWN_START_RED_GREEN_CAR*DOWN)
        #car_image.set_height(0.2)  # Adjust the size of the image if necessary
        road_1 = DashedLine(start=LEFT_START_GREEN_CAR*LEFT+DOWN_START_RED_GREEN_CAR*DOWN, end=RIGHT_START_RED_GREEN_CAR*RIGHT+DOWN_START_RED_GREEN_CAR*DOWN, dashed_ratio=0.5, fill_color=RED)
        
        # Load the Green car image
        green_car_image = ImageMobject("/manim/images/voiture_verte_vers_droite.png")
        gamma_green, v0_green,t0_green,x0_green = 2.5, 4, 2, 0
        DOWN_START_RED_GREEN_CAR = 0.75
        green_car_image.move_to(LEFT_START_GREEN_CAR*LEFT+DOWN_START_RED_GREEN_CAR*DOWN)
        road_2 = DashedLine(start=LEFT_START_GREEN_CAR*LEFT+DOWN_START_RED_GREEN_CAR*DOWN, end=RIGHT_START_RED_GREEN_CAR*RIGHT+DOWN_START_RED_GREEN_CAR*DOWN, dashed_ratio=0.5, fill_color=GREEN)
        # =================================== >>>>>>
        # RED CAR
        def imageRedCarUpdater(v0, x0, t0, t):
            delta_t = t - t0
            if delta_t < 0:
                delta_t = 0
            dummy = red_car_image.move_to( (0.5*gamma_red*delta_t**2+v0*delta_t + x0)*RIGHT + LEFT_START_GREEN_CAR*LEFT  )
            return dummy

        red_car_image = always_redraw(lambda: imageRedCarUpdater(
            v0_red,
            x0_red,
            t0_red, 
            tracker.get_value()
        ))

        # GREEN CAR
        def imageGreenCarUpdater(v0, x0, t0, t):
            delta_t = t - t0
            if delta_t < 0:
                delta_t = 0

            dummy = green_car_image.move_to( (0.5*gamma_green*delta_t**2+v0*delta_t + x0)*RIGHT + LEFT_START_GREEN_CAR*LEFT + DOWN_START_RED_GREEN_CAR*DOWN )
            
            return dummy

        green_car_image = always_redraw(lambda: imageGreenCarUpdater(
            v0_green,
            x0_green,
            t0_green,
            tracker.get_value()
        ))
        # =================================== >>>>>>

        line = Line(LEFT_START_GREEN_CAR*LEFT+DOWN, RIGHT_START_RED_GREEN_CAR*RIGHT+DOWN)

        # =================================== >>>>>>

        LEFT_START_PINK_BLUE_CAR = 5
        RIGHT_START_PINK_BLUE_CAR = 6
        DOWN_START_PINK_BLUE_CAR_1 = 1.25
        # Load the Blue car image
        rose_car_image = ImageMobject("/manim/images/voiture_rose_vers_gauche.png")
        v0_rose,t0_rose,x0_rose = 2.5, 0, RIGHT_START_PINK_BLUE_CAR
        rose_car_image.move_to(RIGHT_START_PINK_BLUE_CAR*RIGHT + DOWN_START_PINK_BLUE_CAR_1*DOWN)
        #car_image.set_height(0.2)  # Adjust the size of the image if necessary
        road_3 = DashedLine(start=LEFT_START_PINK_BLUE_CAR*LEFT+DOWN_START_PINK_BLUE_CAR_1*DOWN, end=RIGHT_START_PINK_BLUE_CAR*RIGHT+DOWN_START_PINK_BLUE_CAR_1*DOWN, dashed_ratio=0.5)
        
        # Load the Pink car image
        DOWN_START_PINK_BLUE_CAR_2 = 1.75
        blue_car_image = ImageMobject("/manim/images/voiture_blueue_vers_gauche.png")
        v0_blue,t0_blue,x0_blue = 3, 2, RIGHT_START_PINK_BLUE_CAR
        blue_car_image.move_to(RIGHT_START_PINK_BLUE_CAR*RIGHT+DOWN_START_PINK_BLUE_CAR_2*DOWN)
        road_4 = DashedLine(start=LEFT_START_PINK_BLUE_CAR*LEFT+DOWN_START_PINK_BLUE_CAR_2*DOWN, end=4.5*RIGHT+DOWN_START_PINK_BLUE_CAR_2*DOWN, dashed_ratio=0.5)



        #self.play( Create(road_1), Create(road_2) , Create(road_3), Create(road_4) )
        
        self.add( line )
        # Animate the movement of the dot along the road
        
        
        # PINK CAR
        def imageRoseCarUpdater(v0, x0, t0, t):
            delta_t = t - t0
            if delta_t < 0:
                delta_t = 0
            dummy = rose_car_image.move_to( (v0*delta_t)*LEFT + x0*RIGHT + DOWN_START_PINK_BLUE_CAR_1*DOWN  )
            return dummy

        rose_car_image = always_redraw(lambda: imageRoseCarUpdater(
            v0_rose,
            x0_rose,
            t0_rose, 
            tracker.get_value()
        ))

        # BLUE CAR
        def imageBlueCarUpdater(v0, x0, t0, t):
            delta_t = t - t0
            if delta_t < 0:
                delta_t = 0

            dummy = blue_car_image.move_to( (v0*delta_t)*LEFT + x0*RIGHT + DOWN_START_PINK_BLUE_CAR_2*DOWN )
            
            return dummy

        blue_car_image = always_redraw(lambda: imageBlueCarUpdater(
            v0_blue,
            x0_blue,
            t0_blue,
            tracker.get_value()
        ))
        # ----------------------------------
        self.add( red_car_image, green_car_image, rose_car_image, blue_car_image )
        self.play(tracker.animate.set_value(3), run_time=5)
        self.wait()