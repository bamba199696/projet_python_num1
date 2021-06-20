# -*- coding: utf-8 -*-
import turtle
"""
Created on Sun Jun 20 13:22:27 2021

@author: Mohamed DIOUF
"""
def cercle(r):
    """
    objectif = tracer un cercle de rayon r
    methode = usage de da fonction native circle
    Besoins = r(rayon)
    connus = -
    Entrées = r(rayon)
    Sorties =
    Resultats = -
    Hypothèse = r>0
    
    """
    turtle.circle(r)
    
def demi_cercle(r):
    """
    objectif = tracer un demie cercle de rayon r
    methode = usage de da fonction native circle
    Besoins = r(rayon)
    connus = -
    Entrées = r(rayon)
    Sorties =
    Resultats = -
    Hypothèse = r>0
    
    """
    turtle.circle(r,180)

def carre(c,nb_cote):
    """
    objectif = tracer un carre du coté droit du curseur
    methode = usage d'une structure iterative
    Besoins = c(coté) nb_cote(parametre permettant de limiter le nombre de coté si besoin)
    connus = -
    Entrées = c nb_cote
    Sorties =
    Resultats = -
    Hypothèse = c>0 nb_cote>0
    
    """
    for i in range(nb_cote):
        turtle.forward(c)
        turtle.right(90)
        
def carre_g(c,nb_cote):
        """
        objectif = tracer un carre du coté gauche du curseur
        methode = usage d'une structure iterative
        Besoins = c(coté) nb_cote(parametre permettant de limiter le nombre de coté si besoin)
        connus = -
        Entrées = c nb_cote
        Sorties =
        Resultats = -
        Hypothèse = c>0 nb_cote>0
    
        """
        for i in range(nb_cote):
            turtle.forward(c)
            turtle.left(90)
            
def rectangle_g(L,l):
    """
        objectif = tracer un rectangle du coté gauche du curseur
        methode = usage d'une structure iterative
        Besoins = L(longueur) l(largeur) 
        connus = -
        Entrées = L(longueur) l(largeur) 
        Sorties =
        Resultats = -
        Hypothèse = L>0 l>0
    
        """
    for i in range(2):
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(L)
        turtle.left(90)
        
def rectangle_d(L,l):
    """
        objectif = tracer un rectangle du coté droite du curseur
        methode = usage d'une structure iterative
        Besoins = L(longueur) l(largeur) 
        connus = -
        Entrées = L(longueur) l(largeur) 
        Sorties =
        Resultats = -
        Hypothèse = L>0 l>0
    
        """
    for i in range(2):
        turtle.right(90)
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(L)
    
        
def triangle_equiliterale(cote):
    """
        objectif = tracer un triangle équilaterale
        methode = usage d'une structure iterative
        Besoins = cote (coté du triangle)
        connus = -
        Entrées = coté 
        Sorties =
        Resultats = -
        Hypothèse = coté>0
    
        """
    for i in range(3):
        turtle.left(120)
        turtle.forward(cote)

def polygone(nbr_cote,l_cote):
    """
        objectif = tracer un polygone parametrable
        methode = usage d'une structure iterative
        Besoins = nbr_cote l_cote
        connus = -
        Entrées = nbr_cote l_cote
        Sorties =
        Resultats = -
        Hypothèse = nbr_cote>0 l_cote>0
    
        """
    for i in range(nbr_cote):
        turtle.forward(l_cote)
        turtle.left(360/nbr_cote)

def trapèze():
    pass

def losange(long,ang):
    """
        objectif = tracer un losange en donnant l'angle et la longueur
        methode = usage d'une structure iterative
        Besoins = long(longueur des coté) ang(valeur des angles)
        connus = -
        Entrées = long ang
        Sorties =
        Resultats = -
        Hypothèse = long>0 ang>0 && ang<=360
    
        """
    for i in range(2):
        turtle.forward(long)
        turtle.right(ang)
        turtle.forward(long)
        turtle.right(180-ang)
    

def ellipse(r):
    """
        objectif = tracer un ellipse
        methode = usage d'une structure iterative et de la fonction native circle
        Besoins = r(rayon) fonction circle()
        connus = -
        Entrées = nbr_cote l_cote
        Sorties =
        Resultats = -
        Hypothèse = nbr_cote>0 l_cote>0
    
        """
    turtle.left(45)
    for i in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)
Turtle.exitonclick()        
        
