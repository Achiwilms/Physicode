from vpython import*
# Cannon: https://zh.wikipedia.org/zh-tw/%E5%8A%A0%E5%86%9C%E7%82%AE

class Cannon:
    def __init__(self, 
                 cannon_pos = vec (0, 0, 0), 
                 cannon_dir = vec(1, 1, 0), 
                 cannon_radius = 0.2, 
                 cannon_length = 1.5,
                 wheel_radius = 0.4, 
                 wheel_thickness = 0.1, 
                 car_width = 0.5,
                 cannonball_radius = 0.1,
                 cannonball_speed = 1000,
                 cannonball_mass = 1
                 ):
        # cannon
        cannon_axis = cannon_length*norm(cannon_dir)
        self.cannon = cylinder(
                            pos=cannon_pos, 
                            axis=cannon_axis, 
                            radius = cannon_radius, 
                            # color=color.red,
                            texture=textures.metal
                            )
        # left wheel
        l_wheel_dir = norm(cross(vec(0, 1, 0), cannon_axis))
        self.l_wheel = cylinder(
                        pos=cannon_pos+l_wheel_dir*car_width/2,
                        axis = l_wheel_dir*wheel_thickness,
                        radius=wheel_radius,
                        color=color.blue,
                        # texture=textures.rock
                        )
        # right wheel
        r_wheel_dir = norm(cross(cannon_axis, vec(0, 1, 0)))
        self.r_wheel = cylinder(
                                pos=cannon_pos+r_wheel_dir*car_width/2,
                                axis = r_wheel_dir*wheel_thickness,
                                radius=wheel_radius,
                                color=color.blue,
                                # texture=textures.rock
                                )        
        # cannonball
        self.cannonball = sphere(
            pos = cannon_pos,
            v = norm(cannon_dir)*cannonball_speed,
            radius = cannonball_radius,
            color = color.yellow,
            make_trail=True, 
            trail_radius=0.05,
        )
        
        print(self.cannonball.v.x)
        print(self.cannonball.v.y)
        print(self.cannonball.v.z)
        print(norm(cannon_dir))
        print(cannonball_speed)
    def cannonball_motion(self, dt):
        # update cannonball position
        self.cannonball.pos = self.cannonball.pos + self.cannonball.v*dt
        self.cannonball.v = self.cannonball.v + vec(0, -9.8, 0)*dt
        # print(self.cannonball.v.x)
        #########
        # TODO
        #########
        # update cannonball velocity
        # self.cannonball.v = ?        
        # Problem 1. 只考慮重力
        # (Hint: 重力 F = mg, g=9.8 m/s^2)
        # Problem 2. 考慮重力與空氣阻力
        # (Hint: 空氣阻力 F = -b*v, b=0.1 kg/s)

# scene
scene=canvas(width=800,height=600, center=vec(0, 0, 0))
planck = Cannon(
                cannon_pos=vec(0, 0, 0), 
                cannon_dir=vec(1, 1, 0), 
                cannonball_speed = 1000
                )
# einstein = Cannon(
#                 cannon_pos=vec(0, 0, 5), 
#                 cannon_dir=vec(0, 1, 1), 
#                 cannonball_speed = 5
#                 )    
# newton = Cannon(
#                 cannon_pos=vec(5, 0, 0), 
#                 cannon_dir=vec(-1, 1, 0), 
#                 cannonball_speed = 5
#                 )   

# Cannons=[]
# for i in range(10):
#     Cannon_i = Cannon(
#         cannon_pos=vec(2*i, 0, 0),
#         cannon_dir=vec(1, 1, 0),
#         cannonball_speed=i, 
#     )
#     Cannons.append(Cannon_i)

# animation
dt = 0.01 # time step
while True:
    rate(100) 
    planck.cannonball_motion(dt)
    # einstein.cannonball_motion(dt)
    # newton.cannonball_motion(dt)

    # for Cannon_i in Cannons:
    #     Cannon_i.cannonball_motion(dt)