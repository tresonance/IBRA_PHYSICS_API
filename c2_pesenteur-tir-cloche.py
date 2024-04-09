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

class ProjectileParaboleTirCloche(SpaceScene):
    def construct(self):
        vo = 60
        alpha = 80 / 180.0 * PI
        g = 10

        x_range, y_range , axe_len = [0, 200, 20],  [0, 150, 15], 5
        axes = Axes(
            x_range=x_range, 
            y_range=y_range, 
            stroke_width=1.0, 
            x_length=axe_len, 
            y_length=axe_len,
            color = BLACK
            )#.add_coordinates()

        self.add(axes)

        point_origin = axes.c2p( 0,0 )
        
        tracker = ValueTracker(0)

        normalized_v =  lambda v: v / np.sqrt(np.sum(v**2))

        def get_next_dot_position(x, y):
            global dot_here
            p = axes.c2p(x,y)
            dot_here =  Dot(color=YELLOW, radius=0.06).move_to( p   )
            return dot_here
        
        def get_next_arrow_position(x, y):
            
            p = axes.c2p(x,y)
            y_prime = -g*x/(vo*np.cos( alpha ))**2 + np.tan( alpha )
            vector_dir = normalized_v(np.array([1.0, y_prime, 0]))

            q = 0.8*vector_dir
            
            p_next = np.array([p[0], p[1], 0]) + np.array([ q[0], q[1], 0])
            #p_next = axes.c2p( p_next[0], p_next[1] )

            arrow_here = Arrow(
                start=p, 
                end=p_next,
                buff=0.2, color=ORANGE
                )
            return arrow_here

        
        def get_next_trajectoiry_point(t):
            if not ( int(t) % 5):
                x =  vo*np.cos(alpha)*t + point_origin[0]
                y = -0.5*g*t**2 + vo*np.sin(alpha)*t + point_origin[1]
                p = axes.c2p(x, y)
                return  Dot(color=BLUE, radius=0.4).move_to( p )
            return VMobject()

        

        point_rond = always_redraw(lambda :get_next_dot_position(
            vo*np.cos(alpha)*tracker.get_value() + point_origin[0],
            -0.5*g*tracker.get_value()**2 + vo*np.sin(alpha)*tracker.get_value() + point_origin[1]
        ) )

        vitesse = always_redraw(lambda :get_next_arrow_position(
            vo*np.cos(alpha)*tracker.get_value() + point_origin[0],
             -0.5*g*tracker.get_value()**2 + vo*np.sin(alpha)*tracker.get_value() + point_origin[1]
        ) )
        
        RUN_TIME = 5
        TRACKER_MAX_VALUE = 20
        graph = axes.plot(
            lambda x:-g*x**2/(2*(vo*np.cos(alpha))**2) + x*np.tan(alpha), x_range=[0, TRACKER_MAX_VALUE], color=BLUE
        )
        
        global trajectory
        trajectory = VGroup()
        
        def get_arc_lines_on_function(group, t):
            x =  vo*np.cos(alpha)*t + point_origin[0]
            y = -0.5*g*t**2 + vo*np.sin(alpha)*t + point_origin[1]
            p = axes.c2p(x, y)
            group.add( Dot(color=BLUE, radius=0.01).move_to( p ) )
            return group

        trajectory = always_redraw(lambda : get_arc_lines_on_function(
            trajectory, tracker.get_value()
        ) )

        trajectory2 = always_redraw(
            lambda: get_arc_lines_on_function2(
                graph=graph,
                plane=axes,
                dx=2+tracker.get_value(),
                x_min=0,
                x_max=TRACKER_MAX_VALUE,
                line_color=RED,
                line_width=5,
            )
        ) 

       
        #basket_player = SVGMobject("/Users/whodunit/Downloads/drawing.svg").move_to(LEFT+DOWN)
        self.add(point_rond, vitesse, trajectory )
        self.play(tracker.animate.set_value(TRACKER_MAX_VALUE), run_time=RUN_TIME)
        self.wait()     
        
