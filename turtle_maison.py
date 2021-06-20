import turtle

'''
Ce programme permet de dessiner une maison
'''
def carre():
    '''ce module nous permet de contructruire la base de la maison'''
    
    turtle.title("la maison de khadim mbacke ndiaye")
    turtle.pensize(3)
    turtle.bgcolor("light grey")
    
    for i in range (6):
        turtle.forward(200)
        turtle.right(90)
    x=0 
    while(x<2):
        turtle.forward(150)
        turtle.right(90)
        x=x+1
    for i in range(2):
        turtle.fd(60)
        turtle.right(90)
        turtle.fd(90)
    for i in range(1):
         turtle.forward(20)
    for i in range(1):
        turtle.right(90)
        turtle.fd(200)
        turtle.right(90)
def triangle():
    '''le triangle permet de dessiner la toiture de la maison'''
    turtle.pensize(3)
    x=0
    for i in range(1):
        
        turtle.forward(250)
        turtle.left(120)
        turtle.forward(100)
    while(x<4):
        turtle.fd(30)
        turtle.right(90)
        x=x+1
    for i in range(2):
        
        turtle.forward(200)
        turtle.left(120)
        turtle.forward(100)
    for i in range(1):
        turtle.forward(95)
        turtle.right(90)
       
def fenetre():
    '''Fonction permettant de construire la fenetre de la maison'''
    x=0
    while(x<3):
        turtle.fd(20)
        turtle.right(90)
        x=x+1
    for i in range(1):
         turtle.fd(40)
         turtle.right(90)
         turtle.fd(40)
         turtle.right(90)
         turtle.fd(40)
         turtle.right(90)
         turtle.fd(20)
         turtle.right(90)
         turtle.fd(40)
         turtle.bk(20)
         turtle.right(90)
         turtle.fd(20)
         
         
         
def deplacer_sans_tracer(x, y = None):
    ''''Fonction pour se déplacer à un point sans tracer'''
    turtle.up()
    turtle.right(90)
    if (isinstance(x, tuple) or isinstance(x, list)) and len(x) ==2: 
        turtle.goto(x)
    else:
        turtle.goto(x, y)
        turtle.down()

def finition1():
    turtle.left(90)
    turtle.pensize(15)
    turtle.bk(26)
    turtle.fd(85)
def finition2():
    turtle.right(90)
    turtle.pensize(12)
    turtle.fd(50)
    
   
        

carre()
triangle()
deplacer_sans_tracer(170, -45)
fenetre()
deplacer_sans_tracer(170, -198)
finition1()
deplacer_sans_tracer(0,-200)
finition2()
turtle.exitonclick()
         
carre()
turtle.exitonclick()