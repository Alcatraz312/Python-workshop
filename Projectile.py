import matplotlib.pyplot as plt 
from matplotlib import animation
import numpy as np
import random 
import sys

try:
    velocity = float(input("Enter initial velocity (m/sec) : "))    #input initial velocity
    phi = float(input("Enter the angle of flight (degrees) : "))    #input the angle of flight

except ValueError:
    sys.exit("Invalid input")   
    
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

fig, ax = plt.subplots()     #initializing the figure and axes objects
line, = ax.plot(x,y, color=random.choice(colour_list))


projectile = plt.Circle((0,0), radius = 5)     #initializing the projectile object
ax.add_patch(projectile)

def update(n, x, y, line, projectile):        #defining a function to uprgade the position of porjectile at each instant of time
    line.set_data(x[:n],y[:n])           #updating the coordinates of the line object 
    projectile.center = (x[n],y[n])       #recentering the projectile at every instant of time
    line.axes.axis([0, max(np.append(x,y)), 0, max(np.append(x,y))])   #adjusting the axis of the line's axes to show the the entire trajectory

    return line, projectile

animation = animation.FuncAnimation(fig, update,frames= len(x), fargs=(x, y, line, projectile), interval = 20)   #intializing the animation object using the FuncAnimation class
#FuncAnimation takes the figure , the update function, len of the x array , a tuple containing x,y and line and projectile objects as values, and an interval argument that deals with the frames of the animation

plt.grid()  #grids 
plt.show()#show graph




