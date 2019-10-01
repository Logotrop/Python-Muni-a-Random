import turtle
zelva = turtle.Turtle()
zelva.color('black')
zelva.pensize(5)
zelva.shape('turtle')

telo = 150
sirka = 130
uhelsipky = 90 # 60 pro rovnou šipku
velikostsipky = 200
pravyuhel = 90 #duh

n = (velikostsipky - sirka)/2 #konce sipky 
m = 180 - uhelsipky #vypocet uhlu

zelva.forward(telo)
zelva.right(pravyuhel)
zelva.forward(n)
zelva.left(m)
zelva.forward(velikostsipky)
zelva.left(m)
zelva.forward(velikostsipky)
zelva.right(uhelsipky)
zelva.backward(n)
zelva.left(pravyuhel)
zelva.forward(telo)
zelva.left(pravyuhel)
zelva.home()
#zelva.forward(sirka)
zelva.hideturtle()
input()
exit