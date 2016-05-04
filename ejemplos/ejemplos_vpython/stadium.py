from visual import *
# Pablo García Corzo <ozrocpablo@gmail.com>

scene=display()
scene.title='Chaotic Billiard'
scene.autoscale=0
scene.fullscreen=0
scene.forward=(0,-0.5,-1)

# Parameters
dt=0.02
maxposx=4.5
maxposz=5.5
# Adjusted for enought realistic physics
FR=0.5
FRBB=0.8
FRBW=0.9

# Billiard table
tapete=box(size=(10.75,0.5,13.75+2*maxposx),color=color.green)
mesa=box(color=color.orange,size=(10,4,20),pos=(0,-2.2,0),material=materials.wood)
l1=box(color=color.orange,size=(11,1,0.5),pos=(0,0.5,6.75+maxposx),material=materials.wood)
l2=box(color=color.orange,size=(11,1,0.5),pos=(0,0.5,-6.75-maxposx),material=materials.wood)
l3=box(color=color.orange,size=(0.5,1,13+2*maxposx),pos=(5.25,0.5,0),material=materials.wood)
l4=box(color=color.orange,size=(0.5,1,13+2*maxposx),pos=(-5.25,0.5,0),material=materials.wood)
estadio=curve(color=color.orange,radius=0.35,material=materials.wood)
for i in arange(180):
	theta=i*pi/180
	estadio.append([(maxposx+0.75)*cos(theta),0.5,maxposz+(maxposx+0.75)*sin(theta)])
for i in arange(180):
	theta=i*pi/180
	estadio.append([-(maxposx+0.75)*cos(theta),0.5,-maxposz-(maxposx+0.75)*sin(theta)])
estadio.append([(maxposx+0.75)*cos(0),0.5,maxposz+(maxposx+0.75)*sin(0)])
# This will be the player
flecha=arrow(color=color.blue,shaftwidth=0.1)

marcador=label(pos=(0,7,0),color=color.yellow,text='Welcome! Point and shoot.')

# These are the balls
bola=[]
bola.append(sphere(color=color.white,pos=(0,0.75,8),radius=0.5, material=materials.plastic))
#bola.append(sphere(color=color.red,radius=0.5,pos=(0,0.75,-4.)))
#for i in arange(2):
#    bola.append(sphere(color=color.red,radius=0.5,pos=(i-0.5,0.75,-5)))
#for i in arange(2):
bola.append(sphere(color=color.red,radius=0.5,pos=(-2,0.75,-5), material=materials.plastic))
bola.append(sphere(color=color.yellow,radius=0.5,pos=(2,0.75,-5), material=materials.plastic))
#for i in arange(4):
#    bola.append(sphere(color=color.red,radius=0.5,pos=(i-1.5,0.75,-7)))
for i in bola:
    i.vel=vector(0.,0.,0.)
    i.carambola=[]
#bola[5].color=(0.2,0.2,0.3)

def Mediavelocidades(bola):
    'Simple way for deciding when everything is stopped'
    vt=0
    for i in bola:
        vt+=mag2(i.vel)
    return vt

def Apunta(bola,flecha):
    'Shoot'
    flecha.visible=True
    flecha.pos=bola[0].pos
    while scene.mouse.clicked != False:
        scene.mouse.getclick()
    while scene.mouse.clicked == False:
        temp = scene.mouse.project(normal=(0,1,0), point=(0,1,0))
        if temp: # temp is None if no intersection with plane
            flecha.axis = temp - bola[0].pos
            if mag2(flecha.axis) >= 400:
                flecha.axis=20*norm(flecha.axis)
        rate(20)
    flecha.visible=False
    bola[0].vel=flecha.axis*2.
    bola[0].vel[1]*=0
    return bola
    
def Disparo(bola,dt,maxposx,maxposz,FR,FRBB,FRBW):
    'Physics are here'
    scene.background=color.white
    veltot=mag2(bola[0].vel)
    for i in bola:
        i.bandas=0
    while veltot > 0.001:
        rate(50)
        for i in bola:
            i.pos+=i.vel*dt
            i.vel-=norm(i.vel)*FR*dt
            if abs(i.pos[2]) >= maxposz:
             if (abs(i.pos[2])-maxposz)**2 >= maxposx**2-(i.pos[0])**2:
                if i.pos[2] > 0:
                        i.pos-=(i.vel+norm(i.vel)*FR*dt)*dt
                        uve=i.pos-vector(0,0.75,maxposz)
                        change=2*dot(i.vel,norm(uve))*uve/mag(uve)
                        i.vel[0]-=change[0]
                        i.vel[2]-=change[2]
                        i.vel*=FRBW
                        i.bandas+=1
                elif i.pos[2] < 0:
                        i.pos-=(i.vel+norm(i.vel)*FR*dt)*dt
                        uve=i.pos-vector(0,0.75,-maxposz)
                        change=2*dot(i.vel,norm(uve))*uve/mag(uve)
                        i.vel[0]-=change[0]
                        i.vel[2]-=change[2]
                        i.vel*=FRBW
                        i.bandas+=1
            elif abs(i.pos[0]) > maxposx :
                i.vel[0] *= -1
                i.vel*=FRBW
                i.pos[0]=i.pos[0]/(abs(i.pos[0]))*maxposx
                i.bandas+=1
        for i in range(len(bola)):
            for j in range(i+1,len(bola)):
                d=mag2(bola[i].pos-bola[j].pos)
                if d < (2*0.5)**2 :
                    bola[i].carambola.append(j)
                    bola[i].carambola.append(i)
                    direction=norm(bola[j].pos-bola[i].pos)
                    pi=dot(bola[i].vel,direction)
                    pj=dot(bola[j].vel,direction)
                    exchange=pj-pi
                    bola[i].vel=bola[i].vel + exchange*direction
                    bola[i].vel*=FRBB
                    bola[j].vel=bola[j].vel - exchange*direction
                    bola[i].vel*=FRBB
                    overlap=2*0.5-sqrt(d)
                    bola[i].pos=bola[i].pos - overlap*direction
                    bola[j].pos=bola[j].pos + overlap*direction
        veltot=Mediavelocidades(bola)
    scene.background=color.black
    for i in bola:
        i.vel*=0.
    return bola            
                
n=0
while True:
    bola=Apunta(bola,flecha)
    bola=Disparo(bola,dt,maxposx,maxposz,FR,FRBB,FRBW)
    n+=1
    caram=[]
    for i in bola:
        for j in i.carambola:
            caram.append(j)
        i.carambola=[]
    if (0 not in caram) or (1 not in caram) or (2 not in caram) :
        n=0
    marcador.text=str(n)
