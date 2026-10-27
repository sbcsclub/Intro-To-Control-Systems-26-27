
import numpy as np
import random, math
import matplotlib.pyplot as plt

def moving_average(data, window_size):
    filtered = []

    # Move the window across the data
    for i in range(len(data)):
        start = max(0, i - window_size + 1)
        window = data[start:i + 1]

        # Calculate the average of the values in the window
        average = sum(window) / len(window)
        filtered.append(average)

    return filtered

num_points = 100
x = np.linspace(0, 10, num_points) # Creates 100 evenly spaced points from 0-10

true_signal = np.sin(x) + 5 # Creates target signal

noise = np.random.normal(0, 0.25, num_points) # Creates random noise

sensor_data = true_signal + noise # Simulates noisy sensor readings

filtered_data = moving_average(sensor_data, 11)

# Plots Data
plt.plot(x, sensor_data, label="Noisy Sensor Data")
plt.plot(x, true_signal, label="True Signal")
plt.plot(x, filtered_data, label="Moving Average Filter")

plt.xlabel("Time")
plt.ylabel("Sensor Reading")
plt.legend()
plt.show()