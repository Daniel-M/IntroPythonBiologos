## Based on gas.py by Bruce Sherwood for a cube as a container
## Sligthly modified by Andrey Antonov for a torus.
from __future__ import division, print_function
from visual import *
from visual.graph import *
from random import random,uniform

def Reflection(p,pos):
    scale=mag(p)
    n=pos/mag(pos)

    return dot(identity(3)-2*n*n[:,newaxis],p)
# A model of an ideal gas with hard-sphere collisions
# Program uses numpy arrays for high speed computations
win=600
Natoms = 100 # change this to have more or fewer atoms
# Typical values
# container is a torus (vpython name is ring) with radius=RingRadius and thickness=RingThickness 
Matom = 4E-3/6E23 # helium mass
Ratom = 0.03 # wildly exaggerated size of helium atom
RingThickness=.3
RingRadius=1
new=[1,1,0]
k = 1.4E-23 # Boltzmann constant
T = 300. # around room temperature
dt = 1E-5
scene = display(title="Gas", width=win, height=win, x=0, y=0)
scene.background=color.yellow

ring(pos=(0,0,0),color=color.green,axis=(0,0,1),radius=RingRadius,opacity=.4,thickness=RingThickness)

dv = 10.

Atoms = []
colors = [color.red, color.green, color.blue,color.black,color.white,
          color.yellow, color.cyan, color.magenta,color.orange]
poslist = []
plist = []
mlist = []
rlist = []
r = Ratom
mass = Matom*r**3/Ratom**3
pavg = sqrt(2.*mass*1.5*k*T) # average kinetic energy p**2/(2mass) = (3/2)kT

for i in range(Natoms):
    alpha=2*pi*random()
    x = RingRadius*cos(alpha)*.9
    y = RingRadius*sin(alpha)*.9
    z = 0
##    print x,y,z
    Atoms = Atoms+[sphere(pos=(x,y,z), radius=r, color=colors[i % 9])]
    theta = pi*random()
    phi = 2*pi*random()
    px = pavg*sin(theta)*cos(phi)
    py = pavg*sin(theta)*sin(phi)
    pz = pavg*cos(theta)
    poslist.append((x,y,z))
    plist.append((px,py,pz))
    mlist.append(mass)
    rlist.append(r)

pos = array(poslist)


poscircle=pos
p = array(plist)
m = array(mlist)
m.shape = (Natoms,1) # Numeric Python: (1 by Natoms) vs. (Natoms by 1)
radius = array(rlist)
r = pos-pos[:,newaxis] # all pairs of atom-to-atom vectors

ds=(p/m)*(dt/2.)
if 'False' not in less_equal(mag(ds),radius):
    pos = pos+(p/mass)*(dt/2.) # initial half-step

while 1:
    rate(100)

    # Update all positions
    ds=(p/m)*(dt/2.)
    if 'False' not in less_equal(mag(ds),radius):
        pos = pos+(p/m)*dt

    r = pos-pos[:,newaxis] # all pairs of atom-to-atom vectors
    rmag = sqrt(sum(square(r),-1)) # atom-to-atom scalar distances
    hit = less_equal(rmag,radius+radius[:,None])-identity(Natoms)
    hitlist = sort(nonzero(hit.flat)[0]).tolist() # i,j encoded as i*Natoms+j
    # If any collisions took place:
    for ij in hitlist:
        i, j = divmod(ij,Natoms) # decode atom pair
        hitlist.remove(j*Natoms+i) # remove symmetric j,i pair from list
        ptot = p[i]+p[j]
        mi = m[i,0]
        mj = m[j,0]
        vi = p[i]/mi
        vj = p[j]/mj
        ri = Atoms[i].radius
        rj = Atoms[j].radius
        a = mag(vj-vi)**2
        if a == 0: continue # exactly same velocities
        b = 2*dot(pos[i]-pos[j],vj-vi)
        c = mag(pos[i]-pos[j])**2-(ri+rj)**2
        d = b**2-4.*a*c
        if d < 0: continue # something wrong; ignore this rare case
        deltat = (-b+sqrt(d))/(2.*a) # t-deltat is when they made contact
        pos[i] = pos[i]-(p[i]/mi)*deltat # back up to contact configuration
        pos[j] = pos[j]-(p[j]/mj)*deltat
        mtot = mi+mj
        pcmi = p[i]-ptot*mi/mtot # transform momenta to cm frame
        pcmj = p[j]-ptot*mj/mtot
        rrel = norm(pos[j]-pos[i])
        pcmi = pcmi-2*dot(pcmi,rrel)*rrel # bounce in cm frame
        pcmj = pcmj-2*dot(pcmj,rrel)*rrel
        p[i] = pcmi+ptot*mi/mtot # transform momenta back to lab frame
        p[j] = pcmj+ptot*mj/mtot
        pos[i] = pos[i]+(p[i]/mi)*deltat # move forward deltat in time
        pos[j] = pos[j]+(p[j]/mj)*deltat

##   Bounce off the boundary of the torus,
##   then update positions of display objects

    for j in range(Natoms):
        poscircle[j]=pos[j]/mag(pos[j])*RingRadius*new
    outside=greater_equal(mag(poscircle-pos),RingThickness-2*Ratom)

    for k in range(len(outside)):
        if outside[k]==1 and dot(p[k],pos[k]-poscircle[k])>0:
            p[k]=Reflection(p[k],pos[k]-poscircle[k])
            
    for i in range(Natoms):
        Atoms[i].pos = pos[i]
    outside=greater_equal(mag(pos),RingRadius+RingThickness)

