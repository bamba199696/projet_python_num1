# -*- coding: utf-8 -*-
import tkinter
import turtle
import dessinMSDA as dessin 
"""
Created on Thu Jun 17 22:39:12 2021

@author: Mohamed DIOUF
"""
def fusee():    
    turtle.setup()
    turtle.title("Mohamed DIOUF")
    turtle.pensize(3)
    
    #rectangle debout
    dessin.rectangle_g(45,15)
        
    turtle.up()
    turtle.forward(15)
    turtle.down()
    
    #premier triangle
    turtle.forward(25)
    turtle.left(120)
    turtle.forward(50)
    
    #retour et deuxième triange
    turtle.up()
    turtle.backward(50)
    turtle.down()
    turtle.left(60)
    turtle.up()
    turtle.forward(40)
    turtle.down()
    turtle.forward(25)
    turtle.right(120)
    turtle.forward(50)
    turtle.up()
    #retour au sommet gauche du triangle
    turtle.backward(50)
    turtle.right(60)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(45)
    turtle.down()
    #petit carré sur le rectangle
   
    dessin.carre(15,3)#
    
    #décalage et traçage du premier petit cercle    
    turtle.right(180)
    turtle.up()
    turtle.forward(15)
    turtle.down()
    
    dessin.cercle(5)#
    
    turtle.up()
    turtle.backward(30)
    turtle.left(180)
    turtle.down()
    #retour et traçage du second petit cercle                                   
    turtle.up()
    #turtle.forward(1)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(15)
    turtle.down()
    
    dessin.cercle(5)#
    
    #placement au sommet gauche du carré
    turtle.up()
    turtle.backward(15)
    turtle.right(90)
    turtle.forward(5)
    turtle.down()
    
    #positionnement et traçage du rectangle au dessus de petit carré
    turtle.up()
    turtle.left(90)
    turtle.forward(30)
    turtle.down()
    
    for i in range(2):
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(75)
        
    #dessin.rectangle_d(90,25)
    
    #carré au dessus du rectangle
    turtle.up()
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.down()
        
    dessin.carre(25,3)
    
    #deplacement et premier cercle    
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.up()
    turtle.forward(20)
    turtle.down()
    
    dessin.cercle(7)
    
    #deplacement et second cercle
    turtle.up()
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.down()
    
    dessin.cercle(7)
    
    #deplacement au sommet gauche du carré
    turtle.up()
    turtle.backward(20)
    turtle.right(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(30)
    turtle.down()
    #traçage du rectangle
    
        turtle.forward(85)"""
        
    dessin.rectangle_d(85,15)
    
    #deux peits carrés
    
    dessin.carre(15,3)
        
    turtle.left(90)
    turtle.up()
    turtle.forward(85)
    turtle.down()
    
    dessin.carre(15,3)
        
    turtle.up()
    turtle.right(180)
    turtle.left(15)
    turtle.down()
    turtle.forward(35)
    turtle.left(155)
    turtle.forward(40)
    turtle.backward(8)
    turtle.left(95)
    turtle.up()
    turtle.forward(115)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.down()
    turtle.left(15)
    turtle.forward(35)
    turtle.left(155)
    turtle.forward(40)
    turtle.left(15)
    turtle.forward(13)
    for i in range(2):
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(85)
        turtle.right(90)
        
    turtle.up()
    #turtle.backward(5)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(135)
    turtle.down()
    turtle.forward(21)
    turtle.right(45)
    turtle.up()
    turtle.forward(85)
    turtle.right(45)
    turtle.down()
    turtle.forward(23.5)
    turtle.up()
    turtle.backward(23.5)
    turtle.right(-45)
    turtle.backward(20)
    turtle.left(90)
    turtle.down()
    
    dessin.carre_g(45,3)
    
    turtle.up()
    turtle.backward(20)
    turtle.left(66)
    turtle.down()
    turtle.forward(50)
    turtle.left(-66)
    turtle.up()
    turtle.forward(45)
    turtle.down()
    turtle.right(66)
    turtle.forward(50)
    turtle.up()
    turtle.backward(50)
    turtle.right(-66)
    turtle.down()
    turtle.forward(15)
    
    dessin.triangle_equiliterale(75)
        
    turtle.up()
    turtle.backward(20)
    turtle.left(90)
    turtle.down()
    
    dessin.carre_g(35,3)
    #\turtle.showturtle()
    turtle.exitonclick()

fusee()