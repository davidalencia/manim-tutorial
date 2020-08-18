from manimlib.imports import *
import os
import pyclbr
import numpy as np
from manimlib.utils.rate_functions import linear

class Activacion(Scene):
  def construct(self):
    self.add(Circle(radius=4/np.pi))
    lastC = None
    animations = list()
    t_f =20
    for i in np.arange(10):
      n = i*2+1
      r = 4/(n*np.pi)
      x = lambda t: r*np.cos(n*t)
      y = lambda t: r*np.sin(n*t)

      c=ParametricFunction(lambda t : np.array([x(t),y(t), 0]),t_min=-TAU,t_max=TAU)
      
      if lastC!= None:
        animations.append(MoveAlongPath(c, lastC, run_time=t_f, rate_func=linear))
      animations.append(MoveAlongPath(Dot(radius=0.04), c, run_time=t_f, rate_func=linear))
      lastC = c
    self.play(*animations)

