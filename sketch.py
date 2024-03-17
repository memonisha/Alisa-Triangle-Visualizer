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
  noStroke()
  textSize(25)
  fill('plum')
  a.draw()
  text(f"({a.x},{a.y})",width-150,height-50)
  fill('lightblue')
  b.draw()
  text(f"({b.x},{b.y})",width-150,height-100)
  fill('teal')
  c.draw()
  text(f"({c.x},{c.y})",width-150,height-150)

  #(200,300) plum
  #(500,400) lightblue
  #(200,300) teal

  stroke("plum")
  strokeWeight(4)
  line(b.x,b.y,a.x,a.y)
  stroke("lightblue")
  line(b.x,b.y,c.x,c.y)
  stroke("teal")
  line(c.x,c.y,a.x,a.y)

  distPlum=distances(a,b)
  distLightblue=distances(b,c)
  distTeal=distances(a,c)

def distances(a,b):
  d=round(sqrt((a.x-b.x)**2+(a.y-b.y)**2))
  print(d)
  return d
  