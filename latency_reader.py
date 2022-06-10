#!/usr/bin/env python

import matplotlib.pyplot as plt
import serial
import time

serial_connection = serial.Serial("/dev/cu.usbmodem101", 9600)
timestamp_string = time.strftime("%Y-%m-%d-%H:%M")

latency_measurements = []
current_iteration = 0

# We will be removing the first measurement due to noise
number_of_iterations = 201

measurements_file_writer = open("latencyMeasurements_" + timestamp_string + ".csv", "wb")
statistics_file_writer = open("latencyStatistics_" + timestamp_string + ".txt", "wb")

while current_iteration < number_of_iterations:
    current_latency = int(serial_connection.readline())
    print("Iteration " + str(current_iteration) + ": " + str(current_latency) + "ms")
    
    latency_measurements.append(current_latency)
    current_iteration = current_iteration + 1

    measurements_file_writer.write(str(current_latency) + "\n")

# Removing the first measurement due to noise
latency_measurements.pop(0)

latency_statistics = "Min/Mean/Max latency: " + "%.2f" % (min(latency_measurements)) + "/" + "%.2f" % (sum(latency_measurements)/float(len(latency_measurements))) + "/" + "%.2f" % (max(latency_measurements)) + " ms"
statistics_file_writer.write(latency_statistics)
print(latency_statistics)

plt.hist(latency_measurements, bins="auto")
plt.title("Latency histogram")
plt.savefig("latency_histogram_" + timestamp_string + ".png")
plt.show()