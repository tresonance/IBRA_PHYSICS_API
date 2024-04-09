from manim import *
import numpy as np
import random

#------------------------------------------------------------------------------------------#
# video_prodsca_all_courses.py
#       |--> inside this file, we have manim class which describe the "produit scalaire" course 
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


DEMONSTRATION_SIZE = 22

##############################################################################
# Video 1:  Introduction au produit scalaire : norme de vecteur u
##############################################################################
class RappelNormU_1(Scene):
    def construct(self):
        chapitre = MathTex("\\text{Produit }",  "\\text{scalaire}").to_edge(UR)
        chapitre.set_color_by_tex_to_color_map({
            "{Produit } " : TEAL_B,
            "{scalaire}" : TEAL_E
        })

        niveau = MathTex("\\text{ 1ère }").next_to(chapitre, DOWN)
        niveau.set_color_by_tex_to_color_map({
            "{ 1ère }" : PINK
        })
        line_sep = Line().next_to(niveau, DOWN)
        lecon = MathTex("\\text{Formules }", "\\text{d'}", "\\text{Al }", "\\text{Kashi }").next_to(line_sep, DOWN)
        lecon.set_color_by_tex_by_color_map({
            "{Al }": TEAL_E,
            "{Kashi }": TEAL_E
        })

        title = MarkupText(
            f' <span fgcolor="{YELLOW_A}">NORME </span>d\'un  <span fgcolor="{YELLOW_C}">vecteur</span>', color=RED
        ).scale(0.8).to_edge(UP) 
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        ).add_coordinates()

        vector_u = Vector([2,2], color=YELLOW)
        vector_u_abscisse_line = DashedLine(start=np.array([0,0,0]), end=np.array([2,0,0]), stroke_color=TEAL_C)
        vector_u_ordonnee_line = DashedLine(start=np.array([2,2,0]), end=np.array([2,0,0]), stroke_color=GREEN_C)
        vector_u_name = MathTex("\\vec{u}").move_to(np.array([1.5, 1, 0]) )

        plane2 = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )#.add_coordinates()

        vector_u_name2 = MathTex("\\vec{u}", color=YELLOW).move_to(np.array([0.8, 1.3, 0]) )
        vector_u_abscisse_name = MathTex("X", color=TEAL_C).move_to(np.array([1, 0, 0]) )
        vector_u_ordonnee_name = MathTex("Y", color=GREEN_C).move_to(np.array([2, 1, 0]) )

        vector_u_abscisse_name = MathTex("X", color=TEAL_C).move_to(np.array([1, 0, 0]) )
        vector_u_ordonnee_name = MathTex("Y", color=GREEN_C).move_to(np.array([2, 1, 0]) )

        text_norme_u_square = MathTex("\\norm{\\vec{u}}^2", "=", "X^2" ,"+" , "Y^2", font_size=DEMONSTRATION_SIZE)
        text_norme_u_square.set_color_by_tex_to_color_map({
            "{u}": YELLOW, 
            "X^2": TEAL_C,
            "Y^2": GREEN_C
        })
        text_norme_u = MathTex("\\norm{\\vec{u}}", "=", "\\sqrt{X^2 + Y^2}", font_size=30, color=ORANGE)
        text_norme_u.set_color_by_tex_to_color_map({
            "{u}": YELLOW, 
            "X^2": TEAL_C,
            "Y^2": GREEN_C
        })
        
        #self.play(Write(chapitre), Write(niveau) , Write(line_sep), Write(lecon))
        self.play(Write(chapitre), Write(niveau) , Write(line_sep), Write(lecon))
        self.play(FadeIn(title) , GrowFromCenter(plane) )
        self.play( FadeIn(vector_u) , FadeIn(vector_u_name))
     
        self.wait()
        self.play(Transform(plane, plane2))
        self.play(FadeOut(vector_u_name),  FadeIn(vector_u_name2))
        self.play(FadeIn(vector_u_abscisse_line))
        self.wait()
        self.play(FadeIn(vector_u_abscisse_name))
        self.wait()
        self.play(FadeIn(vector_u_ordonnee_line))
        self.play(FadeIn(vector_u_ordonnee_name))
        self.wait()

        group1 = VGroup(
            plane, plane2, vector_u, vector_u_name2, 
            vector_u_abscisse_line, vector_u_abscisse_name, vector_u_ordonnee_line,
            vector_u_ordonnee_name
        ).animate.set_height(3.1).move_to(4*LEFT)
    
        demonstration1 = Text("D'apres La rélation de Pythagore: ", font_size=DEMONSTRATION_SIZE)
        #demonstration2 = MathTex("La \\!norme \\!du \\! vecteur \\! \\vec{u} \\! noté \\! \\norm{\\vec{u}} \\! est: ")
        demonstration2_1 = Text("La norme du vecteur ", font_size=DEMONSTRATION_SIZE)
        demonstration2_2 = Tex("$ \\vec{u} $", font_size=DEMONSTRATION_SIZE, color=YELLOW)
        demonstration2_3 = Text(" notée  ", font_size=DEMONSTRATION_SIZE)
        demonstration2_4 = Tex("$ \\norm{\\vec{u}} $", font_size=DEMONSTRATION_SIZE, color=YELLOW)
        demonstration2_5 = Text(" est: ", font_size=DEMONSTRATION_SIZE)

        demonstration1.move_to(UP + 2*RIGHT)
        text_norme_u_square.next_to(demonstration1, DOWN)
        demonstration2_1.next_to(text_norme_u_square, DOWN)
      
        demonstration2_2.next_to(demonstration2_1, RIGHT)
        demonstration2_3.next_to(demonstration2_2, RIGHT)
        demonstration2_4.next_to(demonstration2_3, RIGHT)
        demonstration2_5.next_to(demonstration2_4, RIGHT)
      
        text_norme_u.next_to(demonstration2_1, 2*DOWN)
       
        

        self.play(group1)
        self.play(FadeIn(demonstration1))

        self.play(FadeIn(text_norme_u_square))

        self.play(FadeIn(demonstration2_1))
        self.play(FadeIn(demonstration2_2))
        self.play(FadeIn(demonstration2_3))
        self.play(FadeIn(demonstration2_4))
        self.play(FadeIn(demonstration2_5))
       
        self.play(FadeIn(text_norme_u))
        framebox1 = SurroundingRectangle(text_norme_u, buff = .1)
        self.play(Create(framebox1))

        attention_1 = MathTex("\\text{Attention:  }", color=RED)
        attention_2 = MathTex( "\\norm{\\vec{u}} ", "\\neq ", "\\vec{u} ")
        attention_2.set_color_by_tex_to_color_map({ 
            "{u} ": YELLOW_E,
            "{mais} " : RED_E
         })
        attention_3 = MathTex( "Note: ", "\\norm{\\vec{u}}^2 ", "= ", "\\vec{u}", ".", "\\vec{u}")
        attention_3.set_color_by_tex_to_color_map({ 
            "{u} ": YELLOW_E,
            "{mais} " : RED_E,
            "{u}" : YELLOW_E
         })

        attention_1.next_to(plane2, 3*DOWN)
        attention_2.next_to(attention_1, DOWN)

        self.play(FadeIn(attention_1))
        self.wait()
        self.play(FadeIn(attention_2))
        self.wait()
        title.scale(0.7) 
        self.play( ApplyMethod(title.shift, 3*LEFT), FadeOut(attention_1), FadeOut(attention_2) )
        
        group_formule = VGroup(demonstration1, text_norme_u_square, text_norme_u_square,
                               demonstration2_1, demonstration2_2, demonstration2_3,
                               demonstration2_4, demonstration2_5 , text_norme_u,
                               framebox1)
        
        my_size = 5
        group1.shift(3*DOWN) 
        self.play(group1)
        self.play(group_formule.animate.set_height(2.5).shift( 5*LEFT + UP), run_time = 1)
        exemple_exo_title = MathTex("\\text{Exemple:}", font_size=my_size, color=TEAL_D )
        exemple_exo1 = MathTex( "\\vec{u}" , "\\text{ a pour coordonne }" ,"\\vec{u}\\binom{2}{2}", font_size=my_size )
        exemple_exo2 = MathTex("\\norm{\\vec{u}}", "=", "\\sqrt{2^2 + 2^2}", font_size=my_size )
        exemple_exo3 = MathTex("\\norm{\\vec{u}}", "=", "\\sqrt{8}", font_size=my_size )
        exemple_exo4 = MathTex("\\norm{\\vec{u}}", "=", "\\sqrt{4}", " * ", "\\sqrt{2}", font_size=my_size )
        exemple_exo5 = MathTex("\\norm{\\vec{u}}", "=", "2\\sqrt{2}", font_size=my_size )
        exemple_exo1.set_color_by_tex_to_color_map({
            "{u}": YELLOW_E, 
            "2^2": TEAL_C
        })
        exemple_exo2.set_color_by_tex_to_color_map({
            "{u}": YELLOW_E, 
            "2^2": TEAL_C
        })
        exemple_exo3.set_color_by_tex_to_color_map({
            "{u}": YELLOW_E, 
            "8": TEAL_C
        })
        exemple_exo4.set_color_by_tex_to_color_map({
            "{u}": YELLOW_E, 
            "2": TEAL_C,
            "{4}": TEAL_E
        })
        exemple_exo5.set_color_by_tex_to_color_map({
            "{u}": YELLOW_E, 
            "{2}": TEAL_E,
            "2": TEAL_C
        })
        exemple_exo_title.move_to(UP+4*RIGHT)
        self.play(FadeOut(group_formule))
        sentence=VGroup(exemple_exo_title, exemple_exo1, exemple_exo2, 
        exemple_exo3, exemple_exo4, exemple_exo5).scale(6.5)

        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        rectangle = Rectangle(color=YELLOW_E)
        rectangle.surround(sentence).scale(6.5)
        self.play(Write(sentence))
        self.play(FadeIn(rectangle))
                        


##############################################################################
# Video 2:  Introduction au produit scalaire : norme de vecteur AB
#############################################################################
class RappelNormAB_2(Scene):
    def construct(self):
        chapitre = MathTex("\\text{Produit }",  "\\text{scalaire}").to_edge(UR)
        chapitre.set_color_by_tex_to_color_map({
            "{Produit } " : TEAL_B,
            "{scalaire}" : TEAL_E
        })

        niveau = MathTex("\\text{ 1ère }").next_to(chapitre, DOWN)
        niveau.set_color_by_tex_to_color_map({
            "{ 1ère }" : PINK
        })
        line_sep = Line().next_to(niveau, DOWN)
        lecon = MathTex("\\text{Formules }", "\\text{d'}", "\\text{Al }", "\\text{Kashi }").next_to(line_sep, DOWN)
        lecon.set_color_by_tex_by_color_map({
            "{Al }": TEAL_E,
            "{Kashi }": TEAL_E
        })

        self.play(Write(chapitre), Write(niveau) , Write(line_sep), Write(lecon))
        chapitre_niveau_group = VGroup(chapitre, niveau, line_sep, lecon)
        
       

        title = MarkupText(
            f' <span fgcolor="{YELLOW_A}">NORME </span>d\'un  <span fgcolor="{YELLOW_C}">vecteur</span>', color=RED
        ).to_edge(UP) 
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            background_line_style={
                "stroke_color": TEAL_E,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        ).add_coordinates()
        
        absc = 3
        ordo = 2
        vector_AB = Vector([absc, ordo], color=YELLOW).move_to(LEFT-DOWN)
        vector_AB_abscisse_line = DashedLine(start=np.array([-2.5,0,0]), end=np.array([0.5,0,0]), stroke_color=BLUE_E)
        vector_AB_ordonnee_line = DashedLine(start=np.array([0.5,2,0]), end=np.array([0.5,0,0]), stroke_color=GREEN_B)
        vector_AB_name = MathTex("\\vec{u}", color=YELLOW).move_to(np.array([-1.5, 1.4, 0]) )
        vector_AB_A_name = MathTex("A").move_to(np.array([-2.7, -0.3, 0]) )
        vector_AB_B_name = MathTex("B").move_to(np.array([0.7, 2.0, 0]) )

        vector_AB_deltaX = MathTex("\\delta_x = X_B - X_A").move_to(
            np.array([-1, -0.5, 0])
        )
        vector_AB_deltaX.set_color_by_tex_to_color_map({
            "X_B": BLUE_E, 
            "X_A": BLUE_B,
        })
        vector_AB_deltaY = MathTex("\\delta_y = Y_B - Y_A").move_to(
            np.array([2.2, 1.0, 0])
        )
        vector_AB_deltaY.set_color_by_tex_to_color_map({
            "Y_B": GREEN_E, 
            "Y_A": GREEN_B,
        })

        plane2 = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )#.add_coordinates()

        vector_AB_name2 = MathTex("\\vec{u}", color=YELLOW).move_to(np.array([0.8, 1.3, 0]) )
        vector_AB_name2.set_color_by_tex_to_color_map({
            "{u}": YELLOW_E
        })
        text_vecteur_AB = MathTex("\\vec{AB}", "=",  "\\binom{X_B - X_A}{Y_B - Y_A}", font_size=DEMONSTRATION_SIZE)
        text_vecteur_AB.set_color_by_tex_to_color_map({
            "{AB}": YELLOW_E,
            "X_B": BLUE_E, 
            "X_A": BLUE_B,
            "Y_B": GREEN_E, 
            "Y_A": GREEN_B
        })
        text_norme_AB_square = MathTex("\\norm{\\vec{AB}}^2", "=", "(X_B - X_A)^2", "+", "(Y_B - Y_A)^2", font_size=DEMONSTRATION_SIZE)
        text_norme_AB_square.set_color_by_tex_to_color_map({
            "{AB}": YELLOW_E,
            "X_B": BLUE_E, 
            "X_A": BLUE_B,
            "Y_B": GREEN_B, 
            "Y_A": GREEN_B,
            "^2": YELLOW_B
        })
        text_norme_AB = MathTex("\\norm{\\vec{AB}}", "=",  "\\sqrt{(X_B - X_A)^2", "+", "(Y_B - Y_A)^2}", font_size=30)
        text_norme_AB.set_color_by_tex_to_color_map({
            "{AB}": YELLOW_E,
            "X_B": BLUE_E, 
            "X_A": BLUE_B,
            "Y_B": GREEN_B, 
            "Y_A": GREEN_B,
            "^2": YELLOW_B
        })

        #self.play(Write(chapitre), Write(niveau) , Write(line_sep), Write(lecon))
        self.play(ApplyMethod(chapitre_niveau_group.to_edge ,DOWN ))
        chapitre_niveau_group_original = chapitre_niveau_group.copy()
        chapitre_niveau_group.animate.scale(0.6)
        self.play(FadeIn(title) , FadeIn(plane) )
        self.play( FadeIn(vector_AB) , FadeIn(vector_AB_name), FadeIn(vector_AB_A_name), FadeIn(vector_AB_B_name))
     
        self.wait()
        self.play(Transform(plane, plane2))
        
        self.play(FadeIn(vector_AB_abscisse_line))
        self.wait()
        self.play(FadeIn(vector_AB_ordonnee_line))
        self.wait()
        self.play(FadeIn( vector_AB_deltaX))
        self.play(FadeIn(  vector_AB_deltaY ))
        self.wait()

        group1 = VGroup(
            plane, plane2, vector_AB, vector_AB_name, vector_AB_A_name, vector_AB_B_name, 
            vector_AB_abscisse_line, vector_AB_ordonnee_line, vector_AB_deltaX, vector_AB_deltaY
        ).animate.set_height(3.1).move_to(4*LEFT)

        demonstration0 = Text("Le vecteur ", font_size=DEMONSTRATION_SIZE)
        demonstration00 = Tex("$ \\vec{AB} $", color=YELLOW, font_size=DEMONSTRATION_SIZE)
        demonstration000 = Text("a pour coordonnée: ", font_size=DEMONSTRATION_SIZE)
        demonstration1 = Text("D'apres La rélation de Pythagore: ", font_size=DEMONSTRATION_SIZE)
        #demonstration2 = MathTex("La \\!norme \\!du \\! vecteur \\! \\vec{u} \\! noté \\! \\norm{\\vec{u}} \\! est: ")
        demonstration2_1 = Text("La norme du vecteur ", font_size=DEMONSTRATION_SIZE)
        demonstration2_2 = Tex("$ \\vec{AB} $", font_size=DEMONSTRATION_SIZE, color=YELLOW)
        demonstration2_3 = Text(" notée  ", font_size=DEMONSTRATION_SIZE)
        demonstration2_4 = Tex("$ \\norm{\\vec{AB}} $", font_size=DEMONSTRATION_SIZE, color=YELLOW)
        demonstration2_5 = Text(" est: ", font_size=DEMONSTRATION_SIZE)

        dec = 0.15
        demonstration0.move_to(UP + dec*LEFT)
        demonstration00.next_to(demonstration0, RIGHT)
        demonstration000.next_to(demonstration00, RIGHT)

        text_vecteur_AB.next_to(demonstration000, 2*DOWN )


        demonstration1.next_to(demonstration0, 4*DOWN )
        text_norme_AB_square.next_to(demonstration1, DOWN)
        demonstration2_1.next_to(text_norme_AB_square, 2*DOWN)
      
        demonstration2_2.next_to(demonstration2_1, RIGHT)
        demonstration2_3.next_to(demonstration2_2, RIGHT)
        demonstration2_4.next_to(demonstration2_3, RIGHT)
        demonstration2_5.next_to(demonstration2_4, RIGHT)

        text_norme_AB.next_to(demonstration2_5, 2*DOWN )
        

        self.play(group1)
        self.play(FadeIn(demonstration0))
        self.play(FadeIn(demonstration00))
        self.play(FadeIn(demonstration000))
       
        self.play(FadeIn(text_vecteur_AB))
        self.play(FadeIn(demonstration1))
        self.play(FadeIn(text_norme_AB_square))
        self.play(FadeOut(chapitre_niveau_group))
        self.play(FadeIn(demonstration2_1))
        self.play(FadeIn(demonstration2_2))
        self.play(FadeIn(demonstration2_3))
        self.play(FadeIn(demonstration2_4))
        self.play(FadeIn(demonstration2_5))
       
        self.play(FadeIn(text_norme_AB))
        framebox1 = SurroundingRectangle(text_norme_AB, buff = .1)
        self.play(Create(framebox1))

        attention_1 = Tex("$ Attention:  $", color=RED)
        attention_2 = Tex("$ \\norm{\\vec{AB}} \\neq \\vec{AB} $", color=YELLOW)

        attention_1.next_to(plane2, 3*DOWN)
        attention_2.next_to(attention_1, DOWN)

        group_formule = VGroup(demonstration0, demonstration00, demonstration000,
        text_vecteur_AB, demonstration1, text_norme_AB_square, demonstration2_1,
         demonstration2_2, demonstration2_3, demonstration2_4, demonstration2_5,
         text_norme_AB, framebox1)

        self.play(FadeIn(attention_1))
        self.wait()
        self.play(FadeIn(attention_2))
        title.scale(0.7) 
        #self.play(FadeOut(chapitre_niveau_group))
        self.play( ApplyMethod(title.shift, 3*LEFT), FadeOut(attention_1), FadeOut(attention_2) )
        
        my_size = 5
        group1.shift(3*DOWN) 
        self.play(group1)
        self.play(group_formule.animate.set_height(2.5).shift( 5*LEFT + UP), run_time = 1)
        exemple_exo_title = MathTex("\\text{Exemple:}", font_size=my_size, color=TEAL_D )
        self.play(FadeIn(chapitre_niveau_group_original))
        exemple_exo1 = MathTex( "Si ", "A\\binom{-2.5}{0}" ,"," ,"B\\binom{0.5}{2}",  "\\text{ on obtient donc }" ,"\\vec{AB}\\binom{X_B - X_A}{Y_B - Y_A}", font_size=my_size )
        exemple_exo1.set_color_by_tex_to_color_map({
            "{-2.5}": BLUE_B,
            "{0}": BLUE_E,
            "0.5": GREEN_B,
            "2": GREEN_E,
            "{AB}": YELLOW_B
        })
        exemple_exo2 = MathTex(  "\\text{ => }" ,"\\vec{AB}\\binom{0.5 - (-2.5)}{2 - 0}", font_size=my_size )
        exemple_exo2.set_color_by_tex_to_color_map({
            "{-2.5}": BLUE_B,
            "{0}": BLUE_E,
            "0.5": GREEN_B,
            "2": GREEN_E,
            "{AB}": YELLOW_B
        })

        exemple_exo3 = MathTex(  "\\text{ => }" ,"\\vec{AB}\\binom{3}{2}", font_size=my_size )
        exemple_exo3.set_color_by_tex_to_color_map({
            "{3}": BLUE_B,
            "{2}": GREEN_B,
            "{AB}": YELLOW_B
        })
        exemple_exo4 = MathTex("\\norm{\\vec{AB}}", "=", "\\sqrt{3^2 + 2^2}", font_size=my_size )
        exemple_exo4.set_color_by_tex_to_color_map({
            "{-2.5}": BLUE_B,
            "{0}": BLUE_E,
            "0.5": GREEN_B,
            "2": GREEN_E,
            "{AB}": YELLOW_B
        })
        exemple_exo5 = MathTex("\\norm{\\vec{AB}}", "=", "\\sqrt{13}", font_size=my_size )
        exemple_exo5.set_color_by_tex_to_color_map({
            "{-2.5}": BLUE_B,
            "{0}": BLUE_E,
            "0.5": GREEN_B,
            "2": GREEN_E,
            "{AB}": YELLOW_B
        })
        exemple_exo1.set_color_by_tex_to_color_map({
            "{AB}": YELLOW_E, 
            "2^2": TEAL_C
        })
        exemple_exo2.set_color_by_tex_to_color_map({
            "{u}": YELLOW_E, 
            "X_B": TEAL_C,
            "X_A": TEAL_C
        })
        exemple_exo3.set_color_by_tex_to_color_map({
            "{u}": YELLOW_E, 
            "2^2": TEAL_C
        })
        exemple_exo4.set_color_by_tex_to_color_map({
            "{u}": YELLOW_E, 
            "8": TEAL_C
        })
        exemple_exo5.set_color_by_tex_to_color_map({
            "{u}": YELLOW_E, 
            "8": TEAL_C
        })
        
        exemple_exo_title.move_to(UP+4*RIGHT)
        self.play(FadeOut(group_formule))
        sentence=VGroup(exemple_exo_title, exemple_exo1, exemple_exo2, 
        exemple_exo3, exemple_exo4, exemple_exo5).scale(6.5)

        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        #chapitre_niveau_group.animate.scale(0.7)
        #self.play(ApplyMethod(chapitre_niveau_group.to_edge ,DOWN ))
        self.play(Write(sentence))
        


##############################################################################
# Video 3:  Introduction au produit scalaire : Formule d'Al Kashi
#                    a^2 = b^2 + c^2 - 2bc Cos(A)
#                    b^2 = a^2 + c^2 - 2ac Cos(B)
#                    c^2 = a^2 + b^2 - 2ab Cos(C)
#############################################################################
class FormuleAlkhashi_3(Scene):
    def construct(self):

        chapitre = MathTex("\\text{Produit }",  "\\text{scalaire}").to_edge(UR)
        chapitre.set_color_by_tex_to_color_map({
            "{Produit } " : TEAL_B,
            "{scalaire}" : TEAL_E
        })

        niveau = MathTex("\\text{ 1ère }").next_to(chapitre, DOWN)
        niveau.set_color_by_tex_to_color_map({
            "{ 1ère }" : PINK
        })
        line_sep = Line().next_to(niveau, DOWN)
        lecon = MathTex("\\text{Formules }", "\\text{d'}", "\\text{Al }", "\\text{Kashi }").scale(0.9).next_to(line_sep, DOWN)
        lecon.set_color_by_tex_to_color_map({
            "{Al }": TEAL_E,
            "{Kashi }": TEAL_E
        })

        self.play(Write(chapitre), Write(niveau) , Write(line_sep), Write(lecon))
        chapitre_niveau_group = VGroup(chapitre, niveau, line_sep, lecon)

        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        ).add_coordinates()

        plane2 = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )#.add_coordinates()
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


        group = VGroup(line_AB, vector_AB_A_name, 
        line_BC, vector_BC_B_name, 
        line_CA, vector_CA_C_name,
        angle_A, angle_B, angle_C
        ).animate.set_height(3.1).move_to(4*LEFT)

        
        self.play(FadeIn(plane))
        self.play(FadeIn(line_AB),  FadeIn(vector_AB_A_name) )
        self.play(FadeIn(line_BC),  FadeIn(vector_BC_B_name) )
        self.play(FadeIn(line_CA),  FadeIn(vector_CA_C_name) )
        self.play(FadeIn(angle_A), FadeIn(angle_B), FadeIn(angle_C) )
        self.play(Transform(plane, plane2))
        self.play(FadeOut(plane))
        self.wait()
        
        self.play(FadeOut(plane2))
        self.play(group)
        #self.play( FadeOut(plane2))

        angle_A.set_color(ORANGE)
        line_BC.set_color(ORANGE)
        
        #-------- formule alkashi 
        line_BC_copy = line_BC.copy().set_color(BLUE)
        self.play(FadeIn(line_BC), FadeIn(angle_A))

        my_size=5
        chapitre_niveau_group_copy = chapitre_niveau_group.copy()
    

        titre_calcul  = MathTex("\\text{Formules d'Al Kashi}", font_size=my_size, color=YELLOW_E)
        formule_BC_a = MathTex("\\text{a}^2", "=", "\\text{b}^2", "+", "\\text{c}^2", "-", "2", ".", "\\text{b}", ".", "\\text{c}", ".", "\\text{cos}", "\\text{(}", "\\widehat{A}", "\\text{)}", font_size=my_size, color=YELLOW)
        rectangle_formule_BC_a = Rectangle()
        
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
        formule_BC = MathTex("\\text{BC}^2", "=", "\\text{AC}^2", "+", "\\text{AB}^2", "-", "\\text{2}", ".", "\\text{AC}", ".", "\\text{AB}", ".", "\\text{cos}", "\\text{(}", "\\widehat{A}", "\\text{)}", font_size=my_size)
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
       
        titre_calcul.shift(UP + 4*RIGHT)
        #line_separator = Line(color=TEAL_E).next_to(formule_BC, DOWN)
        
        sentence=VGroup(titre_calcul, formule_BC_a, formule_BC).scale(6.5)

        sentence.arrange_submobjects(2*DOWN , buff=MED_LARGE_BUFF).shift(2*UP + 3*RIGHT)

        #------
        arrow_double_fleche_a = DoubleArrow(
            start=line_BC.get_start() + np.array([0, 0.2, 0]), 
            end=line_BC.get_end() + np.array([0, 0.2, 0]), stroke_width=1, color=GREEN_E
             )

        arrow_double_fleche_text_a = MathTex("\\text{a}", "=", "\\text{?}").shift(
            arrow_double_fleche_a.get_center() + np.array([0, 0.2, 0])
            )

        arrow_double_fleche_text_a.set_color_by_tex_to_color_map({"{a}" :  GREEN_E})
        
        #------
        arrow_double_fleche_b = DoubleArrow(
            start=line_CA.get_start() + np.array([0.2, 0,  0]), 
            end=line_CA.get_end() + np.array([0.2, 0, 0]), stroke_width=1, color=TEAL_E
             )

        arrow_double_fleche_text_b = MathTex("\\text{b}", "=", "5.8").shift(
            arrow_double_fleche_b.get_center() + np.array([0.2, 0,  0])
            )

        arrow_double_fleche_text_b.set_color_by_tex_to_color_map({"{a}" :  TEAL_E})
        
        #------
        arrow_double_fleche_c = DoubleArrow(
            start=line_AB.get_start() + np.array([-0.2, 0, 0]), 
            end=line_AB.get_end() + np.array([-0.2, 0, 0]), stroke_width=1, color=RED_E
             )

        arrow_double_fleche_text_c = MathTex("\\text{c}", "=", "4.9").shift(
            arrow_double_fleche_c.get_center() + np.array([-0.2, 0, 0])
            )

        arrow_double_fleche_text_c.set_color_by_tex_to_color_map({"{a}" :  RED_E})
        #--------
        
        angle_exemple_value = MathTex("\\text{58}", "\\text{°}").shift(
            angle_A.get_center() + np.array([0.2, 0.3, 0])
            ).set_size(3).set_color(YELLOW)
        angle_exemple_value.set_color_by_tex_to_color_map({
            "{60}": YELLOW_B,
            "{°}": YELLOW_B
        })
        #---------

        self.play(FadeIn(arrow_double_fleche_a)) 
        self.wait()
        self.play(FadeIn(arrow_double_fleche_text_a))  

        self.play(FadeIn(arrow_double_fleche_b)) 
        self.wait()
        self.play(FadeIn(arrow_double_fleche_text_b))  

        self.play(FadeIn(arrow_double_fleche_c)) 
        self.wait()
        self.play(FadeIn(arrow_double_fleche_text_c)) 
        self.wait() 
        self.play(FadeIn(angle_exemple_value))
        self.wait()

        self.play(FadeOut(chapitre_niveau_group))       
        self.play(Write(sentence))
        self.wait()
        
        rectangle_formule_BC_a.surround(formule_BC_a)
        self.play(Create(rectangle_formule_BC_a))

        self.wait()
        
        
        group_with_mesure = VGroup(line_AB, vector_AB_A_name, 
        line_BC, vector_BC_B_name, 
        line_CA, vector_CA_C_name,
        angle_A, angle_B, angle_C,
        arrow_double_fleche_a, arrow_double_fleche_text_a,
        arrow_double_fleche_b, arrow_double_fleche_text_b,
        arrow_double_fleche_c, arrow_double_fleche_text_c,
        angle_exemple_value
        ).animate.set_height(3.1).shift(1.5*DOWN)
        
        self.play(group_with_mesure)
        #self.play(group_with_mesure))
        
        # *****
        self.play(FadeOut(rectangle_formule_BC_a))

        self.play(ApplyMethod(sentence.shift, 7*LEFT))

        decallage = 3*UP+2*RIGHT
        exercice_exemple_calcul = MathTex("\\text{Exemples:}", font_size=my_size).move_to(decallage)
        exercice_exemple_calcul.set_color_by_tex_to_color_map({
            "{Exemples}": YELLOW_E
        })
      
        exercice_exemple1_calcul = MathTex("\\text{BC}^2", "=", "\\text{AC}^2", "+", "\\text{AB}^2", "-", "\\text{2}", ".", "\\text{AC}", ".", "\\text{AB}", ".", "\\text{cos}", "\\text{(}", "\\widehat{A}", "\\text{)}", font_size=my_size).move_to(decallage)
        exercice_exemple1_calcul.set_color_by_tex_to_color_map({
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
        exercice_exemple2_calcul = MathTex("\\text{BC}^2", "=", "\\text{5.8}^2", "+", "\\text{4.9}^2", "-", "\\text{2}", ".", "\\text{(5.8)}", ".", "\\text{(4.9)}", ".", "\\text{cos}", "\\text{(}", "\\text{58°}", "\\text{)}", font_size=my_size).move_to(decallage)
        exercice_exemple2_calcul.set_color_by_tex_to_color_map({
            "{BC}": YELLOW_E, 
            "{cos}": BLUE_E,
            "{(}": BLUE_E,
            "{)}": BLUE_E
        })

        exercice_exemple3_calcul = MathTex("\\text{BC}^2", "\\approx", "\\text{56.143}", font_size=my_size).move_to(decallage)
        exercice_exemple3_calcul.set_color_by_tex_to_color_map({
            "{BC}": YELLOW_E
        })

        exercice_exemple4_calcul = MathTex("\\text{BC}", "\\approx", "\\sqrt{56.143}", font_size=my_size).move_to(decallage)
        exercice_exemple4_calcul.set_color_by_tex_to_color_map({
            "{BC}": YELLOW_E, 
        })

        exercice_exemple5_calcul = MathTex("\\text{BC}", "\\approx", "\\text{7.493}", font_size=my_size).move_to(decallage)
        exercice_exemple5_calcul.set_color_by_tex_to_color_map({
            "{BC}": YELLOW_E, 
            "{7.493}": GREEN
        })

        self.play(FadeIn(chapitre_niveau_group_copy))

        sentence2=VGroup(exercice_exemple_calcul, exercice_exemple1_calcul,
        exercice_exemple2_calcul, exercice_exemple3_calcul,
        exercice_exemple4_calcul, exercice_exemple5_calcul).scale(6.5)

        titre_calcul_copy = titre_calcul.copy().set_color(GREEN).to_edge(UL)
        sentence2.arrange_submobjects(2*DOWN , buff=MED_LARGE_BUFF)
        self.play(FadeOut(sentence),  Write( titre_calcul_copy ))
        self.play(Write(sentence2))
        self.wait()

        #sentence2.scale(0.6).shift(3*DOWN)
        #self.play(Write(sentence2))

        titre_resume  = MathTex("\\text{Formules}", "\\text{d'}" , "\\text{Al}",  "\\text{Kashi}", "\\text{(Je retiens): }", font_size=my_size, color=GREEN)
        #titre_resume.to_edge(UR)
        titre_resume.set_color_by_tex_to_color_map({
            "{Al}": GREEN_E,
             "{Kashi}": GREEN_E
         })
        rectangle_resume = Rectangle(width=3.5, height=2.5 )
        formule_BC_a_resume = MathTex("\\text{a}^2", "=", "\\text{b}^2", "+", "\\text{c}^2", "-", "2", ".", "\\text{b}", ".", "\\text{c}", ".", "\\text{cos}", "\\text{(}", "\\widehat{A}", "\\text{)}", font_size=my_size, color=YELLOW)
        formule_BC_a_resume.set_color_by_tex_to_color_map({
            "{a}": YELLOW_E, 
            "{b^2}": TEAL_C,
            "{c^2}": TEAL_C,
            "2": GREEN_E,
            "{b}": TEAL_C,
            "{c}": TEAL_C, 
            "{cos}": TEAL_B,
            "{(}": TEAL_B,
            "{)}": TEAL_B,
            "{A}": YELLOW_E
        })

        formule_CA_b_resume = MathTex("\\text{b}^2", "=", "\\text{c}^2", "+", "\\text{a}^2", "-", "2", ".", "\\text{c}", ".", "\\text{a}", ".", "\\text{cos}", "\\text{(}", "\\widehat{B}", "\\text{)}", font_size=my_size, color=YELLOW)
        formule_CA_b_resume.set_color_by_tex_to_color_map({
            "{a}": YELLOW_E, 
            "{b^2}": TEAL_C,
            "{c^2}": TEAL_C,
            "2": GREEN_E,
            "{a}": TEAL_C,
            "{c}": TEAL_C, 
            "{cos}": TEAL_B,
            "{(}": TEAL_B,
            "{)}": TEAL_B,
            "{A}": YELLOW_E
        })

        formule_BA_c_resume = MathTex("\\text{c}^2", "=", "\\text{a}^2", "+", "\\text{b}^2", "-", "2", ".", "\\text{a}", ".", "\\text{b}", ".", "\\text{cos}", "\\text{(}", "\\widehat{C}", "\\text{)}", font_size=my_size, color=YELLOW)
        formule_BA_c_resume.set_color_by_tex_to_color_map({
            "{a}": YELLOW_E, 
            "{b^2}": TEAL_C,
            "{c^2}": TEAL_C,
            "2": GREEN_E,
            "{a}": TEAL_C,
            "{b}": TEAL_C, 
            "{cos}": TEAL_B,
            "{(}": TEAL_B,
            "{)}": TEAL_B,
            "{A}": YELLOW_E
        })

        #resume_group = VGroup(titre_resume, formule_BC_a_resume, formule_CA_b_resume,
        #formule_BA_c_resume)
        #resume_group.arrange_submobjects(DOWN , buff=MED_LARGE_BUFF)
        #resume_group.scale(6.5).shift(6*RIGHT + UP)
        scale_value = 5
        titre_resume.scale(scale_value).to_edge(UL)
        self.play( FadeIn( titre_calcul_copy )  )

        formule_BC_a_resume.scale(scale_value)
        formule_BC_a_resume.next_to(titre_resume, DOWN)
        self.play(Write( formule_BC_a_resume  ))

        formule_CA_b_resume.scale(scale_value)
        formule_CA_b_resume.next_to(formule_BC_a_resume, DOWN)
        self.play(Write( formule_CA_b_resume  ))

        formule_BA_c_resume.scale(scale_value)
        formule_BA_c_resume.next_to(formule_CA_b_resume, DOWN)
        self.play(Write( formule_BA_c_resume  ))
        
        rectangle_resume.to_edge(UL)
        self.play(GrowFromCenter(rectangle_resume))



##############################################################################
# Video 4:  Introduction au produit scalaire : Demonstration formule prodSca
#                      uvcos
#############################################################################
class FormuleProduitScalaire_uvcos_4(Scene):
    def construct(self):
        
        chapitre = MathTex("\\text{Produit }",  "\\text{scalaire}").to_edge(UR)
        chapitre.set_color_by_tex_to_color_map({
            "{Produit } " : TEAL_B,
            "{scalaire}" : TEAL_E
        })

        niveau = MathTex("\\text{ 1ère }").next_to(chapitre, DOWN)
        niveau.set_color_by_tex_to_color_map({
            "{ 1ère }" : PINK
        })
        line_sep = Line().next_to(niveau, DOWN)
        lecon = MathTex("\\text{Formules }", "\\text{d'}", "\\text{Al }", "\\text{Kashi }").scale(0.9).next_to(line_sep, DOWN)
        lecon.set_color_by_tex_to_color_map({
            "{Al }": TEAL_E,
            "{Kashi }": TEAL_E
        })

        self.play(Write(chapitre), Write(niveau) , Write(line_sep), Write(lecon))
        chapitre_niveau_group = VGroup(chapitre, niveau, line_sep, lecon)

        line_partage_screen = Line(
            start=np.array([0, 6, 0]) , 
            end=np.array([0, -7, 0]), color=YELLOW_B, stroke_width=4)
        title = MathTex("\\text{Formules }", "\\text{du }",  "\\text{produit }", "\\text{scalaire }").to_edge(UP)
        title.set_color_by_tex_to_color_map({
            "{produit }" : TEAL_E,
            "{scalaire }": TEAL_B
        })
        

        common_start_point = np.array([-6, 0, 0])
        v_start = common_start_point
        v_end = np.array([-5, 3, 0])
        stroke_size = 1

        line_vector_v = Arrow(start=v_start , end=v_end, color=LIGHT_PINK, stroke_width=stroke_size)
        name_vector_v = MathTex("\\vec{v}").move_to(
            line_vector_v.get_center() + np.array([-0.2, 0, 0])
        )
        name_vector_v.set_color_by_tex_to_color_map({
            "{v}" : LIGHT_PINK
        })


        u_start = common_start_point + np.array([-0.1, 0.15, 0])
        u_start_real = common_start_point
        u_end = np.array([-1, 2, 0])
        line_vector_u = Arrow(start=u_start , end=u_end, color=LIGHT_BROWN, stroke_width=stroke_size)
        name_vector_u = MathTex("\\vec{u}").move_to(
            line_vector_u.get_center() + np.array([0, 0.3, 0])
        )
        name_vector_u.set_color_by_tex_to_color_map({
            "{u}" : LIGHT_BROWN
        })

        decallage = np.array([-0.2, -0.2, 0])
        stroke_size = 3
        line_vector_u_v = Arrow(start=v_end + decallage, end=u_end + decallage + np.array([-0.2, 0, 0]), color=GREEN_E, stroke_width=stroke_size)
        name_vector_u_v = MathTex("\\vec{u}", "-", "\\vec{v}").move_to(
            line_vector_u_v.get_center() + np.array([0, 0.3, 0])
        )
        name_vector_u_v.set_color_by_tex_to_color_map({
            "{u}" : GREEN_E,
            "-" : GREEN_E,
            "{v}" : GREEN_E
        })

       
        angle_alpha = Angle(line_vector_u, line_vector_v, radius=0.4,  quadrant=(1,1), other_angle=False).set_color(YELLOW_E)
        text_alpha = MathTex("\\alpha", font_size=36).move_to(angle_alpha.get_center() + np.array([0.2, 0.2, 0]))
        
        group_triangle = VGroup(line_vector_v, line_vector_u, line_vector_u_v,
                         name_vector_u, name_vector_v, name_vector_u_v, angle_alpha,
                         text_alpha)
        
        self.play(Write(chapitre), Write(niveau) , Write(line_sep), Write(lecon))
        #### 
        self.add(line_partage_screen)
        ##### 

        
        self.play(FadeIn(line_vector_u), FadeIn(line_vector_v))
        self.play( 
            Write(title), 
            Write(name_vector_u), 
            Write(name_vector_v),
            #Write(name_vector_u_v) ,
            FadeIn(angle_alpha),
            Write(text_alpha)
            )
        self.wait()
        my_size = 27
        demonstration = MathTex("\\text{D'après ", "\\text{Al} " , "\\text{Kashi} ", "\\text{(videos precedentes): }", font_size=my_size).next_to(text_alpha, 2*DOWN + 0.125*RIGHT)
        demonstration.set_color_by_tex_to_color_map({
            "{Al} " : GREEN_E,
            "{Kashi} " : GREEN_E
        })
        formule_BC_a = MathTex("\\text{a}^2", "=", "\\text{b}^2", "+", "\\text{c}^2", "-", "2", ".", "\\text{b}", ".", "\\text{c}", ".", "\\text{cos}", "\\text{(}", "\\widehat{A}", "\\text{)}", font_size=my_size, color=YELLOW).next_to(demonstration, DOWN )
        formule_BC_a.set_color_by_tex_to_color_map({
            "{a}": YELLOW_E, 
            "{b^2}": TEAL_C,
            "{c^2}": TEAL_C,
            "2": GREEN_E,
            "{b}": TEAL_C,
            "{c}": TEAL_C, 
            "{cos}": TEAL_B,
            "{(}": TEAL_B,
            "{)}": TEAL_B,
            "{A}": YELLOW_E
        })

        implik = MathTex("\\text{ <=> }").next_to(formule_BC_a, DOWN )
        implik.set_color_by_tex_to_color({
            "{ <=> }" : YELLOW_B
        })

        demonstration1 = MathTex("\\text{( }", "\\vec{u} ", "\\text{ - } ", "\\vec{v}",
        "\\text{ )}^2", "=", "\\norm{\\vec{u}}^2 ", " + " , "\\norm{\\vec{v}}^2 "  ," - ", "2", ".", "\\norm{\\vec{u}}", "." , "\\norm{\\vec{v}}", ".", "\\text{cos}", "(", "\\alpha", ")" , font_size=my_size).next_to(implik, DOWN )
        demonstration1.set_color_by_tex_to_color_map({
            "{u}" : GREEN_E,
            "{ - } " : dot_color,
            "{ + } " : dot_color,
            "{v}" : GREEN_E
        })
        framebox_alkashi_formule = SurroundingRectangle(demonstration1, buff = .1, color=RED_E)
        
        demonstration2 = MathTex("\\text{Par ailleurs, on peut aussi }", "\\text{developper }", ":", font_size=my_size).next_to(demonstration1, DOWN )
        demonstration2.set_color_by_tex_to_color_map({
            "{developper }" : RED_E
        })
       
        demonstration3 = MathTex("\\text{( }", "\\vec{u} ", "\\text{ - } ", "\\vec{v}",
        "\\text{ )}^2", "=", "\\text{( }", "\\vec{u} ", "\\text{ - } ", "\\vec{v}",
        "\\text{ )}" , ".", "\\text{( }", "\\vec{u} ", "\\text{ - } ", "\\vec{v}",
        "\\text{ )}", font_size=my_size).next_to(demonstration2, DOWN )
        demonstration3.set_color_by_tex_to_color_map({
            "{u}" : GREEN_E,
            "-" : GREEN_E,
            "{v}" : GREEN_E
        })
       
        demonstration4 = MathTex("\\text{( }", "\\vec{u} ", "\\text{ - } ", "\\vec{v}",
        "\\text{ )}^2", "=", "\\vec{u}.\\vec{u}", "\\text{ - }", "\\vec{u}.\\vec{v}", "\\text{ - }",
        "\\vec{v}.\\vec{u}" , "\\text{ + } ",  "\\vec{v}.\\vec{v}", font_size=my_size).next_to(demonstration3, DOWN )
        demonstration4.set_color_by_tex_to_color_map({
            "{u}" : GREEN_E,
            "{ - } " : GREEN_E,
            "{ + } " : GREEN_E,
            "{v}" : GREEN_E
        })

        demonstration4_bis = MathTex("\\text{( }", "\\vec{u} ", "\\text{ - } ", "\\vec{v}",
        "\\text{ )}^2", "=", "\\vec{u}.\\vec{u}", "\\text{ - }", "2", "\\vec{u}.\\vec{v}", 
          "\\text{ + }",  "\\vec{v}.\\vec{v}", font_size=my_size).next_to(demonstration3, DOWN ).move_to(3*RIGHT + 3*UP )
        demonstration4_bis.set_color_by_tex_to_color_map({
            "{u}" : GREEN_E,
            "{ - } " : GREEN_E,
            "{ + } " : GREEN_E,
            "{v}" : GREEN_E
        })

        demonstration5 = MathTex("\\text{D'apres video 1: } ", "\\vec{u}.\\vec{u} = \\norm{\\vec{u}}^2", "\\text{ donc: }" ,font_size=my_size).next_to(demonstration4_bis, DOWN )
        demonstration5.set_color_by_tex_to_color_map({
            "{D'apres video 1: }": TEAL_B,
            "{u}" : GREEN_E,
            "-" : GREEN_E,
            "{v}" : GREEN_E
        })
       
        demonstration6 = MathTex("\\text{( }", "\\vec{u} ", "\\text{ - } ", "\\vec{v} ",
        "\\text{ )}^2", "=", "\\norm{\\vec{u}}^2", "\\text{ - }", "\\text{2}", "\\vec{u}", "\\text{.}", "\\vec{v}", "\\text{ + }", "\\norm{\\vec{v}}^2" , font_size=my_size).next_to(demonstration5, DOWN )
        demonstration6.set_color_by_tex_to_color_map({
            "{u} " : GREEN_E,
             "{u}" : GREEN_E,
            "{ - }" : GREEN_E,
            "{ + }" : GREEN_E,
            "{v} " : GREEN_E,
            "{v}" : GREEN_E
        })
       
        
        framebox_developpement = SurroundingRectangle(demonstration6, buff = .1, color=YELLOW_E)
        demonstration8 = MathTex("\\text{En egalisant les deux }", "\\text{expressions} ","\\text{, on obtient: }" , font_size=my_size).next_to(demonstration6, DOWN )
        demonstration8.set_color_by_tex_to_color_map({
            "{expressions} " : GREEN_E,
        })
        
        demonstration9_1 = MathTex("\\norm{\\vec{u}}^2", "\\text{ - }", "\\text{2}", "\\vec{u}", "\\text{.}", "\\vec{v}", "\\text{+}", "\\norm{\\vec{v}}^2"
         ,font_size=my_size).move_to(demonstration8.get_corner(DL)+ DOWN + RIGHT)
        demonstration9_1.set_color_by_tex_to_color_map({
            "{u}" : GREEN_E,
            "{ - }" : GREEN_E,
            "{ + }" : GREEN_E,
            "{v}" : GREEN_E
        })
        framebox_demonstration9_1 = SurroundingRectangle(demonstration9_1, buff = .1, color=YELLOW_E)

        demonstration9_2 = MathTex("\\text{ = }",font_size=my_size).next_to(demonstration9_1, RIGHT )
        demonstration9_2.set_color_by_tex_to_color_map({
           
        })
        demonstration9_3 = MathTex("\\norm{\\vec{u}}^2 ", "\\text{ + }" , "\\norm{\\vec{v}}^2 "  ,"\\text{ - }", "2", ".", "\\norm{\\vec{u}}", "." , "\\norm{\\vec{v}}", ".", "\\text{cos}", "(", "\\alpha", ")" ,font_size=my_size).next_to(demonstration9_2, RIGHT )
        demonstration9_3.set_color_by_tex_to_color_map({
            "{u}" : GREEN_E,
            "{ - }" : GREEN_E,
            "{ + }" : GREEN_E,
            "{v}" : GREEN_E
        })
        framebox_demonstration9_3 = SurroundingRectangle(demonstration9_3, buff = .1, color=RED_E)

        resume_text = MathTex("\\text{Après simplification }", font_size=my_size).move_to(demonstration9_3.get_corner(DL)+ DOWN )
        resume_text.set_color_by_tex_to_color_map({
            "{Après simplification }" : TEAL_A,
        })
        demonstration10 = MathTex("\\vec{u}.\\vec{v}", "=", "\\norm{\\vec{u}}", "." , "\\norm{\\vec{v}}", ".", "\\text{cos}", "(", "\\alpha", ")" , font_size=my_size).next_to(resume_text,  RIGHT)
        demonstration10.set_color_by_tex_to_color_map({
            "{expressions}" : GREEN_E,
        })
        framebox_demonstration10 = SurroundingRectangle(demonstration10, buff = .1, color=ORANGE)

        # coté gauche (de l'écran)
        self.play(
        Write(demonstration), 
        Write(formule_BC_a) , 
        Write(implik))
        self.play(GrowFromCenter(line_vector_u_v))
        self.play(
        Write(name_vector_u_v) ,
        Write(demonstration1), 
        Create(framebox_alkashi_formule),
        Write(demonstration2), 
        Write(demonstration3),
        Write(demonstration4))
        
        #cote droit (de l'ecran)
        self.play(FadeOut(chapitre_niveau_group))
        self.play(
        Write(demonstration4_bis),
        Write(demonstration5),
        Write(demonstration6),
        #Write(demonstration7),
        Create(framebox_developpement))

        self.play(
        Write(demonstration8),
        Write(demonstration9_1),  Write(demonstration9_2),  Write(demonstration9_3),
        Create(framebox_demonstration9_1), Create(framebox_demonstration9_3))

        self.play(
            Write(resume_text),
            Write(demonstration10)
        )
        self.play(FadeIn(framebox_demonstration10))

        exemple_title = MathTex("\\text{ Exemple }", font_size=my_size).next_to(resume_text, DOWN)
        exemple_1 = MathTex("\\norm{ \\vec{u} }", "\\text{ = }", "\\text{5, }", font_size=my_size, color=LIGHT_BROWN).next_to(exemple_title, DOWN)
       
        exemple_2 = MathTex("\\norm{ \\vec{v} }", "\\text{ = }", "\\text{ 3,  }", font_size=my_size, color=LIGHT_PINK ).next_to(exemple_1, RIGHT)
        exemple_3 = MathTex(  "\\alpha", "\\text{ = }", "\\text{37°}", font_size=my_size, color=PINK ).next_to(exemple_2, RIGHT)
        exemple_4 = MathTex("\\norm{\\vec{u}}", "." ,"\\norm{\\vec{v}}",  "." ,"\\text{cos}", "(", "\\alpha" ,")", " = ", 
        "\\text{5 * 3 * cos( 37 °) = }" ,font_size=my_size).next_to(exemple_1, DOWN)
        exemple_4.set_color_by_tex_to_color_map({ 
            "{u}": LIGHT_BROWN,
            "{v}": LIGHT_PINK,
            "{cos}": YELLOW,
        })
        exemple_5 = MathTex("\\text{ 11.481 }" ,font_size=my_size ).next_to(exemple_4, RIGHT)
        

        self.play(Write(exemple_title))
        self.play(Transform(name_vector_u.copy(), exemple_1))
        self.play(Transform(name_vector_v.copy(), exemple_2))
        self.play(Transform(text_alpha.copy(), exemple_3))
        self.play(Write(exemple_4), Write(exemple_5))
        



##############################################################################
# Video 5:  Introduction au produit scalaire : Demonstration formule prodSca
# x1x2 + y1y2
#############################################################################
class FormuleProduitScalaire_x1x2_plus_y1y2_5(Scene):
    def construct(self):
        chapitre = MathTex("\\text{Produit }",  "\\text{scalaire}").to_edge(UR)
        chapitre.set_color_by_tex_to_color_map({
            "{Produit } " : TEAL_B,
            "{scalaire}" : TEAL_E
        })

        my_size = 27
        niveau = MathTex("\\text{ 1ère }").next_to(chapitre, DOWN)
        niveau.set_color_by_tex_to_color_map({
            "{ 1ère }" : PINK
        })
        line_sep = Line().next_to(niveau, DOWN)
        lecon = MathTex("\\text{Formules }", "\\text{sur }", "\\text{les }", "\\text{Coordonnées }").scale(0.7).next_to(line_sep, DOWN)
        lecon.set_color_by_tex_to_color_map({
            "{Coordonnées }": TEAL_E
        })

        self.play(Write(chapitre), Write(niveau) , Write(line_sep), Write(lecon))
        chapitre_niveau_group = VGroup(chapitre, niveau, line_sep, lecon)
        chapitre_niveau_group_copy = chapitre_niveau_group.copy().to_edge(DR)

        rappel_formule_cos1 = MathTex("\\text{Rappel (Vidéo précédente): }" , font_size=my_size).to_edge(UL)
        rappel_formule_cos2 = MathTex("\\vec{u}.\\vec{v}", "=", "\\norm{\\vec{u}}", "." , "\\norm{\\vec{v}}", ".", "\\text{cos}", "(", "\\alpha", ")" , font_size=my_size).next_to(rappel_formule_cos1, DOWN+RIGHT)
        rappel_formule_cos2.set_color_by_tex_to_color_map({
            "{u}" : GREEN_B,
            "{v}" : GREEN_C,
            "{cos}" : GREEN_E
        })
        
        group_rappel_formule_cos = VGroup(rappel_formule_cos1, rappel_formule_cos2)
        framebox_group_rappel_formule_cos = SurroundingRectangle(group_rappel_formule_cos, buff = .1, color=ORANGE)

        line_partage_screen = Line(
            start=np.array([0, 6, 0]) , 
            end=np.array([0, -7, 0]), color=YELLOW_B, stroke_width=4)
        
       
        self.add(line_partage_screen)
        self.play( Write(rappel_formule_cos1), Write(rappel_formule_cos2) )
        self.play(FadeIn(framebox_group_rappel_formule_cos))

        number_plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": TEAL_E,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        ).scale(0.4)

        my_size = 8
        scale_factor = 3.5
        
        origine_name = MathTex("\\text{0}",  color=BLUE, stroke_width=1).move_to(
             np.array([-0.1, -0.1, 0])
        ).scale(0.5)

        vector_1 = Vector([-2,2], color=YELLOW_E, stroke_width=2)
        vector_2 = Vector([2, 1.5], color=PURPLE_B, stroke_width=2)

        vector_unitaire_abscisse = Vector([1, 0], color=ORANGE, stroke_width=2)
        vector_unitaire_ordonnee = Vector([0, 1], color=ORANGE, stroke_width=2)

        vector_unitaire_abscisse_name = MathTex("\\vec{i}", color=ORANGE, stroke_width=1).move_to(
             vector_unitaire_abscisse.get_center() + np.array([0, -0.2, 0])
        ).scale(0.5)
        vector_unitaire_ordonnee_name = MathTex("\\vec{j}", color=ORANGE, stroke_width=1).move_to(
             vector_unitaire_ordonnee.get_center() + np.array([-0.3, -0.2, 0])
        ).scale(0.5)

        group_graphic = VGroup(origine_name, number_plane, vector_1, vector_2, vector_unitaire_abscisse,
         vector_unitaire_ordonnee, vector_unitaire_abscisse_name, vector_unitaire_ordonnee_name)

        group_graphic.next_to(framebox_group_rappel_formule_cos, DOWN)

        
        self.play(FadeIn(group_graphic))

        # vector name
        vector_1_name = MathTex("\\vec{u}", color=YELLOW_E).move_to(
             vector_1.get_center() + np.array([0, 0.3, 0])
        )
        vector_2_name = MathTex("\\vec{v}", color=PURPLE_B).move_to(
             vector_2.get_center() + np.array([0, 0.3, 0])
        )

        #coordinates text
        vector_1_coordinate_text = MathTex("\\binom{x_1}{y_1}", color=RED_B).move_to(
            vector_1_name.get_center() + np.array([0.5, 0, 0])
        ).scale(0.5)
        vector_2_coordinate_text = MathTex("\\binom{x_2}{y_2}", color=RED_E).move_to(
            vector_2_name.get_center() + np.array([0.5, 0, 0])
        ).scale(0.5)

        self.play(  
            Write(vector_1_name), 
            FadeIn(vector_1_coordinate_text),

            Write(vector_2_name),
            FadeIn(vector_2_coordinate_text)
        )

        #####
        demonstration1 = MathTex("\\text{Dans }", "\\text{le }", "\\text{répère }", 
        "\\text{(}", "\\text{0}",  ",", "\\vec{i}", ",", "\\vec{j}", "\\text{)}" , ":", font_size=my_size).next_to(
            number_plane, DOWN ).scale(scale_factor)

        demonstration1.set_color_by_tex_to_color_map({
            "{i}": ORANGE,
            "{j}": ORANGE,
            "{0}": ORANGE
         })

        demonstration2 = MathTex("\\vec{u} ", "\\text{ a pour coordonnée } ", 
        "\\vec{u}\\binom{x_1}{y_1}", "\\text{ donc }:" , font_size=my_size).next_to(
            demonstration1, DOWN ).scale(scale_factor)
        demonstration2.set_color_by_tex_to_color_map({
            "{u}": YELLOW_E,
            "{v}": YELLOW_E,
            "{x_1}": YELLOW_E,
            "{x_2}": YELLOW_E,
            "{y_1}": YELLOW_E,
            "{y_2}": YELLOW_E
         })

        demonstration3 = MathTex("\\vec{u} " , "=", "\\text{x}_1", "\\vec{i}", "\\text{ + }", 
        "\\text{y}_1", "\\vec{j}",  font_size=my_size).next_to(
            demonstration2, DOWN ).scale(scale_factor)
        demonstration3.set_color_by_tex_to_color_map({
            "{u}": YELLOW_E,
            "{v}": YELLOW_E,
            "{x}_1": YELLOW_E,
            "{x}_2": YELLOW_E,
            "{y}_1": YELLOW_E,
            "{y}_2": YELLOW_E,
            "{i}": ORANGE,
            "{j}": ORANGE
         })

        demonstration4 = MathTex("\\vec{v} ", "\\text{ a pour coordonnée } ", 
        "\\vec{v}\\binom{x_2}{y_2}", "\\text{ donc }:", font_size=my_size ).next_to(
            demonstration3, DOWN ).scale(scale_factor)
        demonstration4.set_color_by_tex_to_color_map({
            "{u}": YELLOW_E,
            "{v}": YELLOW_E,
            "{x}_1": YELLOW_E,
            "{x}_2": YELLOW_E,
            "{y}_1": YELLOW_E,
            "{y}_2": YELLOW_E
         })

        demonstration5 = MathTex("\\vec{v} " , "=", "\\text{x}_2", "\\vec{i}", "\\text{ + }", 
        "\\text{y}_2", "\\vec{j}" , font_size=my_size).move_to( 2*RIGHT + 3*UP ).scale(scale_factor)
        demonstration5.set_color_by_tex_to_color_map({
            "{u}": YELLOW_E,
            "{v}": YELLOW_E,
            "{x}_1": YELLOW_E,
            "{x}_2": YELLOW_E,
            "{y}_1": YELLOW_E,
            "{y}_2": YELLOW_E,
            "{i}": ORANGE,
            "{j}": ORANGE
         })

        demonstration6 = MathTex("\\text{ Le produit } ", "\\vec{u }", "\\text{ par }", "\\vec{v }", "\\text{ :}", font_size=my_size + 2).next_to(demonstration5, DOWN).scale(scale_factor)
        demonstration6.set_color_by_tex_to_color_map({
            "{u }": YELLOW_E,
            "{v }": YELLOW_E
        })

        

        demonstration7 = MathTex("\\text{     }"  "\\vec{u}", ".", "\\vec{v}", "=", "(", "\\text{x}_1", "\\vec{i}", "\\text{ + }", 
        "\\text{y}_1", "\\vec{j}" ,")", "(", "\\text{x}_2", "\\vec{i}", "\\text{ + }", 
        "\\text{y}_2", "\\vec{j}",")", font_size=my_size + 1).next_to(demonstration6, 2*DOWN).scale(scale_factor)
        
        demonstration7.set_color_by_tex_to_color_map({ 
            "{u}": YELLOW_E,
            "{v}": YELLOW_E,
            "{x}_1": YELLOW_E,
            "{x}_2": YELLOW_E,
            "{y}_1": YELLOW_E,
            "{y}_2": YELLOW_E,
            "{i}": ORANGE,
            "{j}": ORANGE
        })

        demonstration8 = MathTex("\\text{Après dévéloppement, on obtient}", font_size=my_size + 1).next_to(demonstration7, DOWN).scale(scale_factor)
        
        demonstration9 = MathTex("\\vec{u}", ".", "\\vec{v}", "=", "\\text{x}_1", "\\text{x}_2", "\\text{ + }", "\\text{y}_1", "\\text{y}_2" ,font_size=my_size + 1).next_to(demonstration8, 2*DOWN + 0.1*RIGHT).scale(scale_factor)
        
        demonstration9.set_color_by_tex_to_color_map({ 
            "{u}": YELLOW_E,
            "{v}": YELLOW_E,
            "{x}_1": YELLOW_E,
            "{x}_2": YELLOW_E,
            "{y}_1": YELLOW_E,
            "{y}_2": YELLOW_E,
            "{i}": ORANGE,
            "{j}": ORANGE
        })
        framebox_demonstration9 = SurroundingRectangle(demonstration9, buff = .1, color=ORANGE)


        self.play(
            Write(demonstration1),
            Write(demonstration2),
            Write(demonstration3),
            Write(demonstration4))

        self.play(FadeOut( chapitre_niveau_group))
        self.play( ApplyMethod( chapitre_niveau_group_copy.to_edge, DR ))
        
        new_title = MathTex("\\text{Formules }", "\\text{avec }",  "\\text{cosinus }", font_size=my_size).to_edge(UP)
        new_title.set_color_by_tex_to_color_map({
            "{produit }" : TEAL_E,
            "{scalaire }": TEAL_B
        })

        self.play(
            #Transform(title,  new_title),
            Write(demonstration5),
            Write(demonstration6),
            Write(demonstration7)
        )

        self.wait()
        self.play(
             Write(demonstration8),
             Write(demonstration9),
             Create(framebox_demonstration9),
             FadeOut(chapitre_niveau_group_copy)
        )
        
        my_size = 20
        exemple_title = MathTex("\\text{ Exemples }", font_size=my_size + 8, color=TEAL_B).next_to(demonstration9, 2*DOWN + LEFT)
        exemple_1 = MathTex("\\text{soient }", "\\text{A}\\binom{-1}{3}", "\\text{, }",
        "\\text{B}\\binom{2}{5}", "\\text{, }", "\\text{C}\\binom{-5}{3}" ,font_size=my_size + 1, color=TEAL_B).next_to(exemple_title, 2*DOWN)
       
        exemple_1.set_color_by_tex_to_color_map({
            "{A}": YELLOW,
            "{B}": YELLOW,
            "{C}": YELLOW
        })

        exemple_2 = MathTex( "\\vec{AB}\\binom{2 - (-1)}{5 - 3}",  "\\text{= }", "\\binom{3}{2}",
        font_size=my_size + 1, color=TEAL_B).next_to(exemple_1, 2*DOWN)
       
        exemple_2.set_color_by_tex_to_color_map({
            "{AB}": YELLOW,
            "{AC}": YELLOW,
        })

        exemple_3 = MathTex( "\\vec{AC}\\binom{-5 - (-1)}{3 - 3}","\\text{= }", "\\binom{-4}{0}" ,font_size=my_size + 1, color=TEAL_B).next_to(exemple_2, RIGHT)
       
        exemple_3.set_color_by_tex_to_color_map({
            "{AB}": YELLOW,
            "{AC}": YELLOW,
        })

        exemple_4 = MathTex( "\\vec{AB}","\\text{.}", "\\vec{AC}", "\\text{ = }",
        "\\text{3 * (-4)  }", "\\text{ + }", "\\text{2 * 0}" ,font_size=my_size + 1, color=TEAL_B).next_to(exemple_3, 2*DOWN + LEFT)
       
        exemple_4.set_color_by_tex_to_color_map({
            "{AB}": YELLOW,
            "{AC}": YELLOW,
        })

        exemple_5 = MathTex( "\\vec{AB}","\\text{.}", "\\vec{AC}", "\\text{ = }",
        "\\text{-12}" ,font_size=my_size + 1, color=TEAL_B).next_to(exemple_4, 2*DOWN  )
       
        exemple_5.set_color_by_tex_to_color_map({
            "{AB}": YELLOW,
            "{AC}": YELLOW,
        })

        exemples_group = VGroup(exemple_title, exemple_1, exemple_2, exemple_3,
         exemple_4, exemple_5)

        self.play(
            Write(exemple_title),
            Write(exemple_1),
            Write(exemple_2),
            Write(exemple_3),
            Write(exemple_4),
            Write(exemple_5)
        )



#############################################################################
# Video 6:  Introduction au produit scalaire : Demonstration formule prodSca
#                      uv = 1/2(  ||u-v||^2  - ||u||^2 - ||v||^2  )
#############################################################################
class FormuleProduitScalaire_1demi_6(Scene):
    def construct(self):
        my_size = 29
        scale_factor = 3.5
        chapitre = MathTex("\\text{Produit }",  "\\text{scalaire}").to_edge(UR)
        chapitre.set_color_by_tex_to_color_map({
            "{Produit } " : TEAL_B,
            "{scalaire}" : TEAL_E
        })

        niveau = MathTex("\\text{ 1ère }").next_to(chapitre, DOWN)
        niveau.set_color_by_tex_to_color_map({
            "{ 1ère }" : PINK
        })
        line_sep = Line().next_to(niveau, DOWN)
        lecon = MathTex( "\\text{troisième }",  "\\text{formule}").next_to(line_sep, DOWN)
        lecon.set_color_by_tex_by_color_map({
            "{troisième }": TEAL_B,
            "{formule}": TEAL_E
        })


        self.play(Write(chapitre), Write(niveau) , Write(line_sep), Write(lecon))
        chapitre_niveau_group = VGroup(chapitre, niveau, line_sep, lecon)

        rappel_formule_title = MathTex("\\text{Rappel (Vidéos précédentes): }" , font_size=my_size).to_edge(UL)
        rappel_formule_1 = MathTex("\\vec{u}.\\vec{v}", "=", "\\norm{\\vec{u}}", "." , "\\norm{\\vec{v}}", ".", "\\text{cos}", "(", "\\alpha", ")" , font_size=my_size).next_to(rappel_formule_title, DOWN)
        rappel_formule_1.set_color_by_tex_to_color_map({
            "{u}" : GREEN_B,
            "{v}" : GREEN_C,
            "{cos}" : GREEN_E
        })

        rappel_formule_2 = MathTex("\\vec{u}", ".", "\\vec{v}", "=", "\\text{x}_u", "\\text{x}_v", "\\text{ + }", "\\text{y}_u", "\\text{y}_v" ,font_size=my_size + 1).next_to(rappel_formule_1, DOWN)
        rappel_formule_2.set_color_by_tex_to_color_map({ 
            "{u}": YELLOW_E,
            "{v}": YELLOW_E,
            "{x}_u": YELLOW_E,
            "{x}_v": YELLOW_E,
            "{y}_u": YELLOW_E,
            "{y}_v": YELLOW_E,
            "{i}": ORANGE,
            "{j}": ORANGE
        })

        group_rappel_formule = VGroup(rappel_formule_title, rappel_formule_1, rappel_formule_2 )
        framebox_group_rappel_formule= SurroundingRectangle(group_rappel_formule, buff = .1, color=ORANGE)

        line_partage_screen = Line(
            start=np.array([0, 6, 0]) , 
            end=np.array([0, -7, 0]), color=YELLOW_B, stroke_width=4)
        
       
        self.add(line_partage_screen)
        self.play( Write(rappel_formule_title), Write(rappel_formule_1), Write(rappel_formule_2) )
        self.play(FadeIn(framebox_group_rappel_formule))

        demonstration0 = MathTex("\\text{Pour }" ,"\\text{rappel, }" , "\\text{on sait que}", "\\text{ la }", "\\text{norme}",  
         "\\text{ d'un }", "\\text{vecteur }", "\\vec{u}", "\\text{ est }",font_size=my_size).move_to(framebox_group_rappel_formule.get_center() + DOWN + RIGHT)
        demonstration0.set_color_by_tex_to_color_map({
            "{rappel, }": TEAL_E,
            "{u}": ORANGE
        })
        
        demonstration1 = MathTex("\\norm{\\vec{u}}^2", "\\text{=}", "\\vec{u}", "*", "\\vec{u}" , font_size=my_size).next_to(demonstration0, DOWN)
        demonstration1.set_color_by_tex_to_color_map({
            "{u}" : ORANGE,
            "u" : ORANGE
        })

        demonstration2 = MathTex("\\text{ donc }"  , font_size=my_size).next_to(demonstration1, DOWN)
        demonstration2.set_color_by_tex_to_color_map({
            "{ }" : TEAL_E
        })


        demonstration3 = MathTex( "\\norm{ \\vec{u} + \\vec{v} }^2", "=",
        "(","\\vec{u}", " + ", "\\vec{v}" ,")", "(","\\vec{u}", " + ", "\\vec{v}" ,")", font_size=my_size).next_to(demonstration2, DOWN)
        demonstration3.set_color_by_tex_to_color_map({
           "{u}" : PINK,
             "u" : PINK,
            "{v}" : GREEN_C,
            "v" : GREEN_C,
            "{cos}" : GREEN_E
        })

        demonstration4 = MathTex( "\\norm{ \\vec{u} + \\vec{v} }^2", "=",
         "\\vec{u}",".", "\\vec{u}", "\\text{ + }", "\\vec{u}", "*", "\\vec{v}", "\\text{ + }", "\\vec{v}", "*", "\\vec{u}",
         "\\text{ + }",  "\\vec{v}",".", "\\vec{v}" ,font_size=my_size).next_to(demonstration3, DOWN)
        demonstration4.set_color_by_tex_to_color_map({
           "{u}" : PINK,
             "u" : PINK,
            "{v}" : GREEN_C,
            "v" : GREEN_C,
            "{cos}" : GREEN_E
        })

        demonstration5 = MathTex("\\text{ <=> }", font_size=my_size).next_to(demonstration4, DOWN)
        demonstration5.set_color_by_tex_to_color_map({
    
        })

        demonstration6 = MathTex( "\\norm{ \\vec{u} + \\vec{v} }^2", "=",
         "\\norm{\\vec{u} }^2", "\\text{ + }", "\\text{2}", "*","\\vec{u}", "*", "\\vec{v}",  "\\text{ + }",  "\\norm{ \\vec{v} }^2" ,font_size=my_size).next_to(demonstration5, DOWN)
        demonstration6.set_color_by_tex_to_color_map({
           "{u}" : PINK,
             "u" : PINK,
            "{v}" : GREEN_C,
            "v" : GREEN_C,
            "{cos}" : GREEN_E
        })

        demonstration7 = MathTex("\\text{ <=> }", font_size=my_size).next_to(demonstration6, DOWN)
        demonstration7.set_color_by_tex_to_color_map({
    
        })

        demonstration8 = MathTex(  "\\vec{u}}" ,"." , "\\vec{v} }", "=", "\\frac{1}{2}", "\\text{(}",
         "\\norm{\\vec{u} + \\vec{v} }^2", " - " ,"\\norm{ \\vec{u} }^2", "\\text{ - }" ,"\\norm{ \\vec{v} }^2",  "\\text{)}" ,font_size=my_size).next_to(demonstration7, DOWN)
        demonstration8.set_color_by_tex_to_color_map({
           "{u}" : PINK,
             "u" : PINK,
            "{v}" : GREEN_C,
            "v" : GREEN_C,
            "{cos}" : GREEN_E
        })

        self.play(Write(demonstration0), Write(demonstration1), Write(demonstration2),
        Write(demonstration3))

        self.play(Write(demonstration4), Write(demonstration5), Write(demonstration6),
        Write(demonstration7), Write(demonstration8))

        framebox = SurroundingRectangle(demonstration8, buff = .1, color=ORANGE)
        self.play(Create(framebox))

        parallelogram = [
            (-4, -2, 0),
            (3, -2, 0),
            (4, 2, 0),
            (-3, 2, 0),
            (-4, -2, 0),
            (4, 2, 0)
        ]

        dot1 = Dot(point=parallelogram[0], radius=0.08, color=ORANGE)
        dot2 = Dot(point=parallelogram[1], radius=0.08, color=ORANGE)
        dot3 = Dot(point=parallelogram[2], radius=0.08, color=ORANGE)
        dot4 = Dot(point=parallelogram[3], radius=0.08, color=ORANGE)
        dot_group = VGroup(dot1, dot2, dot3, dot4)

        # Rappel title 
        group_rappel_formule.scale(0.7)

        # Exemple to calculate
        exemple_title = MathTex("\\text{Exemple:}", font_size=my_size + 3, color=TEAL_D ).move_to(3*RIGHT + 3.3*UP)
        
        polygon  = Polygon(*parallelogram)#.scale(0.4).next_to( exemple_title, DOWN)
        additional_size = 50
        my_color = PURPLE
        exemple_1 = MathTex("\\text{A}", font_size=my_size + additional_size, color=my_color).next_to(dot1, np.array([2, 2, 0]) + dot1.get_center() )
        exemple_2 = MathTex("\\text{B}", font_size=my_size + additional_size, color=my_color).next_to(dot2, np.array([-2, 2,0]) + dot2.get_center() )
        exemple_3 = MathTex("\\text{C}", font_size=my_size + additional_size, color=my_color).next_to(dot3, np.array([-2,-2,0]) + dot3.get_center() )
        exemple_4 = MathTex("\\text{D}", font_size=my_size + additional_size, color=my_color).next_to(dot4, np.array([-1,-2,0]) + dot4.get_center() )
        
        exemples_group = VGroup( polygon, dot_group, exemple_1, exemple_2, exemple_3, exemple_4).scale(0.3).next_to(exemple_title, DOWN)

        self.play(
            Write(exemple_title),
            ApplyMethod(chapitre_niveau_group.to_edge, DR),
            Write(exemples_group),
           
        )

        exemple_5 = MathTex("\\text{4}", font_size=my_size + 1, color=GREEN).move_to( np.array([0, 0, 0]) + 0.5*(dot1.get_center() + dot2.get_center() ))
        exemple_6 = MathTex("\\text{3}", font_size=my_size + 1, color=GREEN).move_to( np.array([0, 0, 0]) + 0.5*(dot2.get_center() + dot3.get_center() ))
        exemple_7 = MathTex("\\text{6}", font_size=my_size + 1, color=GREEN).move_to( np.array([0, 0, 0]) + 0.5*(dot1.get_center() + dot3.get_center() ))

        self.play( Write(exemple_5), Write(exemple_6), Write(exemple_7) )
        scale_factor = 0.7

        exemple_8 = MathTex("\\text{Dans le parallelogramme ABCD: }", font_size=my_size + 1, color=GREEN).next_to(exemples_group, DOWN)
        exemple_9 = MathTex("\\vec{AB}", ".", "\\vec{AD}", "=", "\\frac{1}{2}",
        "(", "\\norm{\\vec{AB} + \\vec{AD}}^2", " - " ,"\\norm{\\vec{AB}}^2", " - ", "\\norm{\\vec{AD}}^2", 
         ")", font_size=my_size + 1 ).next_to(exemple_8, DOWN).scale(scale_factor)
        
        exemple_9.set_color_by_tex_to_color_map({
            "{AB}": YELLOW,
            "{AC}": YELLOW,
            "AB": YELLOW,
            "AC": YELLOW
        })

        exemple_10 = MathTex("\\vec{AB}", ".", "\\vec{AD}", "=", "\\frac{1}{2}",
        "(", "\\norm{\\vec{AB} + \\vec{BC}}^2", " - " ,"\\norm{\\vec{AB}}^2", " - ", "\\norm{\\vec{AD}}^2", 
         ")", font_size=my_size + 1 ).next_to(exemple_9, DOWN).scale(scale_factor)
        
        exemple_10.set_color_by_tex_to_color_map({
            "{AB}": YELLOW,
            "{AC}": YELLOW,
            "AB": YELLOW,
            "AC": YELLOW
        })

        exemple_11 = MathTex("\\vec{AB}", ".", "\\vec{AD}", "=", "\\frac{1}{2}",
        "(", "\\norm{\\vec{AC}}^2", " - " ,"\\norm{\\vec{AB}}^2", " - ", "\\norm{\\vec{BC}}^2", 
         ")", font_size=my_size + 1 ).next_to(exemple_10, DOWN).scale(scale_factor)
        
        exemple_11.set_color_by_tex_to_color_map({
            "{AB}": YELLOW,
            "{AC}": YELLOW,
            "AB": YELLOW,
            "AC": YELLOW
        })


        exemple_14 = MathTex("\\vec{AB}", ".", "\\vec{AD}", "=", "\\frac{1}{2}",
        "(", "\\text{6}^2", " - " ,"\\text{4}^2", " - ", "\\text{3}^2", 
         ")", font_size=my_size + 1 ).next_to(exemple_11, DOWN).scale(scale_factor)
        
        exemple_14.set_color_by_tex_to_color_map({
            "{4}": TEAL_B,
            "{3}": GREEN_E,
            "{6}": GOLD_B,
            "{AB}": YELLOW,
            "{AD}": YELLOW
        })

        exemple_15 = MathTex("\\vec{AB}", ".", "\\vec{AD}", "=", "\\frac{11}{2}",
        font_size=my_size + 1 ).next_to(exemple_14, DOWN).scale(scale_factor)
        
        exemple_15.set_color_by_tex_to_color_map({
            "{4}": TEAL_B,
            "{3}": GREEN_E,
            "{6}": GOLD_B,
            "{AB}": YELLOW,
            "{AD}": YELLOW
        })

        self.play(
            FadeIn(exemple_8),
            FadeIn(exemple_9),
            FadeIn(exemple_10),
            FadeIn(exemple_11),
            FadeOut(chapitre_niveau_group),
            #FadeIn(exemple_12),
            #FadeIn(exemple_13),
            FadeIn(exemple_14),
            FadeIn(exemple_15)
        )



###########################################################################
# Video 7:  Introduction au produit scalaire : Demonstration formule prodSca
#                      formule de projection
#############################################################################
class FormuleProduitScalaire_projection_7(Scene):
    def construct(self):
        my_size = 29
        scale_factor = 3.5
        chapitre = MathTex("\\text{Produit }",  "\\text{scalaire}").to_edge(UR)
        chapitre.set_color_by_tex_to_color_map({
            "{Produit } " : TEAL_B,
            "{scalaire}" : TEAL_E
        })

        niveau = MathTex("\\text{ 1ère }").next_to(chapitre, DOWN)
        niveau.set_color_by_tex_to_color_map({
            "{ 1ère }" : PINK
        })
        line_sep = Line().next_to(niveau, DOWN)
        lecon = MathTex( "\\text{Formule }",  "\\text{avec }", "\\text{projetté}").next_to(line_sep, DOWN)
        lecon.set_color_by_tex_by_color_map({
            "{troisième }": TEAL_B,
            "{formule}": TEAL_E
        })


        self.play(Write(chapitre), Write(niveau) , Write(line_sep), Write(lecon))
        chapitre_niveau_group = VGroup(chapitre, niveau, line_sep, lecon)

        rappel_formule_title = MathTex("\\text{Rappel (Vidéos précédentes): }" , font_size=my_size).to_edge(UL)
        rappel_formule_1 = MathTex("\\vec{u}.\\vec{v}", "=", "\\norm{\\vec{u}}", "." , "\\norm{\\vec{v}}", ".", "\\text{cos}", "(", "\\alpha", ")" , font_size=my_size).next_to(rappel_formule_title, DOWN)
        rappel_formule_1.set_color_by_tex_to_color_map({
            "{u}" : GREEN_B,
            "{v}" : GREEN_C,
            "{cos}" : GREEN_E
        })

        rappel_formule_2 = MathTex("\\vec{u}", ".", "\\vec{v}", "=", "\\text{x}_u", "\\text{x}_v", "\\text{ + }", "\\text{y}_u", "\\text{y}_v" ,font_size=my_size + 1).next_to(rappel_formule_1, DOWN)
        rappel_formule_2.set_color_by_tex_to_color_map({ 
            "{u}": YELLOW_E,
            "{v}": YELLOW_E,
            "{x}_u": YELLOW_E,
            "{x}_v": YELLOW_E,
            "{y}_u": YELLOW_E,
            "{y}_v": YELLOW_E,
            "{i}": ORANGE,
            "{j}": ORANGE
        })

        rappel_formule_3 = MathTex("\\vec{u}", ".", "\\vec{v}", "=", "\\frac{1}{2}", "\\text{(}",
         "\\norm{\\vec{u} + \\vec{v} }^2", " - " ,"\\norm{ \\vec{u} }^2", "\\text{ - }" ,"\\norm{ \\vec{v} }^2",  "\\text{)}" ,font_size=my_size + 1).next_to(rappel_formule_2, DOWN)
        rappel_formule_3.set_color_by_tex_to_color_map({ 
            "{u}": PINK,
            "{v}": PINK,
            "{x}_u": PINK,
            "{x}_v": PINK,
            "{y}_u": PINK,
            "{y}_v": PINK,
            "{i}": PINK,
            "{j}": PINK
        })

        group_rappel_formule = VGroup(rappel_formule_title, rappel_formule_1, rappel_formule_2 , rappel_formule_3)
        framebox_group_rappel_formule= SurroundingRectangle(group_rappel_formule, buff = .1, color=ORANGE)

        line_partage_screen = Line(
            start=np.array([0, 6, 0]) , 
            end=np.array([0, -7, 0]), color=YELLOW_B, stroke_width=4)
        
       
        self.add(line_partage_screen)
        self.play( Write(rappel_formule_title), Write(rappel_formule_1), Write(rappel_formule_2), Write(rappel_formule_3) )
        self.play(FadeIn(framebox_group_rappel_formule))

        #draw vector 
        common_start_point = np.array([-6, 0, 0])
        v_start = common_start_point
        v_end = np.array([-5, 3, 0])
        stroke_size = 1

        line_vector_v = Arrow(start=v_start , end=v_end, color=LIGHT_PINK, stroke_width=stroke_size)
        name_vector_v = MathTex("\\vec{v}").move_to(
            line_vector_v.get_center() + np.array([-0.2, 0, 0])
        )
        name_vector_v.set_color_by_tex_to_color_map({
            "{v}" : LIGHT_PINK
        })


        u_start = common_start_point + np.array([-0.1, 0.15, 0])
        u_start_real = common_start_point
        u_end = np.array([-1, 2, 0])
        line_vector_u = Arrow(start=u_start , end=u_end, color=LIGHT_BROWN, stroke_width=stroke_size)
        name_vector_u = MathTex("\\vec{u}").move_to(
            line_vector_u.get_center() + np.array([0, 0.3, 0])
        )
        name_vector_u.set_color_by_tex_to_color_map({
            "{u}" : LIGHT_BROWN
        })

        norme_v = 10
        proj_angle = Angle(line_vector_v, line_vector_u).get_value()
        projetted_line = DashedLine( np.array([-0.2, -0.3, 0]) + v_end, np.array([-0.8, -0.3, 0]) + line_vector_u.get_center() , color=ORANGE)

        '''
        decallage = np.array([-0.2, -0.2, 0])
        stroke_size = 3
        line_vector_u_v = Arrow(start=v_end + decallage, end=u_end + decallage + np.array([-0.2, 0, 0]), color=GREEN_E, stroke_width=stroke_size)
        name_vector_u_v = MathTex("\\vec{u}", "-", "\\vec{v}").move_to(
            line_vector_u_v.get_center() + np.array([0, 0.3, 0])
        )
        name_vector_u_v.set_color_by_tex_to_color_map({
            "{u}" : GREEN_E,
            "-" : GREEN_E,
            "{v}" : GREEN_E
        })'''

       
        angle_alpha = Angle(line_vector_u, line_vector_v, radius=0.4,  quadrant=(1,1), other_angle=False).set_color(YELLOW_E)
        text_alpha = MathTex("\\alpha", font_size=36).move_to(angle_alpha.get_center() + np.array([0.2, 0.2, 0]))
        
        group_vector = VGroup(line_vector_v, line_vector_u, 
                         name_vector_u, name_vector_v, angle_alpha,
                         text_alpha, projetted_line).shift(3*DOWN)
        
        
        self.play(GrowFromCenter(group_vector))
        self.wait()

        A = MathTex("\\text{ A }", color=GREEN).move_to(line_vector_u.get_projection(line_vector_v.start + np.array([-1, -0.5, 0])))
        B =  MathTex("\\text{ B }", color=GREEN).move_to(v_end + np.array([0, -3 ,0]) )
        C =  MathTex("\\text{ C }", color=GREEN).move_to(u_end + np.array([0, -3 ,0]) )
        H =  MathTex("\\text{ H }", color=GREEN).move_to(line_vector_u.get_center() + np.array([-0.5, -0.5 ,0]) )
        
        self.play(Write(A))
        self.play(Write(B))
        self.play(Write(C))
        self.play(Write(H))

        myradius = 0.02
        d1 = Dot( radius=myradius, fill_opacity=1.0, color=ORANGE).next_to( H.get_center() + np.array([-1, 0.3, 0]))
        d2 = Dot( radius=myradius, fill_opacity=1.0, color=YELLOW).next_to( H.get_center() + np.array([-0.9, 0.1, 0]))
        d3 = Dot( radius=myradius, fill_opacity=1.0, color=GREEN).next_to( H.get_center() + np.array([-0.7, 0.43, 0]))
        
        self.play( FadeIn(d1), FadeIn(d2) , FadeIn(d3))

        l1 = Line(d1, d2)
        l2 = Line(d1, d3)
        self.play( FadeIn (l1)  )
        self.play( FadeIn (l2)  )
        
        scale_factor=0.7
        demonstration1 = MathTex("\\text{H} \\text{ etant le projetté orthoganal de } \\text{B} \\text{ sur } \\text{(AC)}").to_edge(UP + RIGHT).scale(scale_factor)
        demonstration1.set_color_by_tex_to_color_map({ 
            "{H}": GREEN_B,
            "{B}": GREEN_E,
            "{(AC)}": GREEN_C
        })
        demonstration2 = MathTex("\\text{ on a: }").next_to(demonstration1, DOWN).scale(scale_factor)
        demonstration2.set_color_by_tex_to_color_map({ 
            "{AB}": TEAL_B,
            "{AC}": TEAL_E
        })
        demonstration3 = MathTex("\\vec{AB}", "\\text{.}", "\\vec{AC}", "\\text{=}", "\\vec{AH}", "\\text{.}", "\\vec{AC}").next_to(demonstration2, 2*DOWN).scale(scale_factor)
        demonstration3.set_color_by_tex_to_color_map({ 
            "{AB}": TEAL_B,
            "{AC}": TEAL_E
        })

        framebox1 = SurroundingRectangle(demonstration3, buff = .1)
       
        self.play(
            ApplyMethod(chapitre_niveau_group.to_edge, DR),
            Write(demonstration1),
            Write(demonstration2),
            Write(demonstration3)
        )
        self.play(Create(framebox1))