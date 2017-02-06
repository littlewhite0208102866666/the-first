import turtle

def draw_square(t, size):
        for i in range(360):
                t.forward(size)
                t.left(1)
                

window = turtle.Screen()
window.bgcolor("lightgreen")

john = turtle.Turtle()
for i in range(1):
    draw_circle(john.size)
    
