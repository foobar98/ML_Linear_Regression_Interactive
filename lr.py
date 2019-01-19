import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

x = np.array([])
y = np.array([])

def linear_regression():
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Line parameters
    m = sum((x-x_mean)*(y-y_mean))/sum((x-x_mean)**2)
    c = y_mean-m*x_mean

    y_val = [m*i + c for i in x]

    plt.clf()
    plt.axis([0,100,0,100])  

    # Plotting data points
    plt.scatter(x,y,color='black')

    # Plotting hypothesis line
    plt.plot(x,y_val,'b')
    plt.draw()

    # Plotting residual graph
    for i in range(len(x)):
        end_y = m*x[i]+c
        p1 = [x[i],x[i]]
        p2 = [y[i],end_y]
        plt.plot(p1,p2,'--',color='red')
        plt.draw()

def onclick(event):
    global ix,iy,x,y
    ix,iy = event.xdata,event.ydata
    print('x = %d, y = %d'%(ix, iy))

    # Add new mouse click coordinates
    x = np.append(x,ix)
    y = np.append(y,iy)

    linear_regression()

fig.canvas.mpl_connect('button_press_event', onclick)

plt.axis([0,100,0,100])  
plt.show()