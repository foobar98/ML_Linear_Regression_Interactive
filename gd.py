import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

x = np.array([])
y = np.array([])
m = 0
c = 0

def linear_regression_gd():    
    global m,c
    # Line parameters
    y_gen = np.array([m*i+c for i in x])
    #print((y-y_gen).shape)

    error = y-y_gen
    print(error)
    deltaM = sum(x*error)
    deltaC = sum(error)

    #print(deltaM,deltaC)

    m = m+deltaM
    c = c+deltaC

    #print(m,c)

    plt.clf()
    plt.axis([0,100,0,100])  

    # Plotting data points
    plt.scatter(x,y,color='black')

    # Plotting hypothesis line
    plt.plot(x,y_gen,'b')
    plt.draw()

def onclick(event):
    global ix,iy,x,y
    ix,iy = event.xdata,event.ydata
    #print('x = %d, y = %d'%(ix, iy))

    # Add new mouse click coordinates
    x = np.append(x,ix)
    y = np.append(y,iy)

    linear_regression_gd()

fig.canvas.mpl_connect('button_press_event', onclick)

plt.axis([0,100,0,100])  
plt.show()