import numpy as np
import random, math
import matplotlib.pyplot as plt
from scipy.datasets import electrocardiogram
from matplotlib.widgets import CheckButtons


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


# Load real ECG sensor data
ecg_data = electrocardiogram()

# ECG sensor data is collected at 360 measurements per second
sample_rate = 360

# Select data points from the ECG recording
sensor_data = ecg_data[2000:2300]

# Creates time values based on the sampling rate
x = np.arange(len(sensor_data)) / sample_rate


filtered_data = savitsky_golay(sensor_data, 21, 5)


#Plots Data
fig, ax = plt.subplots()

raw_plot, = ax.plot(x, sensor_data, label="Raw ECG Sensor Data")
filtered_plot, = ax.plot(x, filtered_data, label="Savitzky-Golay Filter")

plt.xlabel("Time (seconds)")
plt.ylabel("ECG Voltage (mV)")
plt.legend()


# Creates toggle buttons
check_ax = plt.axes([0.75, 0.75, 0.2, 0.12])

check = CheckButtons(
    check_ax,
    ["Raw ECG Sensor Data", "Savitzky-Golay Filter"],
    [True, True]
)


# Function that turns graphs on and off
def toggle_graph(label):

    if label == "Raw ECG Sensor Data":
        raw_plot.set_visible(not raw_plot.get_visible())

    elif label == "Savitzky-Golay Filter":
        filtered_plot.set_visible(not filtered_plot.get_visible())

    plt.draw()


# Connects buttons to toggle function
check.on_clicked(toggle_graph)


plt.show()
