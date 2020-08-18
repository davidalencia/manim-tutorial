from manimlib.imports import *
import os
import pyclbr
import numpy as np
from manimlib.utils.rate_functions import linear

class DFT:
  def __init__(self, x, scale=1):
    self.scale = scale
    N = len(x)
    y = [None] * N

    for k in np.arange(N):
      re = 0
      im = 0
      for n in np.arange(N):
        phi = (2*np.pi*k*n)/N
        re = re + x[n]*np.cos(phi)
        im = im - x[n]*np.sin(phi)

      re = re/N
      im = im/N
      freq = PI*2*k/N
      amp = np.sqrt(re*re+im*im)
      phase = np.arctan2(re, im)
      y[k] = (re, im, freq, amp, phase)
    
    y.pop(0)
    y.sort(reverse=True,key=lambda k: k[3])
    self.y = y
  
  def animations(self):
    lastC = None
    animations = list()
    t_f =20
    for y in self.y:
      r = y[3]*self.scale
      freq = y[2]
      phase = y[4]
      x = lambda t: r*np.cos(t*freq+phase)
      y = lambda t: -r*np.sin(t*freq+phase)

      c=ParametricFunction(lambda t : np.array([x(t),y(t), 0]),t_min=-TAU,t_max=TAU, width=1, stroke_width=1, color=BLUE)
      if lastC==None:
        c.shift(LEFT*5)
        animations.append(ShowCreation(c, run_time=0.1))
      else:
        animations.append(MoveAlongPath(c, lastC, run_time=t_f, rate_func=linear))
      animations.append(MoveAlongPath(Dot(radius=0.04), c, run_time=t_f, rate_func=linear))
      lastC = c
    animations.append(MoveAlongPath(Dot(radius=0.1, color=RED), lastC, run_time=t_f, rate_func=linear))
    self.lastC = lastC
    return animations

  def imaginary(self, t):
    y = np.float(0)
    for vec in self.y:
      r =np.float(vec[3])*self.scale
      freq =np.float(vec[2])
      phase =np.float(vec[4])
      y = y + r*np.sin(t*freq+phase)
    return -y



class floatingLine(Animation):
    CONFIG = {
        "suspend_mobject_updating": False,
    }

    def __init__(self, x, path, **kwargs):
        self.path = path
        self.dim = x
        self.x = x
        mobject  = Line([0,0,0], [x,0,0])
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        point = self.path.point_from_proportion(alpha)
        new_dim = self.x-point
        new_scale = new_dim/self.dim 
        self.dim = self.dim*new_scale
        self.mobject.scale(new_scale)
        self.mobject.move_to(point, aligned_edge=LEFT)


class Fourier(GraphScene):
  CONFIG = {
    "x_min" : -TAU,
    "x_max" : TAU,
    "y_min" : -PI,
    "y_max" : PI,
    "graph_origin" : RIGHT*2 ,  
  }


  def construct(self):
    self.setup_axes(animate=True)

    scale = 0.2
    self.y_max = self.y_max*(1/scale)
    self.y_min = self.y_min*(1/scale)

    d = DFT([i for i in np.arange(40)], scale)
    animations = d.animations()
    c = d.lastC
    animations.append(floatingLine(8, c, run_time=20, rate_func=linear))
    
    func_graph=self.get_graph(d.imaginary)
    animations.append(ShowCreation(func_graph, run_time=20, rate_func=linear))

    self.play(*animations)




