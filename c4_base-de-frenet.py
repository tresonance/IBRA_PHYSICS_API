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
DURATION_TO_PROCESS_TIMELINE = 1
#
#############################

DEMONSTRATION_SIZE = 22

LECON_TITLE=25


class BaseFrenet(Scene):
    def construct(self):
        w = 0.14 
        T = (2 * PI / w)
    
        angle_tracker = ValueTracker(0)

        circle = Circle(color=WHITE, radius=3).shift(LEFT)
        R = circle.get_radius()
        circle_center = circle.get_center()

        normalized_v =  lambda v: v / np.sqrt(np.sum(v**2))

        # Repere
        SURPLUS=0.2
        line_x = Line(
            start=circle_center + np.array([-R-SURPLUS, 0, 0]),
             end=circle_center + np.array([R+SURPLUS, 0, 0]),
             color= YELLOW_E, stroke_width=0.4,
           
        )
        triangle_x = Triangle().scale(0.05).rotate(-90*DEGREES).move_to(line_x.get_end())

        line_y = Line(
            start=circle_center + np.array([0,-R-SURPLUS,0]),
             end=circle_center + np.array([0, R+SURPLUS, 0]),
             color= YELLOW_E, stroke_width=0.4,
            
        )
        triangle_y = Triangle().scale(0.05).rotate(-120*DEGREES).move_to(line_y.get_end())


        zero_text = MathTex("\\text{O}").move_to(  circle_center + np.array([0.2,-0.2, 0])  )

        def get_next_point_mobile_position(t):
            pos = np.array([   
                circle_center[0] + R * np.cos(w*t),
                 circle_center[1] + R * np.sin(w*t),
                 0
            ])
            new_dot = Circle( radius=0.1, color=YELLOW, fill_opacity=1).move_to(  pos  )
            return new_dot
        
        point_mobile = always_redraw(lambda: get_next_point_mobile_position((
            angle_tracker.get_value()
        )))


        def get_next_line_radius(t):
            line_radius = Line(
            start=circle_center ,
             end=circle_center + np.array([R * np.cos(w*t), R * np.sin(w*t),  0]),
             color= PURPLE_E, stroke_width=0.6,
            )
            return line_radius

        line_radius = always_redraw(lambda: get_next_line_radius(
            angle_tracker.get_value()
        ) )

        def get_next_arc_position(t):

            if t == 0:
                t += 0.001
            line_start = Line(
            start=circle_center ,
             end=circle_center + np.array([R+SURPLUS, 0, 0]),
             color= YELLOW_E, stroke_width=0.2)
            
            line_radius = Line(
            start=circle_center ,
             end=circle_center + np.array([R * np.cos(w*t), R * np.sin(w*t),  0]),
             color= PURPLE_E, stroke_width=0.6,
            )

            global angle_arc

            angle_arc = Angle(
                line1 = line_start, 
                line2 = line_radius, 
                stroke_width=1, dot=False, 
                color=YELLOW_E
            )
            return angle_arc



        angle_arc = always_redraw(lambda: get_next_arc_position(
                angle_tracker.get_value()
        ))

        def get_next_vector_normal(t):

            new_dot_pos = np.array([   
                circle_center[0] + R * np.cos(w*t),
                 circle_center[1] + R * np.sin(w*t),
                 0
            ])

            normal_dir =  normalized_v( circle.get_center() - new_dot_pos )
            vector_normal = Arrow(
            start=new_dot_pos,
             end=new_dot_pos + 1.3 * normal_dir ,
             color= RED_E, stroke_width=2.7,
           
            )
            return vector_normal

        
        def get_next_vector_tangent(t):

            new_dot_pos = np.array([   
                circle_center[0] + R * np.cos(w*t),
                 circle_center[1] + R * np.sin(w*t),
                 0
            ])

            normal_dir =   circle.get_center() - new_dot_pos 
            tangent_dir = normalized_v( np.array([
                normal_dir[1], -normal_dir[0], 0 ]) 
            )

            vector_tangent = Arrow(
            start=new_dot_pos,
             end=new_dot_pos + 1.3 * tangent_dir ,
             color= BLUE_E, stroke_width=2.7,
           
            )
            return vector_tangent


        normal_vector = always_redraw(lambda: get_next_vector_normal(
            angle_tracker.get_value()
        ))

        tangent_vector = always_redraw(lambda: get_next_vector_tangent(
            angle_tracker.get_value()
        ))

        def get_next_angle_arc_text(t):
            t = 0.5*t
            new_dot_middle_pos = np.array([   
                circle_center[0] + R * np.cos(w*t),
                 circle_center[1] + R * np.sin(w*t),
                 0
            ])
            vector_dir =   normalized_v( new_dot_middle_pos - circle.get_center() )
            
            arc_text = MathTex(r"\alpha", color=TEAL_A).scale(0.9).move_to(  
              circle_center + 1.1*vector_dir)
            return  arc_text


        arc_angle_text = always_redraw(lambda : get_next_angle_arc_text(
            angle_tracker.get_value()
        ))

        vecteur_i =  Arrow(
            start=circle_center ,
             end=circle_center + np.array([0.45*R , 0,  0]),
             color= YELLOW_E, stroke_width=0.6,
            )
        vecteur_j =  Arrow(
            start=circle_center ,
             end=circle_center + np.array([0, 0.45*R ,  0]),
             color= YELLOW_E, stroke_width=0.6,
            )

       
        self.add(  circle, point_mobile, line_x, line_y , 
        triangle_x, triangle_y, zero_text, line_radius, 
        angle_arc,  normal_vector, tangent_vector,
        arc_angle_text, vecteur_i, vecteur_j )

        self.play(angle_tracker.animate.set_value(T), run_time=7)
        self.wait()
