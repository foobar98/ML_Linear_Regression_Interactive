import numpy as np
import matplotlib.pyplot as plt

def linear_regression(x,y,p):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    # Line parameters
    m = sum((x-x_mean)*(y-y_mean))/sum((x-x_mean)**2)
    c = y_mean-m*x_mean

    y_val = [m*i + c for i in x]

    plt.subplot(2,2,p)
    plt.subplots_adjust(hspace=0.5)
    plt.axis([0,20,0,15])
    
    # Plotting data points
    plt.scatter(x,y,color='black')

    # Plotting hypothesis line
    plt.plot(x,y_val,'b')
    plt.title("Slope = %f \n Intercept = %f" %(m,c),fontsize=10)
    plt.draw()

# Anscombe's Quartet Datasets
x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])
y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])

linear_regression(x,y1,1)
linear_regression(x,y2,2)
linear_regression(x,y3,3)
linear_regression(x4,y4,4)

plt.show()