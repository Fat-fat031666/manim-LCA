# Manim 项目简介

这是一个使用 [Manim](https://github.com/ManimCommunity/manim) 制作的动画项目。Manim 是一个用于创建数学动画的强大工具，特别适合于教育内容的制作。

## 目录

- [安装](#安装)
- [使用说明](#使用说明)
- [项目结构](#项目结构)


## 安装

确保您已经安装了 Python 3.7 或更高版本。然后，通过 pip 安装 Manim：

```bash
pip install manim
```
对于更多安装选项和详细步骤，请参阅 Manim 官方文档。

## 使用说明
在项目根目录下运行以下命令来生成并预览动画：
```bash
manim -pql your_animation_script.py YourSceneName
```
-p 自动打开视频播放器预览结果。
-q 设置渲染质量（可选参数：l 低, m 中等, h 高, p 生产）。
your_animation_script.py 是包含场景的 Python 脚本文件名。
YourSceneName 是您想渲染的具体场景名称。

## 项目结构
my-project/
│
├── code/                    # 存放所有Python脚本，分别对应不同的scene
│   └── code.py
│   └── Demo.py
│   └── LCA.py
│   └── multiplication.py
├── media/                   # Manim自动生成的媒体文件夹
│
└── README.md                # 项目说明文件
