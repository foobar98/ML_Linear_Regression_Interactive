import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

x = np.array([])
y = np.array([])
rate = 0.0005       # learning rate (alpha)
max_iter = 10000

def draw(theta):
    y_guess = np.array([theta[0]+theta[1]*i for i in x])

    plt.clf()
    plt.axis([-20,20,-20,20])  

    # Plotting data points
    plt.scatter(x,y,color='black')

    # Plotting hypothesis line
    plt.plot(x,y_guess,'b')

    # Uncomment below line for simulation
    # plt.pause(0.01)
    plt.draw()

def gradientDescent():
    x_trans = x.transpose()

    # Initialize theta
    theta = np.zeros(2)
    m = x.size

    for i in range(0,max_iter):
        hypothesis = np.array([theta[0]+theta[1]*i for i in x])
        error = hypothesis-y

        # Cost function
        J = np.sum(error**2)/(2*m)

        #print("Iteration %d | Cost: %f" %(i,J))

        # Calculate gradient
        del0 = np.sum(error)/m
        del1 = np.sum(x_trans*error)/m

        theta[0] = theta[0]-rate*del0
        theta[1] = theta[1]-rate*del1

        # Uncomment below line for simulation
        # draw(theta)
        
    draw(theta)

def onclick(event):
    global x,y
    ix,iy = event.xdata,event.ydata
    print('x = %d, y = %d'%(ix, iy))

    # Add new mouse click coordinates
    x = np.append(x,ix)
    y = np.append(y,iy)

    gradientDescent()

fig.canvas.mpl_connect('button_press_event', onclick)

plt.axis([-20,20,-20,20])  
plt.show()