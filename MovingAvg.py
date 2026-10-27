
import random
import matplotlib.pyplot as plt

# 1. Generate simulated sensor readings
num_readings = 100
true_value = 50

actual_readings = [true_value] * num_readings

# 2. Add random noise to simulate an imperfect sensor
noisy_readings = [
    value + random.uniform(-10, 10)
    for value in actual_readings
]

# 3. Apply a moving-average filter
window_size = 5
filtered_readings = []

for i in range(num_readings):
    start = max(0, i - window_size + 1)
    window = noisy_readings[start:i + 1]
    average = sum(window) / len(window)
    filtered_readings.append(average)

# 4. Display the results
print("First 10 noisy readings:")
print([round(x, 2) for x in noisy_readings[:10]])

print("\nFirst 10 filtered readings:")
print([round(x, 2) for x in filtered_readings[:10]])

# 5. Plot the readings
plt.figure(figsize=(10, 5))

plt.plot(actual_readings, label="True Value")
plt.plot(noisy_readings, label="Noisy Sensor Readings", alpha=0.5)
plt.plot(filtered_readings, label="Moving Average Filter")

plt.xlabel("Reading Number")
plt.ylabel("Sensor Value")
plt.title("Cleaning Up a Noisy Sensor")
plt.legend()
plt.grid(True)
<<<<<<< Updated upstream
plt.show()
=======
plt.show()
>>>>>>> Stashed changes
