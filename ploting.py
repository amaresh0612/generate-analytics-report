import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('mathtext', default='regular')


x=[1,2,3]
y=[1,4,9]
z=[8,5,2]

def bar_plots(x,y,z):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax2 = ax.twinx()
    ax.plot(x,y,label="1st")
    ax.plot(x, z, '-', label = '2nd graph')
    ax2.bar(x, z,edgecolor='black', linewidth=0.5, color='#64B560',label = '3rd graph')
    for index, value in enumerate(x):
        plt.text(value, index,str(value))
    #fig.legend(bbox_to_anchor=(1.3, 0.6))
    #ax.legend(loc=9)#,bbox_to_anchor = (1.05, 0.6))
    #ax2.legend(loc=1)#,bbox_to_anchor = (1.05, 0.6))
    fig.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
            ncol=2, mode="expand", borderaxespad=0.)
    #ax2.plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    ax.grid()
    ax.set_xlabel("x-axis")
    ax.set_ylabel(r"left-y-axis")
    ax2.set_ylabel(r"right-y-axis")
    ax.set_ylim(-50,50)
    ax2.set_ylim(0, 35)
    plt.title('Availability')
    filename="test.png"
    plt.savefig(filename)
    plt.close()