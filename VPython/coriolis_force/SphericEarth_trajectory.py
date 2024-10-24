from vpython import *

# 地球視角 (否則為太空視角)
earth_view = True
# 小球角速度（繞行速度）
ball_omega = 1
# 地球角速度（轉動速度）
omega = 0.1
# 時間間隔
dt = 0.01 

# 場景
# https://www.glowscript.org/docs/VPythonDocs/camera.html
scene = canvas(width=500, height=500, center=vec(0, 0, 0), 
               autoscale=False, 
               range=2)

# 地球(球型的)(https://www.glowscript.org/docs/VPythonDocs/sphere.html)
earth = sphere(pos=vec(0, 0, 0), axis=vec(0, 1, 0), radius=0.9, texture=textures.earth)
# 輔助環 (https://www.glowscript.org/docs/VPythonDocs/ring.html)
circle = ring(pos=vec(0, 0, 0), axis=vec(1, 0, 0), radius=0.9, thickness=0.01, color=color.blue)
# 球 (https://www.glowscript.org/docs/VPythonDocs/sphere.html)
ball = sphere(
    pos = earth.pos + vec(0, 1, 0),
    radius = 0.05,
    color = color.yellow,
    # make_trail=not(earth_view), 
    make_trail=False, 
    trail_radius=0.01,
)

# 迴圈(球離開地球一段距離時結束迴圈)
while True:
    # 更新頻率
    rate(1//dt) 
    # 更新地球、鏡頭、輔助直線的角度 (https://www.glowscript.org/docs/VPythonDocs/camera.html)
    earth.rotate(angle=dt*omega, axis=earth.axis)
    circle.rotate(angle=dt*omega, axis=earth.axis)
    if earth_view:
        scene.forward = rotate(scene.forward, angle=dt*omega, axis=earth.axis)
    # 更新球的位置
    ball.pos = rotate(ball.pos, angle=dt*ball_omega, axis=vec(1, 0, 0))
    