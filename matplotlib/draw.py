#coding:utf8
import matplotlib.pyplot as plt
import numpy as np

def draw_sincos():
    x=np.linspace(0,2*np.pi,100)
    plt.plot(x,np.sin(x),'r-0',x,np.sinc(2*x),'g--')
    
    plt.show()
def draw_submap():
    x=np.linspace(0,5*np.pi,100)
    plt.subplot(2,1,1)
    plt.plot(x,np.sinc(x),'r')
    plt.subplot(2,1,2)
    plt.plot(x,np.cos(x),'g')
    plt.show()
def draw_sandian():
    x=np.linspace(0,5*np.pi,100)
    y=np.sin(x)
    plt.scatter(x,y)
    plt.show()
def draw_rectang():
    x=np.random.randn(1000)
    plt.hist(x,50)
    plt.show()
def draw_xy():
    x=np.linspace(0,5*np.pi,100)
    plt.plot(x,np.sinc(x),'r-x',label='sun_appearance_height_index')
    plt.plot(x,np.cos(x),'g-^',label='baby_sexy_mouth')
    plt.legend()
    plt.xlabel('sha baby')
    plt.ylabel("sha fenbi")
    plt.title('dong')
    plt.show()
if __name__=="__main__" :  
    draw_xy()
    draw_sandian()
    draw_rectang()
    draw_submap()
    draw_sincos()