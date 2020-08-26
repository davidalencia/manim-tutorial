from manimlib.imports import *
import numpy as np

class Texto(Scene):
  def construct(self):
    hola = TextMobject("Hola")
    self.play(Write(hola))
    self.play(FadeOut(hola))

    linea1 = TextMobject("Esta linea va arriba")
    linea2 = TextMobject("Esta linea va abajo")
    linea2.next_to(linea1,DOWN)
    self.play(Write(linea1), Write(linea2))
    self.play(FadeOut(linea1), FadeOut(linea2))

    eq = TexMobject("e^{i\pi} + 1 = 0")
    self.play(Write(eq))
    self.play(FadeOut(eq))

    lugar = TextMobject("Estoy en otro lugar")
    # lugar.move_to(np.array([-4,2,0]))
    lugar.shift(2*UP)
    lugar.shift(4*LEFT)
    lugar.rotate(PI/4)
    self.play(Write(lugar))
    self.play(FadeOut(lugar))


    rojo = TextMobject("De color rojo", color=RED)
    colores = TextMobject("Muchos ", "distintos e interesantes ", "colores")
    colores.next_to(rojo, DOWN)
    # Manera 1
    # colores.set_color_by_tex("distintos", BLUE)
    # colores.set_color_by_tex("colores", GREEN)
    # Manera 2
    colores.set_color_by_tex_to_color_map({
      "distintos": BLUE,
      "colores": GREEN
    })
    self.play(Write(rojo), Write(colores))
    self.play(FadeOut(rojo), FadeOut(colores))


    pichu = TextMobject("Pichu")
    picachu = TextMobject("Picachu")
    raichu = TextMobject("Raichu")
    self.play(Write(pichu))
    self.play(Transform(pichu, picachu))
    self.play(Transform(pichu, raichu))