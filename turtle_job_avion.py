# -*- coding: utf-8 -*-
import tkinter
import turtle
"""
Created on Mon Jun 14 20:09:14 2021

@author: Mohamed DIOUF
"""
def avion():
    turtle.setup()
    turtle.title("Mohamed DIOUF")
    turtle.bgcolor("green")
    turtle.pensize(5)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.right(200) #◘inclinaison base queue
    turtle.forward(30) #longueur base queue
    turtle.right(95)   #premier diadeu
    turtle.forward(15) #longueur premier diadeu
    turtle.right(70)   #deuxieme diadeu
    turtle.forward(30) #longueur deuxième diadeu
    turtle.left(60)    #troisième diadeu
    turtle.forward(50) #talal ba edk
    turtle.left(120)   #dameu kogne
    turtle.forward(90) #talal beu UT
    turtle.right(105)  #diadeu laaf
    turtle.forward(20) #longueur diadeu laaf
    turtle.right(65)   #weugnèkou
    turtle.forward(100) #dem auchan
    turtle.left(50)    #diadeu auchan
    turtle.forward(100) #dem ville
    turtle.left(160)    #tourné rond point
    turtle.circle(18,-120) #weur ront point
    turtle.right(218)      #gnibissi
    turtle.forward(95)    #gnibissi auchan
    turtle.left(85)
    turtle.forward(100)
    turtle.right(65)
    turtle.forward(20)
    turtle.right(105)
    turtle.forward(100)
    turtle.left(80)   #dameu kogne
    turtle.forward(50) #talal ba edk
    turtle.left(90)    #troisième diadeu
    turtle.forward(30) #longueur deuxième diadeu
    turtle.right(70)   #deuxieme diadeu
    turtle.forward(20) #longueur deuxième diadeu
    turtle.right(93) #◘inclinaison base queu
    turtle.forward(90) #longueur base queue
    turtle.end_fill()   
    turtle.showturtle()
    turtle.exitonclick()
    
avion()

"""s=turtle.getscreen()

t=turtle.Turtle()
turtle.fillcolor("green")
turtle.begin_fill()
t.pensize(4)
for i in range(4):
    t.forward(100)
    t.left(90)
turtle.end_fill()

t.up()
t.goto(150,150)
t.down()
for i in range(3):
    t.forward(100)
    t.left(120)
    


t.up()
t.goto(-200,-200)
t.down()
for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    
t.up()
t.goto(-200,100)
t.down()
t.circle(90)
t.circle(50,120)    
turtle.done()"""
