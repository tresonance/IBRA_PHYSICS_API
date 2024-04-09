from manim import *

import numpy as np
import random
import math

# ----------------------------------------- #
#         CAMERA CONFIG 
USE_DEFAULT_MANIM_CONFIG=False
CONFIG_MANIM_BACKGROUND="#475147"
# ----------------------------------------- #

#------------------------------------------------------------------------------------------#
# videos_prodsca_series_intro.py
#
#       |--> inside this file, we have manim class which describe the the presentation of videos courses  
#
#       [1] -> video1: Rappel Norme de vecteur U 
#       [2] -> video2: Rappel Norme de vecteur AB connaissant les coordonnées
#       [3] -> video3: Rappel: Formule d'Al Kashi
#       [4] -> video4: Produit Scalaire avec cos
#       [5] -> video5: Produit Scalaire avec coordonnées
#       [6] -> video6: Produit Scalaire avec 1/2 (Formule deduite d'identité remarquable)
#       [7] -> video7: Formule avec Projection
#       [8] -> video8: Travaux dirigés - Exercices
#
#-------------------------------------------------------------------------------------------#

NUM_YOUTUBE_ICON_LEFT_SIDE = 4 #Number of Vi
NUM_YOUTUBE_ICON_RIGHT_SIDE = 4
DEMONSTRATION_SIZE = 22
# vscode://vscode.github-authentication/did-authenticate?windowid=5&code=2cd85fb160fb4ce98bfd&state=d492904a-fa26-4de0-95fb-73fed8739787

class PreviewVideosSeriesProSca1ere(Scene):
    def construct(self):
        if USE_DEFAULT_MANIM_CONFIG:
            CONFIG={
		        "camera_config":{"background_color":CONFIG_MANIM_BACKGROUND}
	        }

        Radius = 1.50
        STROKE_WIDTH=1.2
       

        angle = ValueTracker(0.5)
        #---------------------------  CHAPTER NAME and CLASSE LEVEL -------------------------#
        lesson_title =always_redraw(lambda: 
        Tex(
            r" Le Produit Scalaire ", color=GREEN
        ).move_to(-3*DOWN))

        lesson_niveau =always_redraw(lambda: 
        Tex(
            r"  Niveau 1ère", color=dot_color, font_size=20
        ).to_edge(UL))
        
       
        self.add(lesson_title)
        self.add(lesson_niveau)
        #------------------------------------------------------------------------------------------#


        #-------------------------- YOUTUBE ICONS CIRCLE CONTAINER (LEFT SIDE) --------------------#
        rectangles_left = VGroup(*[ RoundedRectangle( width=1.0, height=0.45, stroke_color=RED, 
        stroke_width=1.2, corner_radius=0.2, fill_opacity=0.1).set_fill(RED_E) for i in range( NUM_YOUTUBE_ICON_LEFT_SIDE ) ]).arrange(DOWN, buff=0.4).to_edge(3*UL, buff=0.5)
        #-------------------------- YOUTUBE ICONS CIRCLE CONTAINER (RIGHT SIDE) --------------------#
        rectangles_right = VGroup(*[ RoundedRectangle( width=1.0, height=0.45, stroke_color=RED, 
        stroke_width=1.2, corner_radius=0.2, fill_opacity=0.1).set_fill(RED_E) for i in range( NUM_YOUTUBE_ICON_RIGHT_SIDE ) ]).arrange(DOWN, buff=0.4).to_edge(3*UR, buff=0.5)
        

        #------------------------ YOUTUBE ICONS SMALL TRIANGLE (INSIDE LEFT CIRCLE CONTAINER ) --------------------#
        triangles_left = VGroup(*[ Triangle(radius=0.1, fill_opacity=1.0).set_fill(GREEN).rotate(15).move_to(rectangles_left[i].get_center()) for i in range( NUM_YOUTUBE_ICON_LEFT_SIDE ) ])
        #------------------------ YOUTUBE ICONS SMALL TRIANGLE (INSIDE RIGHT CIRCLE CONTAINER ) --------------------#
        triangles_right = VGroup(*[ Triangle(radius=0.1, fill_opacity=1.0).set_fill(GREEN).rotate(15).move_to(rectangles_right[i].get_center()) for i in range( NUM_YOUTUBE_ICON_RIGHT_SIDE ) ])
        
        #Display rectabgles and Triangles
        self.add(rectangles_left)
        self.add(triangles_left)
        self.add(rectangles_right)
        self.add(triangles_right)

        ###################################################################################
        #
        #  PRESENTATION LEFT SCREEN SIDE
        #
        ###################################################################################
        #----------------------------------- FIRST LESSON --------------------------------#
        
        title1_left = MarkupText(f'Vidéo1:  <span fgcolor="{YELLOW}" > Norme d\' un vecteur </span>', color=PINK, font_size=30).move_to(-2.5*DOWN)
        
        text_norme_u_square = MathTex("\\norm{\\vec{u}}", font_size=96).move_to(0.5*RIGHT+UP)
        text_norme_u_square.set_color_by_tex_to_color_map({
            "{u}": YELLOW, 
            "?": TEAL_C
        })

        number_plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_color": TEAL_E,
                "stroke_opacity": 0.2
            },
             axis_config={
                "stroke_color": dot_color,
                "stroke_width": 0.1
                }
            )
        vec_1 = Vector([2, 2], color=GREEN)
        label_1 = vec_1.coordinate_label()

        #"\\coord{ x_{ \\vec{u} }, y_{ \\vec{u} } } . \\coord{ x_{ \\vec{v} }, y_{\\vec{v} } } =  x_{\\vec{u}} . x_{\\vec{v}} +  y_{\\vec{u}} . y_{\\vec{v} } "
        self.play(FadeIn(title1_left))
        self.add(number_plane, vec_1, label_1, text_norme_u_square.scale(0.8) )
        self.play( Rotate(text_norme_u_square.scale(0.8), angle=PI/3 ) )

        self.wait()
        
        intro_video1_left = Group( number_plane, vec_1, label_1,  text_norme_u_square,  title1_left)
        self.play(intro_video1_left.animate.set_height(0.6).move_to(triangles_left[0].get_center()), run_time = 2)
        intro_video1_left.scale(0.15).move_to( triangles_left[0].get_center() )
        self.wait()

        #----------------------------------- END FIRST LESSON --------------------------------#
        #-------------------------------------------------------------------------------------#
    

        #----------------------------------- SECOND LESSON -----------------------------------#
        title2_left = MarkupText(f'Vidéo2:  <span fgcolor="{YELLOW}" > Norme d\' un vecteur </span>', color=PINK, font_size=30).move_to(-2.5*DOWN)
        
        text_norme_u_square = MathTex("\\norm{\\vec{AB}}", font_size=56).move_to(0.5*RIGHT+UP)
        text_norme_u_square.set_color_by_tex_to_color_map({
            "{u}": YELLOW, 
            "?": TEAL_C
        })

        text_A = MathTex("\\text{A}\\binom{x_A}{y_A}", font_size=16).move_to(0.25*DOWN)
        text_A.set_color_by_tex_to_color_map({
            "{A}": YELLOW_B
        })

        text_B = MathTex("\\text{B}\\binom{x_B}{y_B}", font_size=16).move_to(2.3*RIGHT+2*UP)
        text_B.set_color_by_tex_to_color_map({
            "{B}": YELLOW_E
        })

        number_plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_color": TEAL_E,
                "stroke_opacity": 0.2
            },
            axis_config={
                "stroke_color": dot_color,
                "stroke_width": 0.1
                }
            )
        vec_1 = Vector([2, 2], color=GREEN)
       
        #"\\coord{ x_{ \\vec{u} }, y_{ \\vec{u} } } . \\coord{ x_{ \\vec{v} }, y_{\\vec{v} } } =  x_{\\vec{u}} . x_{\\vec{v}} +  y_{\\vec{u}} . y_{\\vec{v} } "
        self.play(FadeIn(title2_left))
        self.add(number_plane, vec_1, text_A,text_B, text_norme_u_square.scale(0.8) )
        self.play( Rotate(text_norme_u_square.scale(0.8), angle=PI/3 ) )

        self.wait()
        
        intro_video1_left = Group( number_plane, vec_1, number_plane, vec_1, text_A,text_B,  text_norme_u_square,  title2_left)
        self.play(intro_video1_left.animate.set_height(0.6).move_to(triangles_left[1].get_center()), run_time = 2)
        intro_video1_left.scale(0.15).move_to( triangles_left[1].get_center() )
        self.wait()
        #------------------------ END SECOND LESSON INTRO------------------------------#
        #-----------------------------------------------------------------------------#


        #----------------------------------- THIRD LESSON --------------------------------#
        title1_left = MarkupText(f'Vidéo3:  <span fgcolor="{YELLOW}" > Al Kashi  </span>', color=PINK, font_size=40).move_to(-2.5*DOWN)

        #"\\coord{ x_{ \\vec{u} }, y_{ \\vec{u} } } . \\coord{ x_{ \\vec{v} }, y_{\\vec{v} } } =  x_{\\vec{u}} . x_{\\vec{v}} +  y_{\\vec{u}} . y_{\\vec{v} } "
        self.play(FadeIn(title1_left))
        xab_start, yab_start = -1.5,-1
        xab_end, yab_end = -2, 2
        line_AB = Line(end=np.array([xab_start, yab_start, 0]), start=np.array([xab_end, yab_end, 0]), 
        color=PINK, stroke_width=4)#.move_to(LEFT-DOWN)
        vector_AB = Vector([xab_start, yab_start], color=YELLOW).move_to(LEFT-DOWN)
        vector_AB_A_name = MathTex("A").move_to(np.array([xab_start, yab_start, 0]) )
       
        xbc_end, ybc_end = 2, 0.5
        line_BC = Line(start=np.array([xab_end, yab_end, 0]), end=np.array([xbc_end, ybc_end, 0]), 
        color=PINK, stroke_width=4)#.move_to(LEFT-DOWN)
        vector_BC = Vector([xab_end, yab_end], color=YELLOW).move_to(LEFT-DOWN)
        vector_BC_B_name = MathTex("B").move_to(np.array([xab_end, yab_end, 0]) )
        

        line_CA = Line(start=np.array([xbc_end, ybc_end, 0]), end=np.array([xab_start, yab_start, 0]), 
        color=PINK, stroke_width=4)#.move_to(LEFT-DOWN)
        vector_CA = Vector([xbc_end, ybc_end], color=YELLOW).move_to(LEFT-DOWN)
        vector_CA_C_name = MathTex("C").move_to(np.array([xbc_end, ybc_end, 0]) )
        
        angle_B = Angle(line_AB, line_BC, radius=0.4,  quadrant=(1,1), other_angle=False)
        angle_C = Angle(line_BC, line_CA, radius=0.4,  quadrant=(-1,1), other_angle=False)
        angle_A = Angle(line_CA, line_AB, radius=0.4,  quadrant=(-1,-1), other_angle=False)

        my_size=25
        formule_BC_a = MathTex("\\text{a}^2", "=", "\\text{b}^2", "+", "\\text{c}^2", "-", "2", ".", "\\text{b}", ".", "\\text{c}", ".", "\\text{cos}", "\\text{(}", "\\widehat{A}", "\\text{)}", font_size=my_size, color=YELLOW).shift(RIGHT)
        formule_BC_a.set_color_by_tex_to_color_map({
            "{a}": YELLOW_E, 
            "{b^2}": TEAL_C,
            "{c^2}": TEAL_C,
            "2": GREEN_E,
            "{b}": TEAL_C,
            "{c}": TEAL_C, 
            "{cos}": BLUE_E,
            "{(}": BLUE_E,
            "{)}": BLUE_E,
            "{A}": YELLOW_E
        })

        formule_BC = MathTex("\\text{BC}^2", "=", "\\text{AC}^2", "+", "\\text{AB}^2", "-", "\\text{2}", ".", "\\text{AC}", ".", "\\text{AB}", ".", "\\text{cos}", "\\text{(}", "\\widehat{A}", "\\text{)}", font_size=my_size).shift(RIGHT+DOWN)
        formule_BC.set_color_by_tex_to_color_map({
            "{BC}": YELLOW_E, 
            "{AB^2}": TEAL_C,
            "{AC^2}": TEAL_C,
            "{2}": GREEN_E,
            "{AB}": TEAL_C,
            "{AC}": TEAL_C, 
            "{cos}": BLUE_E,
            "{(}": BLUE_E,
            "{)}": BLUE_E,
            "{A}": YELLOW_E
        })

        group = VGroup(line_AB, vector_AB_A_name, 
        line_BC, vector_BC_B_name, 
        line_CA, vector_CA_C_name,
        angle_A, angle_B, angle_C,formule_BC_a, formule_BC, title1_left
        )

        self.add(group)
        self.wait()
        
        intro_video1_left = group
        self.play(intro_video1_left.animate.set_height(0.6).move_to(triangles_left[2].get_center()), run_time = 2)
        intro_video1_left.scale(0.15).move_to( triangles_left[2].get_center() )
        self.wait()
        
        #------------------------ END THIRD LESSON INTRO------------------------------#
        #-----------------------------------------------------------------------------#
    

        
        #----------------------------------- FOURTH LESSON --------------------------------#
        title1_left = MarkupText(f'Vidéo4:  <span fgcolor="{YELLOW}" > Formule avec cos  </span>', color=PINK, font_size=23).move_to(-2.5*DOWN)
        text1_left=MathTex(
               "\\vec{u} . \\vec{v} = \\norm{ \\vec{u} } . \\norm{\\vec{v}} . cos( \\vec{u}, \\vec{v} )"
        )
        #"\\coord{ x_{ \\vec{u} }, y_{ \\vec{u} } } . \\coord{ x_{ \\vec{v} }, y_{\\vec{v} } } =  x_{\\vec{u}} . x_{\\vec{v}} +  y_{\\vec{u}} . y_{\\vec{v} } "
        self.play(FadeIn(title1_left))
        self.play(Write(text1_left))
        framebox1 = SurroundingRectangle(text1_left[0], buff = .1)
        #framebox2 = SurroundingRectangle(text[1], buff = .1)
        
        self.play(
            Create(framebox1)#,  Create(framebox2)
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1, framebox1)
        )
        intro_video1 = Group( framebox1,  text1_left, title1_left)
        self.play(intro_video1.animate.set_height(0.6).move_to(triangles_left[3].get_center()), run_time = 2)
        intro_video1.scale(0.09).move_to( triangles_left[3].get_center() )
        self.wait()
        #--------------------------------- END FOURTH LESSON INTRO ---------------------------------#
        #--------------------------------------------------------------------------------------------#
        #--------------------------------------------------------------------------------------------#
        #--------------------------------------------------------------------------------------------#
        #--------------------------------------------------------------------------------------------#


        #------------------------------------ FITH LESSON ------------------------------#
        title2_left = MarkupText(f'Vidéo5:  <span fgcolor="{YELLOW}" > Formule avec coordonnées </span>', color=PINK, font_size=30).move_to(-2.5*DOWN)
        text2_left = MathTex("\\vec{u}\\binom{x_u}{y_u} \\text{.}  \\vec{v}\\binom{x_v}{y_v} = x_u . x_v + y_u . y_v ", font_size=46)
        text2_left.set_color_by_tex_to_color_map({
            "{u}": YELLOW_A,
            "{x_u}": TEAL_C,
            "{x_v}": GREEN_E,
            "{v}": YELLOW_A,
            "{y_u}": TEAL_C,
            "{y_v}": GREEN_E
        })
        #"\\coord{ x_{ \\vec{u} }, y_{ \\vec{u} } } . \\coord{ x_{ \\vec{v} }, y_{\\vec{v} } } =  x_{\\vec{u}} . x_{\\vec{v}} +  y_{\\vec{u}} . y_{\\vec{v} } "
        self.play(FadeIn(title2_left), Write(text2_left))
       
        self.wait()
        
        intro_video1_right = Group( text2_left,  title2_left)
        self.play(intro_video1_right.animate.set_height(0.6).move_to(triangles_right[0].get_center()), run_time = 2)
        intro_video1_right.scale(0.09).move_to( triangles_right[0].get_center() )
        self.wait()
        #---------------------------------- END FITH LESSON INTRO ----------------------------------#
        #-------------------------------------------------------------------------------------------#


        #--------------------------------------- SIXTH LESSON --------------------------------------#
        title3_left = MarkupText(f'Video6:  <span fgcolor="{YELLOW}" > Formule issue d\'identité remarquable </span>', color=PINK, font_size=30).move_to(-2.5*DOWN)
        text3_left=MathTex(
                "\\vec{u} . \\vec{v} = \\frac{1}{2} ( \\norm{ \\vec{u} + \\vec{v}  }^2 - \\norm{ \\vec{u} }^2 - \\norm{\\vec{v}}^2  )"
        )
        #"\\coord{ x_{ \\vec{u} }, y_{ \\vec{u} } } . \\coord{ x_{ \\vec{v} }, y_{\\vec{v} } } =  x_{\\vec{u}} . x_{\\vec{v}} +  y_{\\vec{u}} . y_{\\vec{v} } "
        self.play(FadeIn(title3_left), Write(text3_left))
        framebox1 = SurroundingRectangle(text3_left[0], buff = .1)
        #framebox2 = SurroundingRectangle(text[1], buff = .1)
        
        self.play(
            Create(framebox1)#,  Create(framebox2)
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1, framebox1)
        )
        intro_video2_right = Group( framebox1,  text3_left, title3_left)
        self.play(intro_video2_right.animate.set_height(0.6).move_to(triangles_right[1].get_center()), run_time = 2)
        intro_video1_right.scale(0.09).move_to( triangles_right[1].get_center() )
        self.wait()

        #-------------------------------------- END SIXTH LESSON INTRO------------------------------#
        #--------------------------------------------------------------------------------------------#



        #------------------------------------------ SEVENTH LESSON -----------------------------------#
        title4_left = MarkupText(f'Vidéo7:  <span fgcolor="{YELLOW}" > Formule avec projetté orthogonale </span>', color=PINK, font_size=30).move_to(-2.5*DOWN)
        arrow_1 = Arrow(end=-2*LEFT, start=RIGHT, stroke_color=YELLOW).set_length(5)
       
        arrow_2 = Arrow(start=LEFT, end=1.5*UR, buff=0, stroke_color=PURPLE)
        AH_line = Line(start=LEFT, end=1.4*RIGHT, stroke_color=PINK, stroke_width=13)
        projection_vector_line = DashedLine(start=np.array([1.5, 1.5, 0]) , end=np.array([1.5, 0, 0]))
        angle_droit = Polygon(np.array([1.2, 0, 0]) , np.array([1.2, 0.35, 0]), np.array([1.5, 0.35, 0]), np.array([1.5, 0, 0]))
        

        text_A = Text("A").scale(0.6).next_to(arrow_1, 1.2*DOWN).move_to(1.2*LEFT)
        text_H = Text("H").scale(0.6).move_to(np.array([1.5, -0.3, 0]))
        text_B = Text("B").scale(0.6).next_to(arrow_1, 1.5*RIGHT)
        text_C = Text("C").scale(0.6).next_to(arrow_1, 3.6*UP)

        proj_formula = MathTex("\\vec{AB} . \\vec{AC} = \\vec{AB} . \\vec{AH}  ").to_edge(DR) 
        proj_formula.set_color_by_tex_to_color_map({
            "{AB} ": YELLOW_B,
            "{AC} ": TEAL_B,
            "{AH} ": TEAL_B
        })

        g2 = Group(arrow_1, arrow_2, text_A, text_B, text_C, text_H, proj_formula)
        self.play(FadeIn(title4_left))
        self.play(FadeIn(g2))
        self.wait()
        arrow_2_copy = arrow_2.copy()
        arrow_2_copy.set_color(RED)
        self.play(Transform(arrow_2, arrow_2_copy), FadeIn(AH_line) )
        self.play(FadeIn(projection_vector_line), FadeIn(angle_droit))

        intro_video3_right = Group(g2, title4_left, arrow_2_copy, AH_line, projection_vector_line, angle_droit )

        self.play(intro_video3_right.animate.set_height(0.6).move_to(triangles_right[2].get_center()), run_time = 2)
        intro_video3_right.scale(0.09).move_to( triangles_right[2].get_center() )
        
        self.wait()

        #-------------------------------- END SEVENTH LESSON INTRO------------------------------#
        #----------------------------------------------------------------------------------------#


        #-------------------------------- EIGHTH LESSON ---------------------------------#
        #title5 = MathTex("\\text{Travaux} " , "\\text{ dirigés ").move_to(2.5*UP) 
        title5 = MarkupText(f'Vidéo8:  <span fgcolor="{YELLOW}" > Travaux dirigés - Exercices </span>', color=PINK, font_size=30).move_to(-2.5*DOWN)

        self.play(FadeIn(title5))

        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        ).add_coordinates()

        vector_1 = Vector([2,2], color=YELLOW)
        vector_2 = Vector([-1, 1.5], color=ORANGE)

        vector_1_name = MathTex("\\vec{u}").move_to(np.array([1.5, 1, 0]) )
        vector_2_name = MathTex("\\vec{v}").move_to(0.5*UL)

        self.play(FadeIn(title5) , FadeIn(plane) )
        self.play( FadeIn(vector_1) , FadeIn(vector_1_name))
        self.play( FadeIn(vector_2) , FadeIn(vector_2_name) )
        intro_video4_right = Group( title5, vector_1, vector_2, plane, vector_1_name, vector_2_name) 
        
        self.play(intro_video4_right.animate.set_height(0.6).move_to(triangles_right[3].get_center()), run_time = 2)
        intro_video4_right.scale(0.09).move_to( triangles_right[3].get_center() )
        
        self.wait()

        #------------------------ END EIGTH LESSON INTRO------------------------------#
        #-----------------------------------------------------------------------------#
        
        