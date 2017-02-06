# -*- coding: utf8 -*-
import turtle             # 匯入turtle套件，允許我們使用turtle指令
window = turtle.Screen()  # 產生畫布以進行畫圖
window.bgcolor("black")
john = turtle.Turtle()    # 建立一個海龜turtle，它的名字叫john
john.pensize(5)

colors = ["red", "orange", "yellow", "green","blue"]
for pen_color in colors:
    john.color(pen_color)
    john.forward(200)
    john.left(144)
