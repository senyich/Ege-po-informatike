from turtle import *

k=10
for i in range(0,4):
    forward(8*k)
    right(90)
for i in range(0,4):
    left(30)
    forward(k*6)
    right(30)
    forward(8*k)
    right(150)
    forward(6*k)
    left(60)
done()