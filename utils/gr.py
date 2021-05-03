import matplotlib.pyplot as plt
import numpy as np
from random import choice
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Verdana']

def graphing(a=0,b=0,c=0,n=1,l=5):
    x=np.linspace(-l,l,1000)
    y = a*x**n+b*x+c
    fig, ax = plt.subplots()
    ax.plot(x, y, label=r"$ x^2 $")
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    plt.savefig('tmp\graph.png')

def graphing_random():
    x=np.linspace(-5,5,100)
    fig, ax = plt.subplots()
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.grid(True)
    ax.set_ylim(-5,5)
    ax.set_xlim(-5,5)
    ax.set_title(r"$ax^e+bx+c$")
    for i in range(-3,3):
        n = [-3,-2,2,3]
        a = choice(n)
        b= choice(n)
        c = choice(n)
        e = choice(n)
        y = a*x**e+b*x+c
        if b>0:
            b = "+"+str(b)
        if c>0:
            c = "+"+str(c)

        ax.plot(x,y, label=f"${a}x^{ {e} }{b}x{c}$")
    ax.legend()
    plt.savefig('tmp\graph.png')
    plt.close()
