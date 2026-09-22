import numpy as np
import random, math
import matplotlib.pyplot as plt

def savitsky_golay(data, window_size, degree):
    half = window_size//2
    x_window = np.arange(-half,half+1) #Creates a list of integers from -half to half

    A = np.array([x_window**i for i in range(degree + 1)]).T #Creates the polynomial matrix
    #Polynomial Matrix is Each Value in x_window * [1, x, x^2, x^degree]
    #Creates a degree+1 by window_size/2 matrix

    A_plus = np.linalg.pinv(A) #Assigns the pseduoinverse of the matrix as A+
    #When A+ is multiplied by a point in the sensor data it returns the polynomial coefficients produce the best fit curve
    #0th index is the constant value, 1 is x^1, etc

    weights = A_plus[0] #we only want the center point which is found at 0
    #gives us weights on how important each point in window is to the overall curve

    padded = np.pad(data, (half, half), mode='edge') #Creates "fake" points in the beginning and end where there are none

    filtered = []

    # Move the window across the data
    for i in range(len(data)):
        window = padded[i:i + window_size]

        # Apply the weights
        filtered.append(np.dot(weights, window))

    return filtered

num_points = 100
x = np.linspace(0, 10, num_points) #Creates 100 evenly spaced points from 1-10

true_signal = np.sin(x)+5 #Creates target signal

noise = np.random.normal(0, 0.25, num_points) #Creates noise for the data

sensor_data = true_signal + noise

filtered_data = savitsky_golay(sensor_data, 11, 2)

#Plots Data
plt.plot(x, sensor_data, label="Noisy Sensor Data")
plt.plot(x, true_signal, label="True Signal")
plt.plot(x, filtered_data, label="Savitzky-Golay Filter")

plt.xlabel("Time")
plt.ylabel("Sensor Reading")
plt.legend()
plt.show()