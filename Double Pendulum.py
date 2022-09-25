from vpython import *
import time
from math import pi, sin,cos
import numpy as np
from numpy.linalg import solve
m1=30
m2=30
l1=3
l2=1.5
t1=60
t2=180
t1=t1*pi/180
t2=t2*pi/180
g=10
t11 =t1
t22=t2+0.01
E= -m1*g*l1*(cos(t1)) -m2*g*(l1*cos(t1)+l2*cos(t2))

t1d=0
t2d=0
t1dd=0
t2dd=0

t11d=0
t22d=0
t11dd=0
t22dd=0

thread1=cylinder(pos=vector(0,0,0),axis=vector(l1*sin(t1),-l1*cos(t1),0),radius=0.015*l1)
thread11=cylinder(pos=vector(0,0,0),axis=vector(l1*sin(t11),-l1*cos(t11),0),radius=0.015*l1)
thread2=cylinder(pos=thread1.axis,axis=vector(l2*sin(t2),-l2*cos(t2),0),radius=thread1.radius*m2/m1)
thread22=cylinder(pos=thread11.axis,axis=vector(l2*sin(t22),-l2*cos(t22),0),radius=thread11.radius*m2/m1)

bob1=sphere(pos=thread1.axis,radius=2*thread1.radius,color=vec(1,0,0))
bob2=sphere(pos=thread2.axis+thread2.pos,radius=2*thread1.radius,color=vec(1,0,0))
bob11=sphere(pos=thread11.axis,radius=2*thread11.radius,color=vec(0,1,0))
bob22=sphere(pos=thread22.axis+thread22.pos,radius=2*thread11.radius,color=vec(0,1,0))
attach_trail(bob2,color=vec(1,0,0))
attach_trail(bob22,color=vec(0,1,0))
i=0
sleep(2)

while i<1000:
    
    time.sleep(0.01)

    A=np.array([[(m1+m2)*(l1), m2*l2*cos(t2-t1)],[l1*cos(t2-t1),(l2)]])
    B=np.array([m2*l2*(t2d)*(t2d)*sin(t2-t1) -(m1+m2)*g*sin(t1), l1*(t1d)*(t1d)*sin(t1-t2) -g*sin(t2)])
    x=solve(A,B)
    t1dd=x[0]
    t2dd=x[1]

    t1d=t1d+t1dd*(0.01)
    t2d=t2d+t2dd*(0.01)
    t1=t1+t1d*(0.01)
    t2=t2+t2d*(0.01)

    thread1.axis=vector(l1*sin(t1),-l1*cos(t1),0)
    thread2.pos=thread1.axis
    thread2.axis=vector(l2*sin(t2),-l2*cos(t2),0)
    bob1.pos=thread1.axis
    bob2.pos=thread2.axis+thread2.pos

    A=np.array([[(m1+m2)*(l1), m2*l2*cos(t22-t11)],[l1*cos(t22-t11),(l2)]])
    B=np.array([m2*l2*(t22d)*(t22d)*sin(t22-t11) -(m1+m2)*g*sin(t11), l1*(t11d)*(t11d)*sin(t11-t22) -g*sin(t22)])
    x=solve(A,B)
    t11dd=x[0]
    t22dd=x[1]

    t11d=t11d+t11dd*(0.01)
    t22d=t22d+t22dd*(0.01)
    t11=t11+t11d*(0.01)
    t22=t22+t22d*(0.01)

    thread11.axis=vector(l1*sin(t11),-l1*cos(t11),0)
    thread22.pos=thread11.axis
    thread22.axis=vector(l2*sin(t22),-l2*cos(t22),0)
    bob11.pos=thread11.axis
    bob22.pos=thread22.axis+thread22.pos
    
    i=i+0.01



