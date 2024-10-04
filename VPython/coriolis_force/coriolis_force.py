from vpython import *

scene = canvas(width=800, height=800, center=vec(0, 0, 0))
earth = sphere(pos=vec(0, 1, 0), radius=5, texture=textures.earth)
distant_light(direction=vec(0, -1, 0), color=color.orange)
# earth = box(pos=vec(0, 0, 0), texture=textures.flower)

# 如何讓物體轉動？
# https://www.glowscript.org/docs/VPythonDocs/rotation.html