from vpython import *
# parameters
g = 9.8 # (m/s^2)
size = 0.25 # ball radius (m)
height = 10 # ball center initial height (m)

# scene
scene = canvas(width=800, height=800, center=vec(0, height/2, 0)) # open a window
floor = box(length=30, height=0.01, width=10, color=color.blue) # the floor
ball = sphere(radius=size, color=color.red, make_trail = True, trail_radius = 0.05) # the ball

# initial conditions
# msg = text(text = 'Free Fall', pos = vec(-10, 10, 0)) # message
ball.pos = vec(0, height, 0) # ball center initial position
ball.v = vec(0, 0, 0) # ball initial velocity

# time loop
dt = 0.001 # time step
while ball.pos.y >= size: # until the ball hit the ground
    # run 10000 times per real second
    rate(1000) 

    # update ball position 
    ball.pos = ball.pos + ball.v*dt
    # update ball velocity
    ball.v.y = ball.v.y - g*dt
    # show

# speed msg
msg2 = text(text = "Final Speed: " + str(ball.v.y)+ " m/s", pos = vec(2, 10, 0))
msg2 = text(text = f"Final Speed: {ball.v.y:.2f} m/s", pos = vec(2, 10, 0))
