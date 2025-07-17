from manim import *

class Multiplication(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        self.full_text = Text("Brute Force",font_size=36).move_to(UP * 3.6)
        mul = Text("Multiplication",font_size=36).move_to(UP * 3.6)
        line = Line(LEFT * 8, RIGHT * 8).shift(UP * 3.2)
        self.play(Create(line))
        self.play(TransformMatchingShapes(self.full_text,mul))

        blocks = VGroup()
        for i in range(13):
            block = Rectangle(width=1, height=0.75, color=WHITE)
            number = Text(str(i),font = "Times New Roman" ,color=WHITE).scale(0.8).move_to(block.get_center())
            blocks.add(VGroup(block, number))

        # 将所有方块排列成一行
        blocks.arrange(RIGHT, buff=0)

        # 添加 "Suppose you are going to 7 blocks" 文本
        text1 = Text("Suppose you are going to 7 blocks...",font = "Times New Roman" ,color=WHITE).scale(0.8)
        text1.next_to(blocks, DOWN, buff=0.5)

        # 显示方块和文本
        self.play(DrawBorderThenFill(blocks))
        self.play(Write(text1))
        self.wait(2)
        
        # 创建一个黄色透明的正方体
        cube = Rectangle(width=1, height=0.75, fill_color=YELLOW, fill_opacity=0.6, stroke_width=2, stroke_color=WHITE)
        # 设置初始位置（在第0个方块的位置）
        cube.move_to(blocks[0].get_center())
        self.play(FadeIn(cube))

        # 定义目标位置（从位置0到位置7）
        target_positions = [blocks[i].get_center() for i in range(8)]
        text2 = Text("You may go one block by one...",font = "Times New Roman",color=WHITE).move_to(text1)
        self.play(FadeOut(text1),Write(text2))

        # 动画：依次移动正方体到每个目标位置
        for position in target_positions:
            self.play(ApplyMethod(cube.move_to, position, rate_func=rate_functions.linear), run_time=0.4)
            self.wait()
        self.play(ApplyMethod(cube.move_to,blocks[0].get_center(),rate_func=rate_functions.rush_into),run_time=0.4)
        self.wait(2)
        formular = MathTex("2^0,", "2^1,", "2^2,", "2^3,", "...").move_to(text2.get_center())
        formular2 = MathTex("1,2,4,8").move_to(formular.get_center())

        text_part1 = Text("从",font_size=48)
        text_part2 = Text("出发,向右跨",font_size=48)
        text_part3 = Text("步,到达",font_size=48)

        formular3 = MathTex("f[1][0]=2").move_to(formular2.get_center())
        math_1 = MathTex("1")
        math_20 = MathTex("2^0")
        math_21 = MathTex("2^1")
        math_2 = MathTex("2")
        math_22 = MathTex("2")
        math_23 = MathTex("2^0")
        math_3 = MathTex("3")
        line3 = VGroup(text_part1,math_1,text_part2,math_20,text_part3,math_2).arrange(RIGHT,buff=0.2).next_to(formular3,DOWN,buff=0.1)
        self.play(FadeOut(text2),FadeIn(formular))
        self.wait(2)
        self.play(ReplacementTransform(formular,formular2))
        self.wait(2)
        self.play(ReplacementTransform(formular2,formular3),Write(line3))
        self.wait(2)

        formular4 = MathTex("f[1][1]=3").move_to(formular3.get_center())
        line4 = VGroup(text_part1,math_1,text_part2,math_21,text_part3,math_3).arrange(RIGHT,buff=0.2).next_to(formular4,DOWN,buff=0.1)
        self.play(ReplacementTransform(formular3,formular4),ReplacementTransform(line3,line4))
        self.wait(2)

        formular5 = MathTex("f[2][0]=3").move_to(formular4.get_center())
        line5 = VGroup(text_part1,math_22,text_part2,math_23,text_part3,math_3).arrange(RIGHT,buff=0.2).next_to(formular5,DOWN,buff=0.1)
        #text5 = Text("从2出发,向右跨2^0步,到达3").next_to(formular5,DOWN,buff=0.1)
        self.play(ReplacementTransform(formular4,formular5),ReplacementTransform(line4,line5))
        self.wait(2)

        math_i = MathTex("i")
        math_power = MathTex("2^j")
        math_w = MathTex("w")
        formular6 = MathTex("f[i][j]=w").move_to(formular5.get_center())
        line = VGroup(text_part1,math_i,text_part2,math_power,text_part3,math_w).arrange(RIGHT,buff=0.2).next_to(formular6,DOWN,buff=0.1)
        #text6 = Text("从i出发,向右跨2^j步,到达w").next_to(formular6,DOWN,buff=0.1)
        self.play(ReplacementTransform(formular5,formular6),ReplacementTransform(line5,line))
        self.wait(2)

        self.play(FadeOut(formular6,line))

        math_101 = MathTex("2^2 = 2^1 + 2^1").move_to(formular6.get_center())
        self.play(ApplyMethod(cube.move_to,blocks[4].get_center(),rate_func=rate_functions.rush_into),FadeIn(math_101))
        self.wait(1)
        self.play(ApplyMethod(cube.move_to,blocks[0].get_center(),rate_func=rate_functions.rush_from))
        self.play(ApplyMethod(cube.move_to,blocks[2].get_center(),rate_func=rate_functions.rush_from))
        self.play(ApplyMethod(cube.move_to,blocks[4].get_center(),rate_func=rate_functions.rush_from))

        initial_formula = MathTex("f[i][j]", r"=\quad", "f[i][j-1]").next_to(math_101,DOWN,buff=0.1)
        self.add(initial_formula)
        self.wait(1)

        # 创建要添加的部分
        new_part_1 = MathTex("f[")
        new_part_2 = MathTex("]")
        new_part_3 = MathTex("[j-1]")
        # 将新部分放置在合适的位置
        new_part_1.next_to(initial_formula[2], LEFT, buff=0.1)
        new_part_2.next_to(initial_formula[2], RIGHT, buff=0.1)
        new_part_3.next_to(new_part_2,RIGHT,buff=0.1)
        # 播放动画，添加新部分
        self.play(
            Write(new_part_1),
            Write(new_part_2),
            ApplyMethod(cube.move_to,blocks[0].get_center(),rate_func=rate_functions.rush_from)
        )
        self.wait(1)
        self.play(Write(new_part_3))
        self.wait(1)
        formular7 = VGroup(initial_formula,new_part_1,new_part_2,new_part_3)
        self.play(FadeOut(math_101),ApplyMethod(formular7.move_to,blocks.get_center()+UP,rate_func=smooth))

        table_data = [
            ["i,j", "0", "1", "2", "3", "4", "5", "6"],
            ["2^0", "1", "2", "3", "4", "5", "6", "7"],
            ["2^1", "2", "3", "4", "5", "6", "7", "8"],
            ["2^2", "4", "5", "6", "7", "8", "9", "10"],
            ["2^3", "8", "9", "10", "11", "12", "-1", "-1"]
        ]
        table = Table(
            table_data,
            include_outer_lines=True,
            v_buff=0.3,
            h_buff=0.6,
            element_to_mobject=MathTex,
            element_to_mobject_config={"font_size": 36}
        )
        table.next_to(blocks, DOWN, buff=0.5)
        self.play(Create(table))
        self.wait(1)

        # 创建一个黄色透明的正方体
        target_cell = table.get_cell((1,2))
        cube2 = BackgroundRectangle(target_cell,fill_color=YELLOW, fill_opacity=0.5, stroke_width=0)
        # 设置初始位置（在第0个方块的位置）
        self.play(Create(cube2))
        cube3_cell = table.get_cell((5,2))
        self.play(cube2.animate.move_to(cube3_cell.get_center()))
        self.wait(1)
        cube4_cell = table.get_cell((4,2))
        self.play(cube2.animate.move_to(cube4_cell.get_center()))
        self.play(ApplyMethod(cube.move_to,blocks[4].get_center(),rate_func=rate_functions.ease_in_out_cubic))
        self.wait(2)
        cube5_cell = table.get_cell((1,6))
        self.play(cube2.animate.move_to(table.get_cell((1,2)).get_center()))
        width = cube5_cell.get_width()
        height = cube5_cell.get_height()
        #self.play(cube2.animate.move_to(cube5_cell.get_center()))
        self.play(cube2.animate
                  .move_to(cube5_cell.get_center())
                  .stretch_to_fit_width(width)
                  .stretch_to_fit_height(height))
        self.wait(1)
        self.play(cube2.animate.move_to(table.get_cell((5,6)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.play(cube2.animate.move_to(table.get_cell((4,6)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.play(cube2.animate.move_to(table.get_cell((3,6)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.wait(1)
        self.play(cube2.animate.move_to(table.get_cell((1,6)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.play(cube2.animate.move_to(table.get_cell((1,8)).get_center())
                               .stretch_to_fit_height(table.get_cell((1,8)).get_height())
                               .stretch_to_fit_width(table.get_cell((1,8)).get_width()),rate_func = rate_functions.ease_in_out_cubic)
        self.wait(1)
        self.play(cube2.animate.move_to(table.get_cell((5,8)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.wait(0.5)
        self.play(cube2.animate.move_to(table.get_cell((4,8)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.wait(0.5)
        self.play(cube2.animate.move_to(table.get_cell((3,8)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.wait(0.5)
        self.play(cube2.animate.move_to(table.get_cell((2,8)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.wait()
        self.play(ApplyMethod(cube.move_to,blocks[7].get_center(),rate_func=rate_functions.rush_from))
        self.wait()
        self.play(FadeOut(cube,cube2,table,blocks,formular7,shift=DOWN))