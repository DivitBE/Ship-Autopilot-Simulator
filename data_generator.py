import csv
import math

# Initial GPS position
latitude = 12.9000
longitude = 77.5000

speed = 5.0      # m/s
heading = 90.0   # degrees

with open("../data/imu_gps_simulated_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "timestamp",
        "latitude",
        "longitude",
        "speed",
        "heading",
        "acc_x",
        "acc_y",
        "acc_z",
        "gyro_x",
        "gyro_y",
        "gyro_z",
        "roll",
        "pitch",
        "yaw"
    ])

    for t in range(14400):  # 4 hours
        heading += 0.01 * math.sin(t / 300)

        latitude += 0.00001 * math.cos(math.radians(heading))
        longitude += 0.00001 * math.sin(math.radians(heading))

        roll = 2 * math.sin(t / 50)
        pitch = 1 * math.sin(t / 70)
        yaw = heading

        writer.writerow([
            t,
            latitude,
            longitude,
            speed,
            heading,
            0.02,
            0.01,
            9.8,
            0.001,
            0.001,
            0.002,
            roll,
            pitch,
            yaw
        ])
