import matplotlib.pyplot as plt 
from matplotlib import animation
import numpy as np
import random 

try:
    velocity = float(input("Enter initial velocity (m/sec) : "))    #input initial velocity
    phi = float(input("Enter the angle of flight (degrees) : "))    #input the angle of flight

except ValueError:
    print("Invalid input, please enter an integer or decimal value.")

else:
    phi = np.deg2rad(phi)   #coverting the unit of the angle from degree to radians 

colour_list = ["red","green","blue","yellow","purple","magenta"]    #create list of different colours

g = 9.8   #acceleration due to gravity (m/sec^2)
time_of_flight = (2 * velocity * np.sin(phi))/g       #total time of flight of a projectile 
t = np.linspace(0,time_of_flight,num=150)      #created an array of 150 values of different point of times 
horizontal_velocity = velocity * np.cos(phi)
vertical_velocity = velocity * np.sin(phi)

x = horizontal_velocity * t     #horizontal position of the projectile at an instant  (x-coordinate array)
y = vertical_velocity  * t - 0.5*g*t**2    #vertical position of the projectile at an instant   (y-coordinate array)

fig, ax = plt.subplots()     #initializing the fig and 
line, = ax.plot(x,y, color=random.choice(colour_list))

height_max = max(y)     #max height attained by the projectile
range_ = max(x)         #range of the projectile

projectile = plt.Circle((0,0), radius = 5)     #initializing the projectile object
ax.add_patch(projectile)

def update(n, x, y, line, projectile):        #defining a function to uprgade the position of porjectile at each instant of time
    line.set_data(x[:n],y[:n])           #updating the coordinates of the line object 
    projectile.center = (x[n],y[n])       #recentering the projectile everytime at every instant of time
    line.axes.axis([0, max(np.append(x,y)), 0, max(np.append(x,y))])   #adjusting the axis of the line's axes to show the the entire trajectory

    return line, projectile

animation = animation.FuncAnimation(fig, update, len(x), fargs=(x, y, line, projectile), interval = 20)   #intializing the animation object using the FuncAnimation class
#FuncAnimation takes the figure , the update function, len of the x array , a tuple containing x,y and line and projectile objects as values, and an interval argument that deals with the frames of the animation

plt.grid()  #grids 
plt.show()  #show graph












# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import random
# g = 9.8

# colours = ["red","green","blue","yellow","purple","magenta"]

# try:
#     u = float(input('Enter initial velocity (m/s): '))
#     theta = float(input('Enter angle (deg): '))
# except ValueError:
#     print('Invalid input.')
# else:
#     theta = np.deg2rad(theta)

# t_flight = 2*u*np.sin(theta)/g
# t = np.linspace(0, t_flight, 100)
# x = u*np.cos(theta)*t
# y = u*np.sin(theta)*t - 0.5*g*t**2

# fig, ax = plt.subplots()
# line, = ax.plot(x, y, color=random.choice(colours))

# xmin = x[0]
# ymin = y[0]
# xmax = max(x)
# ymax = max(y)
# ball = plt.Circle((xmin, ymin), radius=5)
# ax.add_patch(ball)

# def update(n, x, y, line, circle):
#     line.set_data(x[:n], y[:n])
#     ball.center = x[n],y[n]
#     line.axes.axis([0, max(np.append(x,y)), 0, max(np.append(x,y))])

#     return line,circle

# ani = animation.FuncAnimation(fig, update, len(x), fargs=(x, y, line, ball),
#                               interval= 20)

# plt.grid()
# plt.show()