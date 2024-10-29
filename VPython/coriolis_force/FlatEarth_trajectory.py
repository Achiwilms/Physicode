from vpython import *

# 地球視角 (否則為太空視角)
earth_view = True
# 小球速度
ball_v = 0.3
# 地球角速度（轉動速度）
omega = 0.1
# 時間間隔
dt = 0.01 

# 場景
# https://www.glowscript.org/docs/VPythonDocs/camera.html
scene = canvas(width=500, height=500, center=vec(0, 0, 0), autoscale=False, range=2)

# 地球(平的)(https://www.glowscript.org/docs/VPythonDocs/cylinder.html)
earth = cylinder(pos=vec(0, 0, 0), axis=vec(0, 0, 0.1), radius=1, texture=textures.earth)
# 輔助直線 (https://www.glowscript.org/docs/VPythonDocs/curve.html)
line = curve(pos=[vec(0, 1, 0.1), vec(0, -1, 0.1)], color=color.blue)

# 球 (https://www.glowscript.org/docs/VPythonDocs/sphere.html)
ball = sphere(
    pos = earth.pos + vec(0, 1, 0.1),
    v = vec(0, -ball_v, 0),
    radius = 0.05,
    color = color.yellow,
    make_trail=False,
)
# 軌跡 (https://www.glowscript.org/docs/VPythonDocs/curve.html)
trail = curve(pos=[ball.pos], color=color.red) 

# 總旋轉角度
total_angle = 0

# 迴圈(球離開地球一段距離時結束迴圈)
while mag(earth.pos-ball.pos) <= 1.5*earth.radius:
    # 更新頻率
    rate(1//dt) 
    # 更新地球、輔助直線的角度 
    earth.up = rotate(earth.up, angle=dt*omega, axis=earth.axis)
    line.up = rotate(line.up, angle=dt*omega, axis=earth.axis)
    # 更新鏡頭、軌跡的角度 (https://www.glowscript.org/docs/VPythonDocs/camera.html)
    if earth_view:
        scene.up = rotate(scene.up, angle=dt*omega, axis=earth.axis)
        trail.up = rotate(trail.up, angle=dt*omega, axis=earth.axis)
    # 更新軌跡
    trail.append(pos=rotate(ball.pos, angle=total_angle, axis=-earth.axis) if earth_view else ball.pos)    
    # 更新球的位置
    ball.pos = ball.pos + ball.v*dt
    # 更新總旋轉角度
    total_angle += omega*dt