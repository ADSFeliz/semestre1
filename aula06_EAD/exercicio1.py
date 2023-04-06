import turtle

def montar_cabeca(smile):
    smile.penup()
    smile.setpos(0,0)
    smile.fillcolor("yellow")
    smile.begin_fill()
    smile.circle(100)
    smile.end_fill()
    montar_olhos(smile)
    montar_boca(smile)
    
def montar_olhos(smile):
    smile.setpos(35,125)
    smile.fillcolor("black")
    smile.begin_fill()
    smile.circle(10)
    smile.setpos(-35,125)
    smile.circle(10)
    smile.end_fill()

def montar_boca(smile):
    smile.setpos(-50,80)
    smile.setheading(270)
    smile.fillcolor("black")
    smile.begin_fill()
    smile.circle(50, 180)
    smile.end_fill()
    
    smile.setpos(-40,80)
    smile.setheading(270)
    smile.fillcolor("yellow")
    smile.begin_fill()
    smile.circle(40)
    smile.end_fill()

window = turtle.Screen()
smile = turtle.Turtle()

montar_cabeca(smile)
smile.hideturtle()

window.exitonclick()
