from manim import *


class Latex (Scene):
    def construct (self):
        lca_text = Text("LCA",font_size = 72)
        self.full_text = Text("Least Common Ancestors",font_size=72)

        lca_text.move_to(ORIGIN)
        self.full_text.move_to(ORIGIN)

        self.play(Write(lca_text))
        self.wait()
        self.play(TransformMatchingShapes(lca_text,self.full_text))
        self.wait()
        #分割线
        line = Line(LEFT * 8, RIGHT * 8).shift(UP * 3.5)

        #LCA文字上移并创建直线
        self.play(self.full_text.animate.move_to(UP * 3.8).scale(0.5),Create(line))
        self.wait()
        self.build_tree()



    def build_tree(self):
        #定义节点类
        class Node(VGroup):
            def __init__(self,number,**kwargs):
                super().__init__(**kwargs)
                self.circle = Circle(radius = 0.3,stroke_width=1,stroke_color = BLUE,fill_opacity=1,fill_color=BLUE)
                self.label = Text(str(number),font_size=24)
                self.label.move_to(self.circle.get_center())
                self.add(self.circle,self.label)

        #node创建树的节点 edge创建边
        node0 = Node(0).shift(UP * 1.5)
        self.play(DrawBorderThenFill(node0),run_time=0.8)
        self.wait()
        node1 = Node(1).next_to(node0, DOWN + LEFT, buff=1.5)
        edge01 = Line(node0.get_bottom(), node1.get_top())
        node2 = Node(2).next_to(node0, DOWN + RIGHT, buff=1.5)
        edge02 = Line(node0.get_bottom(), node2.get_top())
        #将node1 2 edge0102组合vg1
        vg1 = VGroup(node1,node2,edge01,edge02)
        self.play(DrawBorderThenFill(vg1),run_time=1)
        self.wait()

        node3 = Node(3).next_to(node1, DOWN + LEFT, buff=1.5)
        edge13 = Line(node1.get_bottom(), node3.get_top())
        node4 = Node(4).next_to(node1, DOWN + RIGHT, buff=1.5)
        edge14 = Line(node1.get_bottom(), node4.get_top())
        #将node3 4 edge0304组合vg2
        vg2 = VGroup(node3,node4,edge13,edge14)
        self.play(DrawBorderThenFill(vg2),run_time=0.5)
        self.wait()
        self.play(
            ScaleInPlace(node3, scale_factor=2),
            ScaleInPlace(node4, scale_factor=2),
            run_time=1  # 设置动画持续时间为 2 秒
        )
        self.wait()
        self.play(node1.animate.scale(2),run_time=1.5)
        self.play(
            ScaleInPlace(node1, scale_factor=0.5),
            ScaleInPlace(node3, scale_factor=0.5),
            ScaleInPlace(node4, scale_factor=0.5),
            run_time=1  # 设置动画持续时间为 2 秒
        )
        vg3 = VGroup(node0,vg1,vg2)
        brute_text = Text("Brute Force",font_size=36).move_to(self.full_text)
        self.play(vg3.animate.shift(DOWN),FadeOut(vg3,run_time=2),TransformMatchingShapes(self.full_text,brute_text))
        self.brute_tree()

    def brute_tree(self):
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
        self.play(DrawBorderThenFill(node0),run_time=0.8)

        #创建第一层子节点
        node1 = TreeNode(1,1).next_to(node0, DOWN+LEFT*0.5, buff=0.8)
        edge01 = Line(node0.get_bottom(), node1.get_top())
        node2 = TreeNode(2,1).next_to(node0, DOWN+RIGHT*0.5, buff=0.8)
        edge02 = Line(node0.get_bottom(), node2.get_top())
        #将node1 2 edge0102组合vg1
        vg3 = VGroup(node1,node2,edge01,edge02)
        self.play(DrawBorderThenFill(vg3),run_time=1)

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
        self.play(DrawBorderThenFill(vg4),run_time=1)

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
        self.play(DrawBorderThenFill(vg5),run_time=1)
        self.wait()

        highlight3 = Circle(radius = 0.5 ,color = YELLOW,fill_opacity=0.5,stroke_width = 0.4).move_to(node3.get_center())
        highlight9 = Circle(radius = 0.5 ,color = YELLOW,fill_opacity=0.5,stroke_width = 0.4).move_to(node9.get_center())
        highlight = Circle(radius = 0.5 ,color = YELLOW,fill_opacity=0.5,stroke_width = 0.4).move_to(node1.get_center())
        self.play(FadeIn(highlight3),FadeIn(highlight9))

        self.play(ApplyMethod(node3.depth_value.scale,2),ApplyMethod(node9.depth_value.scale,2),
                    rate_func=rate_functions.smooth, run_time=0.6)
        self.play(ApplyMethod(node3.depth_value.scale,0.5),ApplyMethod(node9.depth_value.scale,0.5),
                    rate_func=rate_functions.smooth, run_time=0.6)
        self.play(ApplyMethod(highlight9.move_to,node4.get_center()),rate_func=rate_functions.ease_in_out_quad,run_time=1.2)
        self.play(FadeIn(highlight))
        self.wait(1)
        self.play(ApplyMethod(highlight9.move_to,node1.get_center(),rate_func=rate_functions.ease_in_out_quad),
                  ApplyMethod(highlight3.move_to,node1.get_center(),rate_func=rate_functions.ease_in_out_quad),
                FadeOut(highlight3, rate_func=rate_functions.ease_in_out_quad),
                FadeOut(highlight9, rate_func=rate_functions.ease_in_out_quad),
                FadeOut(highlight),run_time=3)
        self.wait(1)
        
        highlight1 = Circle(radius = 0.5 ,color = YELLOW,fill_opacity=0.5,stroke_width = 0.4).move_to(node1.get_center())
        highlight10 = Circle(radius = 0.5 ,color = YELLOW,fill_opacity=0.5,stroke_width = 0.4).move_to(node10.get_center())
        self.play(FadeIn(highlight1),FadeIn(highlight10))
        self.play(ApplyMethod(node1.depth_value.scale,2),ApplyMethod(node10.depth_value.scale,2),rate_func=rate_functions.smooth, run_time=0.6)
        self.play(ApplyMethod(node1.depth_value.scale,0.5),ApplyMethod(node10.depth_value.scale,0.5),rate_func=rate_functions.smooth, run_time=0.6)
        self.play(ApplyMethod(highlight10.move_to,node4.get_center(),rate_func=rate_functions.ease_in_out_quad,run_time=1.2),
                  ApplyMethod(highlight10.move_to,node1.get_center(),rate_func=rate_functions.ease_in_out_quad,run_time=1.2),run_time=3)
        self.wait(1)
        self.play(FadeOut(vg3,vg4,vg5,node0,highlight1,highlight10))