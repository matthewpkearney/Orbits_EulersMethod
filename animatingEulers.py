from math import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

##note:
#to get the animation working, you will need to change the units to
# get each number to change faster (bigger difference)
 
#_T = 24*60*60 #8640[s] One Earth day
AU = 1.495978707*pow(10, 11) #[m] d(COM(Earth), COM(Sun))
univ_grav= float(6.67*pow(10,-11))  #[N*m^2/kg^2]
 
#variables m_sun and m_earth can represent any objects in the universe
m_sun=float(1.9891*pow(10,30))   #[kg]
m_earth=float(5.97219*pow(10,24))#[kg]
 
###Helper Functions for i step
def unit_vect( x ):
    '''Given array x (w/ 2 elements), return the value of x as a unit vector [rx, ry]'''
    return [x[0]/dist(x), x[1]/dist(x)]
 
def dist( x ):
    '''Return the distance c, using the Pythagorean Theorem
    pos is parameter containing pos[0] = x and pos[1] as y'''
    return sqrt(pow(x[0], 2) + pow(x[1], 2))
 
   
r=[AU, 0]     #x=1AU, y=0
v=[0, 29800]  #vx=0,   vy=29800 (launch vel)
 
def calc_accel(r):
    '''return the acceleration as a vector (list)
    acceleration is force / mass, uses force function to find angular acceleration'''
    ax= -(univ_grav*m_sun*r[0])/(pow(dist(r), 3))
    ay= -(univ_grav*m_sun*r[1])/(pow(dist(r), 3))
    return [ax, ay]
 
 
def next_pos(r, v,  t):
    '''calculate the next position using kinematics'''
    acc=calc_accel(r) 
    xf=r[0] + v[0]*t + 0.5*acc[0]*pow(t, 2) #acc in x
    yf=r[1] + v[1]*t + 0.5*acc[1]*pow(t, 2) #acc in y
    return [xf, yf]
 
def next_vel(r, v, t):
    '''calculates the next velocity using kinematic equations'''
    acc=calc_accel(r) 
    vxf = v[0] + acc[0]*t
    vyf = v[1] + acc[1]*t
    return [vxf, vyf]
 
 
# initialization function
def init():
    # creating an empty plot/frame
    line.set_data([], [])
    return line,
 
fig = plt.figure()
plt.style.use('dark_background')
pos_coordinates = open("351coordinates.txt", "w")
#ax = plt.axes(xlim=(-4*pow(10,11), 4*pow(10,11)), ylim =(-4*pow(10,11), 4*pow(10,11)))
#ax= plt.gca()
ax = plt.axes(xlim=(-2.28*pow(10,11), 2.28*pow(10,11)), ylim =(-2.28*pow(10,11), 2.28*pow(10,11)))
line, = ax.plot([], [], lw=1)
xdata = []
ydata = []


def time_steps(i):
    global r
    global v
    x=r[0]
    y=r[1]
    xdata.append(x)
    ydata.append(y)

    #for quick animation, use a higher number (250-600)
    r2=next_pos(r, v, i * 100) #calculate next pos
    v2=next_vel(r, v, i * 100) #calculate next vel
    r= r2 #changing to next pos
    v=v2  #changing to next velo
    # i = i + t #adding time step
    line.set_data(xdata, ydata)
    return line,
   
plt.title('Earths Orbit Around the Sun')
plt.xlabel('x-pos')
plt.ylabel('y-pos')
 
plt.axhline().set_color("indigo")
plt.axvline().set_color("indigo")
plt.scatter( 0 , 0 , s = 20 ).set_color("orange")
 
# call the animator  
anim = animation.FuncAnimation(fig, time_steps, init_func=init,
                            frames=1000, interval= 1, blit=True)
plt.show()
 
 


#removing spines
#ax.spines['left'].set_position('zero')
#ax.spines['bottom'].set_position('zero')
#
# ax =plt.axes(xlim=(-50,50), ylim =(-50,50))



