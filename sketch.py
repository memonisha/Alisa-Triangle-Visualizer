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
  strokeWeight(1)
  if distPlum == distLightblue == distTeal:
    text("equilateral",width-150,height-200)
  elif distPlum == distLightblue or distLightblue == distTeal or distPlum == distTeal:
    text("isosceles",width-150,height-200)
  else:
    text("scalene",width-150,height-200)


  
  noStroke()
  midPointXplum=(a.x+b.x)/2
  midPointYplum=(a.y+b.y)/2
  fill("black")
  rect(midPointXplum,midPointYplum,40,30)
  fill("plum")
  text(distPlum,midPointXplum,midPointYplum)
  midPointXlightblue=(b.x+c.x)/2
  midPointYlightblue=(b.y+c.y)/2
  fill("black")
  rect(midPointXlightblue,midPointYlightblue,40,30)
  fill("lightblue")
  text(distLightblue,midPointXlightblue,midPointYlightblue)
  midPointXteal=(c.x+a.x)/2
  midPointYteal=(c.y+a.y)/2
  fill("black")
  rect(midPointXteal,midPointYteal,40,30)
  fill("teal")
  text(distTeal,midPointXteal,midPointYteal)
  

def distances(a,b):
  d=round(sqrt((a.x-b.x)**2+(a.y-b.y)**2))
  #print(d)
  return d
  
  