import pandas as pd
import math

# Load hospital data
data = pd.read_csv("hospital_data.csv")

# Calculate distance using Haversine formula
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius (km)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (math.sin(dlat/2) * math.sin(dlat/2) +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) *
         math.sin(dlon/2) * math.sin(dlon/2))

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c


# Convert traffic level to delay factor
def traffic_factor(level):
    if level == "low":
        return 1
    elif level == "medium":
        return 1.5
    else:
        return 2


# AI Decision Function
def find_best_hospital(user_lat, user_lon, condition):

    best_hospital = None
    best_score = float("inf")

    for _, row in data.iterrows():

        # Skip if no ICU beds
        if row["icu_beds"] <= 0:
            continue

        # Check specialist match
        specialist_match = (row["specialist"] == condition)

        distance = calculate_distance(
            user_lat, user_lon,
            row["latitude"], row["longitude"]
        )

        traffic = traffic_factor(row["traffic_level"])

        # Score calculation (AI logic)
        score = distance * traffic

        # Give priority if specialist matches
        if specialist_match:
            score *= 0.7

        if score < best_score:
            best_score = score
            best_hospital = row

    return best_hospital


# 🚑 Driver Simulation
def ambulance_system():

    print("🚑 SMART AMBULANCE SYSTEM")
    print("---------------------------")

    # Simulated GPS location
    user_lat = float(input("Enter current latitude: "))
    user_lon = float(input("Enter current longitude: "))

    print("\nPatient Condition Options: cardiac / trauma / neuro")
    condition = input("Enter patient condition: ").lower()

    print("\n🔍 Finding best hospital...\n")

    result = find_best_hospital(user_lat, user_lon, condition)

    if result is not None:
        print("🏥 Recommended Hospital:")
        print("Name:", result["hospital_name"])
        print("Distance: {:.2f} km".format(
            calculate_distance(user_lat, user_lon,
                               result["latitude"], result["longitude"])
        ))
        print("ICU Beds Available:", result["icu_beds"])
        print("Specialist:", result["specialist"])
        print("Traffic Level:", result["traffic_level"])
    else:
        print("❌ No suitable hospital found!")


# Run system
if __name__ == "__main__":
    ambulance_system()