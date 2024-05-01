from vpython import *
# parameters
k = 10 # (N/m)
spring_length = 3 # spring length (m)
ball_mass = 0.25 # ball mass (kg)
ball_size = 0.25 # ball radius (m)
ball_initial_posx = 4 # ball initial x position (m)
ball_initial_vx = 0 # ball initial x velocity (m/s)
end_time = 10 # end time (s)
drag_constant = 0.1 # drag constant

# scene
scene = canvas(width=800, height=800, center=vec(spring_length, 0, 0)) # window
wall = box(pos = vec(0, 0, 0), length=0.2, height=5, width=5, color=color.blue) # the floor
ball = sphere(radius=ball_size, color=color.red, make_trail = False, trail_radius = 0.05) # the ball
spring = helix(pos=vec(0, 0, 0), radius=ball_size/2, coils=30) # the spring

# graph
graph1=graph(title='Position vs Time', xtitle='Time (s)', ytitle='Position (m)', width=800, height=400)
func_pos=gdots(graph=graph1, color=color.orange,size=3)

# initial conditions
ball.pos = vec(ball_initial_posx, 0, 0)
ball.v = vec(ball_initial_vx, 0, 0)
spring.axis = ball.pos
t = 0

# time loop
dt = 0.001 # time step
while t < end_time: 
    # run 1000 times per real second
    rate(1000) 

    # update ball position 
    ball.pos = ball.pos + ball.v*dt

    # update spring position
    spring.axis = ball.pos
    
    # force by spring
    spring_force = -k*(ball.pos.x - spring_length)

    # acceleration by spring
    spring_acc = spring_force/ball_mass

    # force by drag
    drag_force = -drag_constant*ball.v.x

    # acceleration by air drag
    drag_acc = drag_force/ball_mass

    # update ball velocity
    ball.v.x = ball.v.x + (spring_acc + drag_acc)*dt

    # update time
    t = t + dt

    # update graph
    func_pos.plot(pos=(t, ball.pos.x))