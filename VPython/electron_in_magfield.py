from vpython import *
# PARAMETERS
# charge of electron (C)
e_charge = -1.6e-19
# mass of electron (kg)
e_mass = 9.11e-31
# electron radius (m)
size = 0.2 

# magnetic field (T)
mag_field = 5e-12*vec(0, 0, 1) 
# electron speed (m/s)
e_v = 5*vec(1, 0, 1)

# end time (sec)
end_time = 10

# scene
scene = canvas(width=800, height=800, center=vec(0, 0, 0)) 
electron = sphere(pos=vec(0, 0, 0), radius=size, color=color.red, make_trail=True, trail_radius=0.05) 
mag_arrow = arrow(pos=vec(10, 0, 0), axis=3*norm(mag_field), color=color.orange)
mag_label = text(text = "B", pos = vec(12, 0, 0))

# initial speed
electron.v = e_v

# time loop
t = 0 # initial time
dt = 0.01 # time step
# while t <= end_time:
while True:
    rate(100)

    # update electron position
    electron.pos = electron.pos + electron.v*dt

    # find magnetic force
    magnetic_force = e_charge*cross(electron.v, mag_field)

    # acceleration caused by magnetic force
    magnetic_acc = magnetic_force/e_mass

    # update electron velocity
    electron.v = electron.v + magnetic_acc*dt

    # update time
    t = t + dt

