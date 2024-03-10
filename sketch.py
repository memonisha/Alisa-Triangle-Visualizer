from p5 import *


def setup():
  createCanvas(windowWidth, windowHeight)
  global a, b, c 
  a = createMovableCircle(300, 100, 20)
  b = createMovableCircle(100, 100, 20)
  c = createMovableCircle(200, 300, 20)

def draw():
  background('black')
  drawTickAxes()
  fill('white')
  noStroke()
  a.draw()
  b.draw()
  c.draw()

  stroke("plum")
  strokeWeight(3)
  line(b.x,b.y,a.x,a.y)
  stroke("lightblue")
  line(b.x,b.y,c.x,c.y)
  stroke("teal")
  line(c.x,c.y,a.x,a.y)