import turtle
import time

turtle.Turtle()
screen=turtle.Screen()

screen.setup(width=1.0,height=1.0)


def main():
  turtle.penup()
  turtle.goto(0,50)
  turtle.pendown()
  turtle.hideturtle()
  turtle.write("Mid-Term Project \n\nThe Cancer \n\nGompo Thakuri",font=("New Times Roman",25),align=("center"))
  turtle.hideturtle()

  time.sleep(10)
  screen.clear()

main()

def pageOne():
  screen.bgcolor("black")
  screen.bgpic("cancer.gif")
  screen.update()
  time.sleep(3)

pageOne()
screen.clear()

def pageTwo():
  
    screen.bgcolor("black")
    turtle.color("silver")
    turtle.shape("turtle")
    turtle.pensize(3)

    turtle.penup()
    turtle.goto(200, -150)
    turtle.pendown()

    turtle.write("  Altarf 3.52")
    turtle.dot(10)
    turtle.lt(140)
    turtle.fd(250)



    turtle.write("   Asellus Australia 3.94")
    turtle.dot(10)
    turtle.lt(290)
    turtle.bk(150)


    turtle.write("   Acubens 4.25")
    turtle.dot(10)

    turtle.penup()
    turtle.fd(150)

    turtle.pendown()
    turtle.write("   Asellus Australis 4.94")
    turtle.dot(10)
    turtle.lt(20)
    turtle.fd(80)

    turtle.write("   Asellus Borealis 4.66")
    turtle.dot(10)
    turtle.lt(13)
    turtle.fd(150)
    turtle.write("   Iota Cancri")
    turtle.dot(10)
    turtle.hideturtle()
    time.sleep(5)

pageTwo()
screen.clear()


def pageThree():
  turtle.hideturtle()
  screen.bgpic("sky1.gif")
  screen.bgcolor("black")
  turtle.color("white")
  screen.update()
  time.sleep(2)
  turtle.penup()
  turtle.goto(-5,110)
  turtle.pendown()
  turtle.hideturtle()
  turtle.write("    Iota cancri")
  turtle.dot(10)

  turtle.penup()
  turtle.goto(5,30)
  turtle.pendown()
  turtle.write("   Asellus Australis 4.66")
  turtle.dot(10)

  turtle.penup()
  turtle.goto(0,0)
  turtle.pendown()
  turtle.write("   Asellus Borealis 4.94")
  turtle.dot(10)

  turtle.penup()
  turtle.goto(-50,-100)
  turtle.pendown()
  turtle.write("   Acubens 4.25")
  turtle.dot(10)

  turtle.penup()
  turtle.goto(0,0)
  turtle.pendown()


  turtle.penup()
  turtle.goto(100,-120)
  turtle.pendown()
  turtle.write("  Altarf 3.52")
  turtle.dot(10)
  turtle.hideturtle()

  time.sleep(10)

  turtle.penup()
  turtle.goto(-5,110)
  turtle.pendown()
  turtle.goto(5,30)
  turtle.goto(0,0)
  turtle.goto(-50,-100)

  turtle.penup()
  turtle.goto(0,0)
  turtle.pendown()
  turtle.goto(100,-120)
  turtle.hideturtle()
  time.sleep(5)
pageThree()
screen.clear()

def pageFour():
  turtle.penup()
  turtle.goto(0,50)
  turtle.pendown()
  turtle.hideturtle()
  turtle.write("Thank You...",font=("New Times Roman",35),align=("center"))
  turtle.hideturtle()

  time.sleep(15)
  
pageFour()
turtle.done()



  





