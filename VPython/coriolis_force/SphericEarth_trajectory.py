from vpython import *

# 地球視角 (否則為太空視角)
earth_view = False
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
    make_trail=False,
)
# 軌跡 (https://www.glowscript.org/docs/VPythonDocs/curve.html)
trail = curve(pos=[ball.pos], color=color.red)

# 總旋轉角度
total_angle = 0

# 迴圈(球離開地球一段距離時結束迴圈)
while True:
    # 更新頻率
    rate(1//dt) 
    # 更新地球、鏡頭、輔助直線的角度 (https://www.glowscript.org/docs/VPythonDocs/camera.html)
    earth.rotate(angle=dt*omega, axis=earth.axis)
    circle.rotate(angle=dt*omega, axis=earth.axis)
    if earth_view:
        scene.forward = rotate(scene.forward, angle=dt*omega, axis=earth.axis)
        trail.axis = rotate(trail.axis, angle=dt*omega, axis=earth.axis)
    # 更新軌跡
    trail.append(pos=rotate(ball.pos, angle=total_angle, axis=-earth.axis) if earth_view else ball.pos)    
    
    # 更新球的位置
    ball.pos = rotate(ball.pos, angle=dt*ball_omega, axis=vec(1, 0, 0))    
    
    # 更新總旋轉角度
    total_angle += dt*omega   