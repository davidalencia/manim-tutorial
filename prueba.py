
class Clock:
  def __init__(self, scene, x, y, r, n=60):
    self.minute = 2*np.pi / n
    self.scene = scene
    self.x = x
    self.y = y
    self.r = r
    self.dot_angle = 0
    self.circle = Circle(radius = r)
    self.dot = Dot()

    self.circle.shift(x*RIGHT+y*UP)
    self.dot.shift((x+r)*RIGHT+y*UP)

    scene.add(self.circle)
    scene.add(self.dot)
  
  def tick(self):
    self.dot_angle = self.dot_angle + self.minute
    x = np.cos(self.dot_angle)*self.r
    y = np.sin(self.dot_angle)*self.r
    end_point = (x+self.x)*RIGHT+(y+self.y)*UP
    center = (self.x)*RIGHT+(self.y)*UP
    animation = ApplyMethod(self.dot.move_arc_center_to,center)
    return animation
    #checkout movet_to_arc_center



# move_to es absoluto y
# shift es relativo





      

class MoveAlongPathAnimation(Scene):
    def construct(self): 
      curve=ParametricFunction(
              lambda u : np.array([
                np.cos(u),
                np.sin(u),
                1
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
      dot = Dot()
      self.add(curve)
      self.play(MoveAlongPath(dot, curve, run_time=5, rate_func=linear))
      self.wait()



class RotateRect(Scene):
    def construct(self):
        line = Line([1,0,0],[-1,0,0])
        angle = math.radians(90)
        animation = Rotate(line, angle=angle)
        self.play(animation)

