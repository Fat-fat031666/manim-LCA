from manim import *

class LCA(Scene):
    def construct(self):
        mul = Text("Multiplication",font_size=36).move_to(UP * 3.6)
        lca = Text("LCA Problem",font_size=36).move_to(UP*3.6)
        line = Line(LEFT * 8, RIGHT * 8).shift(UP * 3.2)
        self.play(Create(line))
        self.play(TransformMatchingShapes(mul,lca))

        text1 = Text("①先跳到同样的深度",font_size=36).move_to(UP*1.5)
        text2 = Text("Jump to the same depth",font_size=24).next_to(text1,DOWN,buff=0.1)
        text3 = Text("②直到他们相遇为止",font_size=36).next_to(text2,DOWN,buff=0.1)
        text4 = Text("Jump until they meet",font_size=24).next_to(text3,DOWN,buff=0.1)
        self.play(Write(text1),Write(text2))
        self.play(Write(text3),Write(text4))
        new_part_1 = Text("用倍增法优化",font_size=36).next_to(text4,DOWN,buff=0.5)
        new_part_2 = Text("Using Multiplication",font_size=24).next_to(new_part_1,DOWN,buff=0.1)
        text5 = VGroup(new_part_1,new_part_2)
        box = SurroundingRectangle(text5, fill_opacity=0,stroke_width=1, buff=0.4, stroke_color=WHITE).next_to(text4,DOWN,buff=0.1)
        self.play(DrawBorderThenFill(box),Write(text5))
        self.wait()
        self.play(FadeOut(box,text1,text2,text3,text4,text5,shift=DOWN))
        self.tree()

    def tree(self):
        class TreeNode(VGroup):
            def __init__(self,value,depth,**kwargs):
                super().__init__(**kwargs)
                self.value = value
                self.depth = depth
                self.circle = Circle(radius = 0.5 ,stroke_width=2,stroke_color=BLUE,fill_opacity=0)
                self.value_label = Text(str(value),font_size=24,color=WHITE).move_to(self.circle.get_center())
                self.depth_value = Text(f"dep={depth}",font_size=18,color=WHITE).next_to(self.value_label,DOWN,buff=0.1)
                self.add(self.circle,self.value_label,self.depth_value)

        #node0根节点
        node0 = TreeNode(0,0).shift(UP * 2.4)
        #self.play(DrawBorderThenFill(node0),run_time=0.8)

        #创建第一层子节点
        node1 = TreeNode(1,1).next_to(node0, DOWN+LEFT*0.5, buff=0.8)
        edge01 = Line(node0.get_bottom(), node1.get_top())
        node2 = TreeNode(2,1).next_to(node0, DOWN+RIGHT*0.5, buff=0.8)
        edge02 = Line(node0.get_bottom(), node2.get_top())
        #将node1 2 edge0102组合vg1
        vg3 = VGroup(node0,node1,node2,edge01,edge02)
        #self.play(DrawBorderThenFill(vg3),run_time=1)

        #创建第二层子节点
        node3 = TreeNode(3,2).next_to(node1,DOWN+1.5*LEFT,buff=0.8)
        edge03 = Line(node1.get_bottom(), node3.get_top())
        node4 = TreeNode(4,2).next_to(node1, DOWN , buff=0.8)
        edge04 = Line(node1.get_bottom(), node4.get_top())
        node5 = TreeNode(5,2).next_to(node2,DOWN,buff=0.8)
        edge05 = Line(node2.get_bottom(), node5.get_top())
        node6 = TreeNode(6,2).next_to(node2, DOWN + 1.5*RIGHT, buff=0.8)
        edge06 = Line(node2.get_bottom(), node6.get_top())
        vg4 = VGroup(node3,node4,node5,node6,edge03,edge04,edge05,edge06)
        #self.play(DrawBorderThenFill(vg4),run_time=1)

        #创建第三层子节点
        node7 = TreeNode(7,3).next_to(node3,DOWN+2*LEFT,buff=0.8)
        edge07 = Line(node3.get_bottom(), node7.get_top())
        node8 = TreeNode(8,3).next_to(node3, DOWN + 0.1*LEFT, buff=0.8)
        edge08 = Line(node3.get_bottom(), node8.get_top())
        node9 = TreeNode(9,3).next_to(node4,DOWN+0.5*LEFT,buff=0.8)
        edge09 = Line(node4.get_bottom(), node9.get_top())
        node10 = TreeNode(10,3).next_to(node4, DOWN , buff=0.8)
        edge10 = Line(node4.get_bottom(), node10.get_top())
        node11 = TreeNode(11,3).next_to(node5,DOWN+0.5*LEFT,buff=0.8)
        edge11 = Line(node5.get_bottom(), node11.get_top())
        node12 = TreeNode(12,3).next_to(node5, DOWN , buff=0.8)
        edge12 = Line(node5.get_bottom(), node12.get_top())
        node13 = TreeNode(13,3).next_to(node6,DOWN,buff=0.8)
        edge13 = Line(node6.get_bottom(), node13.get_top())
        node14 = TreeNode(14,3).next_to(node6, DOWN + RIGHT, buff=0.8)
        edge14 = Line(node6.get_bottom(), node14.get_top())
        vg5 = VGroup(node7,node8,node9,node10,node11,node12,node13,node14,edge07,edge08,edge09,edge10,edge11,edge12,edge13,edge14)
        vgtot = VGroup(vg3,vg4,vg5).scale(0.7).move_to(2*LEFT)
        self.play(DrawBorderThenFill(vgtot),run_time=1)
        self.wait()

        part_ch = MathTex("f[i][j]",font_size=36)
        part_ch2 = Text("代表结点i第",font_size=24)
        part_ch3 = MathTex("2^j",font_size=36)
        part_ch4 = Text("个父亲",font_size=24)
        group_ch = VGroup(part_ch,part_ch2,part_ch3,part_ch4).arrange(RIGHT, buff=0.2).next_to(vgtot,DOWN)

        part1 = MathTex("f[i][j]",font_size=36)
        part2 = Text("means the",font_size=24,font="Times New Roman")
        part3 = MathTex("2^j",font_size=36)
        part4 = Text("th father of i",font_size=24,font="Times New Roman")
        group = VGroup(part1, part2, part3, part4).arrange(RIGHT, buff=0.2).next_to(group_ch,DOWN)
        self.play(Write(group),Write(group_ch))
        self.wait()
        self.play(FadeOut(group,group_ch))
        lca_1_14 = Text("LCA(1,14)")

        table_data = [
            ["i,j", "1", "14"],
            ["2^0", "0", "6"],
            ["2^1", "-1", "2"],
            ["2^2", "-1", "0"],
            ["2^3", "-1", "-1"]
        ]
        table = Table(
            table_data,
            include_outer_lines=True,
            v_buff=0.3,
            h_buff=0.6,
            element_to_mobject=MathTex,
            element_to_mobject_config={"font_size": 36}
        )
        highlight1 = Circle(radius = 0.35 ,color = YELLOW,fill_opacity=0.5,stroke_width = 2,stroke_color=WHITE).move_to(node1.get_center())
        highlight14 = Circle(radius = 0.35 ,color = YELLOW,fill_opacity=0.5,stroke_width = 2,stroke_color=WHITE).move_to(node14.get_center())
        table.next_to(vgtot, RIGHT, buff=1.0)
        lca_1_14.next_to(table,UP,buff=0.2)
        self.play(Create(table),Write(lca_1_14),FadeIn(highlight1),FadeIn(highlight14))
        self.wait(1)
        self.play(highlight14.animate.scale(1.5),rate_func= rate_functions.ease_in_out_cubic,run_time=0.8)
        self.play(highlight14.animate.scale(1/1.5),rate_func= rate_functions.ease_in_out_cubic,run_time=0.8)
        target_cell = table.get_cell((1,3))
        cube2 = BackgroundRectangle(target_cell,fill_color=YELLOW, fill_opacity=0.5, stroke_width=0)
        self.play(FadeIn(cube2))
        self.play(cube2.animate.move_to(table.get_cell((5,3)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.wait(0.5)
        self.play(cube2.animate.move_to(table.get_cell((4,3)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.wait(0.5)
        self.play(cube2.animate.move_to(table.get_cell((3,3)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.wait(0.5)
        self.play(highlight14.animate.move_to(node2.get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.play(FadeOut(highlight1,highlight14,table,lca_1_14,cube2))

        highlight7 = Circle(radius = 0.35 ,color = YELLOW,fill_opacity=0.5,stroke_width = 2,stroke_color=WHITE).move_to(node7.get_center())
        highlight8 = Circle(radius = 0.35 ,color = YELLOW,fill_opacity=0.5,stroke_width = 2,stroke_color=WHITE).move_to(node8.get_center())

        table_data = [
            ["i,j", "7", "8"],
            ["2^0", "3", "3"],
            ["2^1", "1", "1"],
            ["2^2", "-1", "-1"],
            ["2^3", "-1", "-1"]
        ]
        table = Table(
            table_data,
            include_outer_lines=True,
            v_buff=0.3,
            h_buff=0.6,
            element_to_mobject=MathTex,
            element_to_mobject_config={"font_size": 36}
        )
        table.next_to(vgtot, RIGHT, buff=1.0)
        lca_7_8 = Text("LCA(7,8)").next_to(table,UP,buff=0.2)
        cube3 = BackgroundRectangle(table.get_cell((5,2)),fill_color=YELLOW, fill_opacity=0.5, stroke_width=0)
        cube4 = BackgroundRectangle(table.get_cell((5,3)),fill_color=YELLOW, fill_opacity=0.5, stroke_width=0)
        self.play(FadeIn(table,highlight7,highlight8),Write(lca_7_8),FadeIn(cube3,cube4))
        self.wait()
        
        self.play(highlight7.animate.scale(1.5),highlight8.animate.scale(1.5),ate_func= rate_functions.ease_in_out_cubic,run_time=0.8)
        self.play(highlight7.animate.scale(1/1.5),highlight8.animate.scale(1/1.5),rate_func= rate_functions.ease_in_out_cubic,run_time=0.8)
        self.play(highlight7.animate.move_to(node1.get_center()),highlight8.animate.move_to(node1.get_center()),
                cube3.animate.move_to(table.get_cell((3,2)).get_center()),
                cube4.animate.move_to(table.get_cell((3,3)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.play(highlight7.animate.move_to(node7.get_center()),highlight8.animate.move_to(node8.get_center()),
                cube3.animate.move_to(table.get_cell((5,2)).get_center()),
                cube4.animate.move_to(table.get_cell((5,3)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.wait(2)
        text1 = Text("①先跳到同样的深度",font_size=36).next_to(vgtot,DOWN)
        text2 = Text("Jump to the same depth",font_size=24).next_to(text1,DOWN,buff=0.1)
        text3 = Text("②直到他们相遇为止",font_size=36).next_to(text1,RIGHT,buff=0.5)
        text4 = Text("Jump until they meet up",font_size=24).next_to(text3,DOWN,buff=0.1)
        self.play(FadeIn(text1,text2,text3,text4))
        text5 = Text("②尽量往上跳但不能相遇",font_size=36).move_to(text3.get_center())
        text6 = Text("Jump so that they don't meet",font_size=24).move_to(text4.get_center())
        self.play(ReplacementTransform(text3,text5),ReplacementTransform(text4,text6))
        self.play(highlight7.animate.move_to(node0.get_center()),highlight8.animate.move_to(node0.get_center()),
                cube3.animate.move_to(table.get_cell((4,2)).get_center()),
                cube4.animate.move_to(table.get_cell((4,3)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.play(highlight7.animate.move_to(node7.get_center()),highlight8.animate.move_to(node8.get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.play(highlight7.animate.move_to(node1.get_center()),highlight8.animate.move_to(node1.get_center()),
                cube3.animate.move_to(table.get_cell((3,2)).get_center()),
                cube4.animate.move_to(table.get_cell((3,3)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.play(highlight7.animate.move_to(node7.get_center()),highlight8.animate.move_to(node8.get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.play(highlight7.animate.move_to(node3.get_center()),highlight8.animate.move_to(node3.get_center()),
                cube3.animate.move_to(table.get_cell((2,2)).get_center()),
                cube4.animate.move_to(table.get_cell((2,3)).get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.play(highlight7.animate.move_to(node7.get_center()),highlight8.animate.move_to(node8.get_center()),rate_func = rate_functions.ease_in_out_cubic)
        highlight3 = Circle(radius = 0.35 ,color = BLUE,fill_opacity=0.5,stroke_width = 2,stroke_color=WHITE).move_to(node3.get_center())
        self.play(FadeOut(highlight3))
        self.play(FadeOut(vgtot,table,lca_7_8,highlight7,highlight8,cube3,cube4,text1,text2,text5,text6))
        self.wait(1)