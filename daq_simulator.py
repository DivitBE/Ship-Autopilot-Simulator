import csv
import time
import requests

API_KEY = "YOUR_API_KEY"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

with open("../data/imu_gps_simulated_data.csv", "r") as file:
    reader = csv.DictReader(file)
    last_upload_time = time.time()

    for row in reader:
        # ---- Serial Monitor Simulation ----
        print(
            f"Time: {row['timestamp']} | "
            f"Lat: {row['latitude']} | Lon: {row['longitude']} | "
            f"Speed: {row['speed']} | Heading: {row['heading']} | "
            f"Roll: {row['roll']} | Pitch: {row['pitch']} | Yaw: {row['yaw']}"
        )

        # ---- ThingSpeak Upload (every 15 seconds) ----
        if time.time() - last_upload_time >= 15:
            payload = {
                "api_key": API_KEY,
                "field1": row["latitude"],
                "field2": row["longitude"],
                "field3": row["speed"],
                "field4": row["heading"],
                "field5": row["roll"],
                "field6": row["pitch"],
                "field7": row["yaw"],
            }
            requests.get(THINGSPEAK_URL, params=payload)
            last_upload_time = time.time()

        # ---- Real-time behavior ----
        time.sleep(1)
