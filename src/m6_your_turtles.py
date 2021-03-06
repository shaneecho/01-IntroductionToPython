"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Shixin Yan.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
flash = rg.SimpleTurtle('turtle')
flash.pen = rg.Pen('yellow', 3)
zoom = rg.SimpleTurtle('turtle')
zoom.pen = rg.Pen('black', 3)
flash.speed = 50
zoom.speed = 50
size = 70
for k in range(18):
    flash.draw_square(size)
    zoom.draw_circle(size)
    flash.pen_down()
    flash.right(20)
    flash.forward(30)
    zoom.pen_down()
    zoom.left(20)
    zoom.backward(30)

window.tracer(20)
damage = rg.SimpleTurtle('triangle')
damage.pen = rg.Pen('dark blue',1)
damage.backward(30)

for k in range(1000):
    damage.right(50)
    damage.forward(2*k)

window.close_on_mouse_click()
