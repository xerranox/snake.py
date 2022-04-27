#Librerias
from random import random
import turtle
import random
import time

#Variables
partes = []

#Puntos
puntos = 0
mejorpuntuacion = 0

#Ventana
ventana = turtle.Screen()
ventana.title("X SNAKE By: xerranox")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)

#Limite arriba
barrera = turtle.Turtle()
barrera.goto(-300, 240)
barrera.pensize(2)
barrera.pencolor("White")
barrera.speed(2)
barrera.goto(300, 240)
barrera.hideturtle()

#Limite abajo
barrera1 = turtle.Turtle()
barrera1.goto(300, -240)
barrera1.pensize(2)
barrera1.pencolor("White")
barrera1.speed(2)
barrera1.goto(-300, -240)
barrera1.hideturtle()

#Limite izquierda
barrera2 = turtle.Turtle()
barrera2.goto(280, 300)
barrera2.pensize(2)
barrera2.pencolor("White")
barrera2.speed(2)
barrera2.goto(280, -300)
barrera2.hideturtle()

#Limite abajo
barrera3 = turtle.Turtle()
barrera3.goto(-280, -300)
barrera3.pensize(2)
barrera3.pencolor("White")
barrera3.speed(2)
barrera3.goto(-280, 300)
barrera3.hideturtle()

#Crear elementos(Tortugas)
def crear_elemento(forma, color):
    elemento  = turtle.Turtle()
    elemento.speed(0)
    elemento.penup()
    elemento.shape(forma)
    elemento.color(color)
    elemento.goto(0, 0)
    return elemento

#Crear texto(puntos)
texto = crear_elemento(None, "white")
texto.hideturtle()
texto.goto(0, 260)
texto.write("Puntos:0 Mejor puntuacion:0", align="center", font=("Courier", 20, "normal"))


Copyright = crear_elemento(None, "White")
Copyright.hideturtle()
Copyright.goto(0, -280)
Copyright.write("    By: xerranox", align="left", font=("Courier", 20, "normal"))

#Elementos
cabeza = crear_elemento("square", "white")
cabeza.direccion = "quieta"
manzana = crear_elemento("circle", "white")
manzana.goto(0, 80)

#Funciones
def arriba():
    cabeza.direccion = "arriba"
def abajo():
    cabeza.direccion = "abajo"
def derecha():
    cabeza.direccion = "derecha"
def izquierda():
    cabeza.direccion = "izquierda"

#Teclado
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(derecha, "Right")
ventana.onkeypress(izquierda, "Left")

#Movimiento
def movimiento():
    if cabeza.direccion == 'arriba':
        y = cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direccion == 'abajo':
        y = cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direccion == 'derecha':
        x = cabeza.xcor()
        cabeza.setx(x+20)
    if cabeza.direccion == 'izquierda':
        x = cabeza.xcor()
        cabeza.setx(x-20)


#Perder
def gameover():
    time.sleep(1)
    cabeza.goto(0, 0)
    cabeza.direccion = "quieta"
    for i in partes:
        i.hideturtle()
    partes.clear()
    texto.clear()
    texto.write("Puntos:{} Mejor puntuacion:{}".format(puntos, mejorpuntuacion), align="center", font=("Courier", 20, "normal"))

#Juego
while True:
    #Ventana
    ventana.update()
    
    #Choque pared
    if cabeza.xcor() > 260 or cabeza.xcor() < -260 or cabeza.ycor() > 220 or cabeza.ycor() < -220:
        puntos = 0
        gameover()

    #Choque manzana
    if cabeza.distance(manzana) < 20:
        x = random.randint(-12, 12)
        y = random.randint(-10, 10)
        manzana.goto(x*20, y*20)
        nuevaparte = crear_elemento("square", "white")
        nuevaparte.direccion = "quieta"
        partes.append(nuevaparte)
        puntos += 1
        if puntos > mejorpuntuacion:
            mejorpuntuacion = puntos
        texto.clear()
        texto.write("Puntos:{} Mejor puntuacion:{}".format(puntos, mejorpuntuacion), align="center", font=("Courier", 20, "normal"))
    
    #Partes serpiente
    partestotales = len(partes)
    for i in range(partestotales-1, 0, -1):
        x = partes[i-1].xcor()
        y = partes[i-1].ycor()
        partes[i].goto(x, y)
    if partestotales > 0:
        x = cabeza.xcor()
        y= cabeza.ycor()
        partes[0].goto(x, y)

    #Movimiento
    movimiento()
   
   #Choque partes
    for i in partes:
        if i.distance(cabeza)<20:
            puntos = 0
            gameover()
    
    #Velocidad
    time.sleep(0.05)