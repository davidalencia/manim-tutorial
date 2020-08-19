from manimlib.imports import *
import numpy as np

class Shapes(Scene):
  def construct(self):
    circulo = Circle() # Creación de circulo
    createCircle = ShowCreation(circulo) # Animación de creación
    self.play(createCircle) # Mostrar la animación
    fadeOutCircle = FadeOut(circulo) # Animación de desaparición 
    self.play(fadeOutCircle) # Mostrar la animación

    rect = Rectangle(color="blue", height=3, width=1) # Rectangulo con color
    # rect = Rectangle(color="#0000FF") # Rectangulo con color en hexadecimal
    self.play(ShowCreation(rect))
    self.play(FadeOut(rect))

    cuadrado = Square() # Cuadrado
    cuadrado.move_to(np.array([-4, 2, 0])) # Llevas al cuadrado a la posición designada
    #                         ( x, y, z)
    cuadrado2 = Square()
    cuadrado2.to_edge(UP) # LLeva una figura al borde
    # Hay cuatro direcciónes UP, LEFT, RIGHT, DOWN
    self.play(ShowCreation(cuadrado), ShowCreation(cuadrado2))
    self.play(FadeOut(cuadrado), FadeOut(cuadrado2))  
      
    linea = Line(np.array([2,0,0]),np.array([-2,1,0]))
    self.play(ShowCreation(linea))
    self.play(FadeOut(linea))




class AllShapes(Scene):
  def construct(self):
    self.anim(Arc(radius=0.5))
    self.anim(ArcBetweenPoints(np.array([2,0,0]),np.array([-2,0,0])))
    self.anim(CurvedArrow(np.array([2,0,0]),np.array([-2,0,0])))
    self.anim(CurvedDoubleArrow(np.array([2,0,0]),np.array([-2,0,0])))
    self.anim(Circle())
    self.anim(Dot())
    self.anim(SmallDot())
    self.anim(Ellipse())
    self.anim(AnnularSector())
    self.anim(Sector())
    self.anim(Annulus())
    self.anim(Line(np.array([2,0,0]),np.array([-2,0,0])))
    self.anim(DashedLine(np.array([2,0,0]),np.array([-2,0,0])))

    #Tangent line requires a mobject
    c = Circle()
    self.play(ShowCreation(c))
    self.anim(TangentLine(c, 0.2))
    self.play(FadeOut(c))

    self.anim(Elbow())
    self.anim(Arrow(np.array([2,0,0]),np.array([-2,0,0])))
    self.anim(Vector(np.array([1,0,0])))
    self.anim(DoubleArrow(np.array([2,0,0]),np.array([-2,0,0])))
    self.anim(Polygon(np.array([2,0,0]),np.array([-2,0,0]), np.array([1,1,0]),np.array([-2,-3,0])))
    self.anim(RegularPolygon(n=5))
    self.anim(Triangle())
    self.anim(ArrowTip())
    self.anim(Rectangle())
    self.anim(Square())
    self.anim(RoundedRectangle())


  def anim(self, mob):
    self.play(ShowCreation(mob))
    self.play(FadeOut(mob))

#Arc
#ArcBetweenPoints
#CurvedArrow
#CurvedDoubleArrow
#Circle
#Dot
#SmallDot
#Ellipse
#AnnularSector
#Sector
#Annulus
#Line
#DashedLine
#TangentLine
#Elbow
#Arrow
#Vector
#DoubleArrow
#Polygon
#RegularPolygon
#Triangle
#ArrowTip
#Rectangle
#Square
#RoundedRectangle

