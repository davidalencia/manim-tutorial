from manimlib.imports import *
import os
import pyclbr
import numpy as np
from manimlib.utils.rate_functions import linear
import json

t_f = 20

class DFT:
  def __init__(self, x, **kwargs):
    kwargs.setdefault('scale', 1)
    kwargs.setdefault('phase', 0)
    self.scale = kwargs['scale']
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
      freq = k
      amp = np.sqrt(re*re+im*im)
      phase = np.arctan2(re, im)+kwargs['phase']
      y[k] = (re, im, freq, amp, phase)
    
    y.pop(0)
    y.sort(reverse=True,key=lambda k: k[3])
    self.y = y
  
  def animations(self, shift=LEFT*5):
    lastC = None
    animations = list()
    for y in self.y:
      r = y[3]*self.scale
      freq = y[2]
      phase = y[4]
      x = lambda t: r*np.cos(t*freq+phase)
      y = lambda t: -r*np.sin(t*freq+phase)

      c=ParametricFunction(lambda t : np.array([x(t),y(t), 0]),t_min=-TAU,t_max=TAU, width=1, stroke_width=1)
      if lastC==None:
        c.shift([0,0,0]+shift)
        animations.append(ShowCreation(c, run_time=0.1))
      else:
        animations.append(MoveAlongPath(c, lastC, run_time=t_f, rate_func=linear))
      animations.append(MoveAlongPath(Dot(radius=0.04), c, run_time=t_f, rate_func=linear))
      lastC = c
    animations.append(MoveAlongPath(Dot(radius=0.1, color=RED), c, run_time=t_f, rate_func=linear))
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

  def real(self, t):
    x = np.float(0)
    for vec in self.y:
      r =np.float(vec[3])*self.scale
      freq =np.float(vec[2])
      phase =np.float(vec[4])
      x = x + r*np.cos(t*freq+phase)
    return x



class floatingLine(Animation):
    CONFIG = {
        "suspend_mobject_updating": False,
    }

    def __init__(self, mobject, path, edge=LEFT, **kwargs):
        self.path = path
        self.edge = edge
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        point = self.path.point_from_proportion(alpha)
        self.mobject.move_to(point, aligned_edge=self.edge)


class Fourier(Scene):
  CONFIG = {
    "x_min" : -TAU,
    "x_max" : TAU,
    "y_min" : -PI,
    "y_max" : PI,
    "graph_origin" : RIGHT*2+DOWN*2 ,  
  }


  def construct(self):
    x = []
    y = []
    i = 0
    with open('coors.json') as json_file:
      data = json.load(json_file)
      for coor in data:
        if i%100==0:
          x.append(int(coor['x']))
          y.append(int(coor['y']))
          i = i + 1


    scale = 0.5
    self.y_max = self.y_max*(1/scale)
    self.y_min = self.y_min*(1/scale)

    dY = DFT([i for i in np.arange(3)], scale=scale)
    dX = DFT([i for i in np.arange(3)], scale=scale, phase=-np.pi/2)

    animationsY = dY.animations()
    c = dY.lastC
    animationsY.append(floatingLine(Line([0,0,0], [2*TAU,0,0]), c, run_time=t_f, rate_func=linear))

    animationsX = dX.animations(UP*3)
    c = dX.lastC
    animationsX.append(floatingLine(Line([0,0,0], [0,2*TAU,0]), c, UP, run_time=t_f, rate_func=linear))

    #dibujo=ParametricFunction(lambda t : np.array([t,dY.imaginary(t), 0]),t_min=-TAU,t_max=TAU)
    dibujo=ParametricFunction(lambda t : np.array([dX.real(t),dY.imaginary(t), 0]),t_min=-TAU,t_max=TAU)

    self.play(*animationsY, 
              *animationsX, 
              ShowCreation(dibujo, run_time=t_f, rate_func=linear))




