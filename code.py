from manim import *

class code(Scene):
    def construct(self):
        lca = Text("LCA Problem",font_size=36).move_to(UP*3.6)
        c = Text("Realizing By C++",font_size=36).move_to(UP*3.6)
        line = Line(LEFT * 8, RIGHT * 8).shift(UP * 3.2)
        self.play(Create(line))
        self.play(TransformMatchingShapes(lca,c))

        code = Code("test.cpp",language="C++",background="window",tab_width=4).scale(0.55).move_to(LEFT*3+DOWN*0.5)
        self.play(Write(code),run_time=3)

        chain = Text("通过链式前向星构建树",font_size=24).next_to(code, RIGHT, buff=0.8)
        line1 = MathTex(r"\texttt{for(int i=head[v]; i; i=e[i].next)}", font_size=24)
        line2 = MathTex(r"\texttt{attr[i]}", font_size=24)

        # 使用 VGroup 组合并右对齐
        code_text = VGroup(line1, line2).arrange(
            DOWN,               # 垂直排列
            aligned_edge=LEFT, # 左对齐
            buff=0.3            # 行间距
        )
        code_text.next_to(chain, DOWN, buff=0.3)

        self.play(Write(chain))
        self.wait(1)
        self.play(Write(code_text))
        self.wait(2)
        self.play(FadeOut(chain), FadeOut(code_text))
        self.wait(2)
        self.play(FadeOut(code), run_time=2)

        code2 = Code("testlca.cpp",language="C++",background="window",tab_width=4).scale(0.55).move_to(LEFT*4)
        self.play(Write(code2),run_time=3)
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
        vgtot = VGroup(vg3,vg4,vg5).scale(0.7).move_to(2.8*RIGHT)
        self.play(DrawBorderThenFill(vgtot),run_time=1)
        self.wait()

        highlight1 = Circle(radius = 0.35 ,color = YELLOW,fill_opacity=0.5,stroke_width = 2,stroke_color=WHITE).move_to(node3.get_center())
        highlight13 = Circle(radius = 0.35 ,color = YELLOW,fill_opacity=0.5,stroke_width = 2,stroke_color=WHITE).move_to(node13.get_center())
        self.play(FadeIn(highlight1),FadeIn(highlight13))
        self.wait(1)

        self.play(highlight1.animate.move_to(highlight13.get_center()),highlight13.animate.move_to(highlight1.get_center()))
        self.wait(2)
        self.play(highlight1.animate.move_to(node2.get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.play(highlight1.animate.move_to(node13.get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.play(highlight1.animate.move_to(node6.get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.play(highlight13.animate.move_to(node1.get_center()),highlight1.animate.move_to(node2.get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.play(highlight13.animate.move_to(node0.get_center()),highlight1.animate.move_to(node0.get_center()),rate_func = rate_functions.ease_in_out_cubic)
        self.play(highlight13.animate.move_to(node1.get_center()),highlight1.animate.move_to(node2.get_center()),rate_func = rate_functions.ease_in_out_cubic)
        highlight = Circle(radius = 0.35 ,color = BLUE,fill_opacity=0.5,stroke_width = 2,stroke_color=WHITE).move_to(node0.get_center())
        self.play(FadeIn(highlight))
        self.wait(3)
        self.play(FadeOut(vgtot,highlight,highlight1,highlight13))

        code_text = [
            "dfs(tree_root, 0);",
            "lca(x, y);"
        ]
        code_lines = VGroup(*[
            Text(line, font="JetBrains Mono", color=WHITE, font_size=24)
            for line in code_text
        ])

        # 垂直排列并设置行间距
        code_lines.arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(RIGHT*2)
        self.play(FadeIn(code_lines))
        self.wait(2)