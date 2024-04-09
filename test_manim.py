from manim import *
#from chanim import *
import numpy as np
import random

dir = "/Users/whodunit/GIT_MY_CHANNELS_MATHS/Tle/Geometry/representation_parametric/MANIM/SVG_IMG/"



path1 =  "./SVG_IMG/1.svg"
path2 =  "./SVG_IMG/2.svg"
path3 =  "./SVG_IMG/3.svg"


class Exemple1(Scene):
    def construct(self):
        square = Square(color=ORANGE)
        circle = Circle(color=TEAL)
        line = Line(2*LEFT, 2*RIGHT, color=RED).shift(1.5*DOWN)

        up_square = Square(fill_color=PINK, fill_opacity=0.3).scale(5).next_to(line, UP, buff=0)
        down_square = Square(fill_color=MAROON, fill_opacity=0.3).scale(5).next_to(line, DOWN, buff=0)
        slider = VGroup(up_square, down_square, line)

        # self.add(line, slider, square, circle)
        self.add( slider )

        def get_intersection_updater(no_added_mob, background):
            def updater(added_mob):
                added_mob.become(Intersection(no_added_mob, background)).match_style(no_added_mob)
            return updater
        
        pre_mob = VMobject().add_updater(get_intersection_updater(square, up_square))
        pos_mob = VMobject().add_updater(get_intersection_updater(circle, down_square))
        self.add(pre_mob, pos_mob)

        self.play(slider.animate.shift(UP * 4), run_time=4)
        self.wait()


class Exemple2(Scene):
    def construct(self):
        base = Square(color=ORANGE)
        target = Circle(color=TEAL)
        line = Line(2*UP, 2*DOWN, color=RED).next_to(base, LEFT, buff=1)

        base_background = Square(fill_color=PINK, fill_opacity=0.3).rotate(PI/2).scale(5).next_to(line, RIGHT, buff=0).set_opacity(0)

        target_background = Square(fill_color=MAROON, fill_opacity=0.3).rotate(PI/2).scale(5).next_to(line, LEFT, buff=0).set_opacity(0)

        slider = VGroup( base_background , target_background, line)

        # self.add(line, slider, square, circle)
        self.add( slider )

        def get_intersection_updater(no_added_mob, background):
            def updater(added_mob):
                added_mob.become(Intersection(no_added_mob, background)).match_style(no_added_mob)
            return updater
        
        pre_mob = VMobject().add_updater(get_intersection_updater(base, base_background))
        pos_mob = VMobject().add_updater(get_intersection_updater(target, target_background))
        self.add(pre_mob, pos_mob)

        self.play(slider.animate.shift(RIGHT * 4), run_time=4)
        self.wait()


class Exemple3(Scene):
    def construct(self):
        base_square = Square(color=ORANGE, side_length=5.0)
        base_text = MathTex(r"\lim_{h \rightarrow 0 } \frac{f(x+h)-f(x)}{h}").move_to(base_square.get_center())
        
        pre_mob = VGroup(base_square, base_text)
        pos_mob = Circle(color=TEAL)
        line = Line(2*LEFT, 2*RIGHT, color=RED).shift(1.5*DOWN)

        pre_bk = Square(fill_color=PINK, fill_opacity=0.3).rotate(PI/2).scale(5).next_to(line, UP, buff=0).set_opacity(0)
        pos_bk = Square(fill_color=MAROON, fill_opacity=0.3).rotate(PI/2).scale(5).next_to(line, DOWN, buff=0).set_opacity(0)

        slider = VGroup(pre_bk, pos_bk, line)


        def get_intersection_updater(pre_mob, bk):
            def updater(pos_mob):
                pos_mob.become(Intersection(pre_mob, bk)).match_style(pre_mob)
            return updater
        
        def extract_all_submobs( grp, mob ):
            if len(mob.submobjects) == 0:
                grp.add( mob )
            else:
                for submob in mob.submobjects:
                    extract_all_submobs( grp, submob )


        def get_intersection_updater_sub_recursive(pre_mob, bk):
            grp = VGroup()
            extract_all_submobs(grp, pre_mob )
            def updater(pos_mob):
                pos_mob.become(
                    VGroup(*[
                    Intersection(submob, bk).match_style(submob) 
                    for submob in grp.submobjects 
                    ])
                )
            return updater

        
        pre_mob = VMobject().add_updater(get_intersection_updater_sub_recursive(pre_mob, pre_bk))
        pos_mob = VMobject().add_updater(get_intersection_updater(pos_mob, pos_bk))
        self.add(pre_mob, pos_mob)
        #self.add( slider )

        
        self.add( slider )
        self.play(slider.animate.shift(UP * 4), run_time=4)
        self.wait()


class Exemple4(Scene):
    def construct(self):
        pre_text = Text("BEFORE", color=ORANGE)
        pos_text = Text("AFTER", color=TEAL)
        line = Line(2*LEFT, 2*RIGHT, color=RED).rotate(PI/2).next_to(pre_text, LEFT, buff=1)

        pre_bk = Square().scale(5).next_to(line, RIGHT, buff=0).set_opacity(0)
        pos_bk = Square().scale(5).next_to(line, LEFT, buff=0).set_opacity(0)
        
        slider = VGroup(pre_bk, pos_bk, line)

        # self.add(line, slider, square, circle)
        
        

        def get_intersection_updater(pre_mob, bk):
            def updater(pos_mob):
                pos_mob.become(
                    VGroup(*[
                    Intersection(submob, bk).match_style(submob) 
                    for submob in pre_mob.submobjects 
                    ])
                )
            return updater
        
        pre_mob = VMobject().add_updater(get_intersection_updater(pre_text, pre_bk))
        pos_mob = VMobject().add_updater(get_intersection_updater(pos_text, pos_bk))
        self.add(pre_mob, pos_mob)
        #self.add( slider )

        
        self.add( slider )
        self.play(slider.animate.shift(RIGHT * 4), run_time=4)
        self.wait()



class Exemple5(Scene):
    def construct(self):
        pre_mob = VGroup(
            Circle(), Triangle(), Square(), Star(color=YELLOW)
        ).arrange_in_grid()
        pos_mob = Circle(color=PINK)
        line = Line(3*LEFT, 3*RIGHT, color=RED).rotate(PI/2).next_to(pre_mob, LEFT, buff=1)

        pre_bk = Square().scale(5).next_to(line, RIGHT, buff=0).set_opacity(0)
        pos_bk = Square().scale(5).next_to(line, LEFT, buff=0).set_opacity(0)
        
        slider = VGroup(pre_bk, pos_bk, line)

        # self.add(line, slider, square, circle)
        
        

        def get_intersection_updater_sub(pre_mob, bk):
            def updater(pos_mob):
                pos_mob.become(
                    VGroup(*[
                    Intersection(submob, bk).match_style(submob) 
                    for submob in pre_mob.submobjects 
                    ])
                )
            return updater

        
        def get_intersection_updater(pre_mob, bk):
            def updater(pos_mob):
                pos_mob.become( Intersection(pre_mob, bk).match_style(pre_mob) )
            return updater
        

        pre_mob = VMobject().add_updater(get_intersection_updater_sub(pre_mob, pre_bk))
        pos_mob = VMobject().add_updater(get_intersection_updater(pos_mob, pos_bk))
        self.add(pre_mob, pos_mob)
        #self.add( slider )

        
        self.add( slider )
        self.play(slider.animate.shift(RIGHT * 6), run_time=4)
        self.wait()


class Exemple6(Scene):
    def construct(self):
        pre_mob = VGroup(
            VGroup(Circle(), Triangle()).arrange(RIGHT), 
            Square()
        ).arrange_in_grid()

        pos_mob = Circle(color=PINK)
        line = Line(3*LEFT, 3*RIGHT, color=RED).rotate(PI/2).next_to(pre_mob, LEFT, buff=1)

        pre_bk = Square().scale(5).next_to(line, RIGHT, buff=0).set_opacity(0)
        pos_bk = Square().scale(5).next_to(line, LEFT, buff=0).set_opacity(0)
        
        slider = VGroup(pre_bk, pos_bk, line)

        # self.add(line, slider, square, circle)
        
        def get_intersection_updater_sub(pre_mob, bk):
            def updater(pos_mob):
                pos_mob.become(
                    VGroup(*[
                    Intersection(submob, bk).match_style(submob) 
                    for submob in pre_mob.submobjects 
                    ])
                )
            return updater

        
        def get_intersection_updater(pre_mob, bk):
            def updater(pos_mob):
                pos_mob.become( Intersection(pre_mob, bk).match_style(pre_mob) )
            return updater

        
        def extract_all_submobs( grp, mob ):
            if len(mob.submobjects) == 0:
                grp.add( mob )
            else:
                for submob in mob.submobjects:
                    extract_all_submobs( grp, submob )


        def get_intersection_updater_sub_recursive(pre_mob, bk):
            grp = VGroup()
            extract_all_submobs(grp, pre_mob )
            def updater(pos_mob):
                pos_mob.become(
                    VGroup(*[
                    Intersection(submob, bk).match_style(submob) 
                    for submob in grp.submobjects 
                    ])
                )
            return updater


        pre_mob = VMobject().add_updater(get_intersection_updater_sub_recursive(pre_mob, pre_bk))
        pos_mob = VMobject().add_updater(get_intersection_updater(pos_mob, pos_bk))
        self.add(pre_mob, pos_mob)
        #self.add( slider )

        
        self.add( slider )
        self.play(slider.animate.shift(RIGHT * 8), run_time=4)
        self.wait()


class Exemple7(Scene):
    def construct(self):
        pre_mob = VGroup(
            Circle(), Triangle(), Square(), Star(color=YELLOW)
        ).arrange_in_grid()
        pos_mob = MathTex("\\int_a^b", "x^2", "dx")
        line = Line(3*LEFT, 3*RIGHT, color=RED).rotate(PI/2).next_to(pre_mob, LEFT, buff=1)

        pre_bk = Square().scale(5).next_to(line, RIGHT, buff=0).set_opacity(0)
        pos_bk = Square().scale(5).next_to(line, LEFT, buff=0).set_opacity(0)
        
        slider = VGroup(pre_bk, pos_bk, line)

        # self.add(line, slider, square, circle)
        
        def get_intersection_updater_sub(pre_mob, bk):
            def updater(pos_mob):
                pos_mob.become(
                    VGroup(*[
                    Intersection(submob, bk).match_style(submob) 
                    for submob in pre_mob.submobjects 
                    ])
                )
            return updater

        
        def get_intersection_updater(pre_mob, bk):
            def updater(pos_mob):
                pos_mob.become( Intersection(pre_mob, bk).match_style(pre_mob) )
            return updater

        
        def extract_all_submobs( grp, mob ):
            if len(mob.submobjects) == 0:
                grp.add( mob )
            else:
                for submob in mob.submobjects:
                    extract_all_submobs( grp, submob )


        def get_intersection_updater_sub_recursive(pre_mob, bk):
            grp = VGroup()
            extract_all_submobs(grp, pre_mob )
            def updater(pos_mob):
                pos_mob.become(
                    VGroup(*[
                    Intersection(submob, bk).match_style(submob) 
                    for submob in grp.submobjects 
                    ])
                )
            return updater


        pre_mob = VMobject().add_updater(get_intersection_updater_sub_recursive(pre_mob, pre_bk))
        pos_mob = VMobject().add_updater(get_intersection_updater_sub_recursive(pos_mob, pos_bk))
        self.add(pre_mob, pos_mob)

        
        self.add( slider )
        self.play(slider.animate.shift(RIGHT * 6), run_time=4)
        self.wait()


# ##################################################################
class Video_Intro(Scene):
    def construct(self):
        base_square = Square(color=ORANGE, side_length=5.0)
        base_text = MathTex(r"\lim_{h \rightarrow 0 } \frac{f(x+h)-f(x)}{h}").move_to(base_square.get_center())
        
        pre_mob_1 = VGroup(base_square, base_text)
        pos_mob_1 = Circle(color=TEAL)
        line_1 = Line(2*LEFT, 2*RIGHT, color=RED).shift(1.5*DOWN)

        pre_bk_1 = Square(fill_color=PINK, fill_opacity=0.3).rotate(PI/2).scale(5).next_to(line_1, UP, buff=0).set_opacity(0)
        pos_bk_1 = Square(fill_color=MAROON, fill_opacity=0.3).rotate(PI/2).scale(5).next_to(line_1, DOWN, buff=0).set_opacity(0)

        slider_1 = VGroup(pre_bk_1, pos_bk_1, line_1)


        def get_intersection_updater(pre_mob, bk):
            def updater(pos_mob):
                pos_mob.become(Intersection(pre_mob, bk)).match_style(pre_mob)
            return updater
        
        def extract_all_submobs( grp, mob ):
            if len(mob.submobjects) == 0:
                grp.add( mob )
            else:
                for submob in mob.submobjects:
                    extract_all_submobs( grp, submob )


        def get_intersection_updater_sub_recursive(pre_mob, bk):
            grp = VGroup()
            extract_all_submobs(grp, pre_mob )
            def updater(pos_mob):
                pos_mob.become(
                    VGroup(*[
                    Intersection(submob, bk).match_style(submob) 
                    for submob in grp.submobjects 
                    ])
                )
            return updater

        
        pre_mob_1 = VMobject().add_updater(get_intersection_updater_sub_recursive(pre_mob_1, pre_bk_1))
        pos_mob_1 = VMobject().add_updater(get_intersection_updater(pos_mob_1, pos_bk_1))
        self.add(pre_mob_1, pos_mob_1)
        #self.add( slider )

        
        self.add( slider_1 )
        self.play(slider_1.animate.shift(UP * 4), run_time=4)
        self.wait(1)

        # ................
        pre_mob_2 = pos_mob_1
        pos_mob_2 = MathTex("\\int_a^b", "x^2", "dx")
        line_2 = Line(3*LEFT, 3*RIGHT, color=RED).rotate(PI/2).next_to(pre_mob_2, LEFT, buff=1)

        pre_bk_2 = Square().scale(5).next_to(line_2, RIGHT, buff=0).set_opacity(0)
        pos_bk_2 = Square().scale(5).next_to(line_2, LEFT, buff=0).set_opacity(0)
        
        slider_2 = VGroup(pre_bk_2, pos_bk_2, line_2)

        # self.add(line, slider, square, circle)
        
        def get_intersection_updater_sub(pre_mob, bk):
            def updater(pos_mob):
                pos_mob.become(
                    VGroup(*[
                    Intersection(submob, bk).match_style(submob) 
                    for submob in pre_mob.submobjects 
                    ])
                )
            return updater

        
        def get_intersection_updater(pre_mob, bk):
            def updater(pos_mob):
                pos_mob.become( Intersection(pre_mob, bk).match_style(pre_mob) )
            return updater

        
        def extract_all_submobs( grp, mob ):
            if len(mob.submobjects) == 0:
                grp.add( mob )
            else:
                for submob in mob.submobjects:
                    extract_all_submobs( grp, submob )


        def get_intersection_updater_sub_recursive(pre_mob, bk):
            grp = VGroup()
            extract_all_submobs(grp, pre_mob )
            def updater(pos_mob):
                pos_mob.become(
                    VGroup(*[
                    Intersection(submob, bk).match_style(submob) 
                    for submob in grp.submobjects 
                    ])
                )
            return updater


        pre_mob_2 = VMobject().add_updater(get_intersection_updater_sub_recursive(pre_mob_2, pre_bk_2))
        pos_mob_2 = VMobject().add_updater(get_intersection_updater_sub_recursive(pos_mob_2, pos_bk_2))
        self.add(pre_mob_2, pos_mob_2)

        
        self.add( slider_2 )
        self.play(slider_2.animate.shift(RIGHT * 6), run_time=4)
        self.wait()

