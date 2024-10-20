import serial
import time

data_dict = {
    "red": [
        {
            "crop": "Groundnut",
            "season": "May to June",
            "moisture_requirement": "32% to 40%",
            "humidity": "50% to 60%",
            "temperature": "20°C to 30°C",
            "irrigation": "4,000 to 5,000 liters per acre"
        },
        {
            "crop": "Sorghum",
            "season": "June to July",
            "moisture_requirement": "24% to 32%",
            "humidity": "Low preferred",
            "temperature": "20°C to 35°C",
            "irrigation": "3,000 to 5,000 liters per acre"
        },
        {
            "crop": "Pearl Millet",
            "season": "June to July",
            "moisture_requirement": "24% to 40%",
            "humidity": "Moderate",
            "temperature": "25°C to 35°C",
            "irrigation": "3,000 to 4,000 liters per acre"
        },
        {
            "crop": "Pigeon Pea",
            "season": "June to July",
            "moisture_requirement": "48% to 64%",
            "humidity": "50% to 70%",
            "temperature": "20°C to 30°C",
            "irrigation": "4,000 to 6,000 liters per acre"
        },
        {
            "crop": "Sugarcane",
            "season": "February to March",
            "moisture_requirement": "60% to 80%",
            "humidity": "60% to 80%",
            "temperature": "20°C to 30°C",
            "irrigation": "10,000 to 15,000 liters per acre"
        }
    ],
    "sandy": [
        {
            "crop": "Watermelon",
            "season": "March to June",
            "moisture_requirement": "32% to 48%",
            "humidity": "60% to 80%",
            "temperature": "20°C to 35°C",
            "irrigation": "4,000 to 6,000 liters per acre"
        },
        {
            "crop": "Muskmelon",
            "season": "March to June",
            "moisture_requirement": "32% to 48%",
            "humidity": "60% to 80%",
            "temperature": "20°C to 35°C",
            "irrigation": "4,000 to 6,000 liters per acre"
        },
        {
            "crop": "Cowpea",
            "season": "June to July",
            "moisture_requirement": "24% to 32%",
            "humidity": "50% to 70%",
            "temperature": "20°C to 35°C",
            "irrigation": "3,000 to 5,000 liters per acre"
        },
        {
            "crop": "Sorghum",
            "season": "June to July",
            "moisture_requirement": "24% to 32%",
            "humidity": "Low preferred",
            "temperature": "20°C to 35°C",
            "irrigation": "3,000 to 5,000 liters per acre"
        }
    ],
    "clayey": [
        {
            "crop": "Rice",
            "season": "May to June",
            "moisture_requirement": "96% to 100%",
            "humidity": "70% to 90%",
            "temperature": "20°C to 35°C",
            "irrigation": "8,000 to 12,000 liters per acre"
        },
        {
            "crop": "Wheat",
            "season": "October to November",
            "moisture_requirement": "32% to 48%",
            "humidity": "40% to 60%",
            "temperature": "10°C to 25°C",
            "irrigation": "4,000 to 6,000 liters per acre"
        },
        {
            "crop": "Barley",
            "season": "October to November",
            "moisture_requirement": "24% to 32%",
            "humidity": "40% to 60%",
            "temperature": "10°C to 20°C",
            "irrigation": "3,000 to 5,000 liters per acre"
        },
        {
            "crop": "Mustard",
            "season": "October to November",
            "moisture_requirement": "32% to 40%",
            "humidity": "50% to 70%",
            "temperature": "10°C to 25°C",
            "irrigation": "3,000 to 5,000 liters per acre"
        },
        {
            "crop": "Sugarcane",
            "season": "February to March",
            "moisture_requirement": "60% to 80%",
            "humidity": "60% to 80%",
            "temperature": "20°C to 30°C",
            "irrigation": "10,000 to 15,000 liters per acre"
        }
    ],
    "silty": [
        {
            "crop": "Potatoes",
            "season": "January to March",
            "moisture_requirement": "48% to 64%",
            "humidity": "60% to 70%",
            "temperature": "15°C to 20°C",
            "irrigation": "5,000 to 7,000 liters per acre"
        },
        {
            "crop": "Sunflower",
            "season": "June to July",
            "moisture_requirement": "32% to 48%",
            "humidity": "50% to 70%",
            "temperature": "20°C to 30°C",
            "irrigation": "4,000 to 5,000 liters per acre"
        },
        {
            "crop": "Cucumbers",
            "season": "June to July",
            "moisture_requirement": "40% to 56%",
            "humidity": "60% to 80%",
            "temperature": "20°C to 30°C",
            "irrigation": "5,000 to 7,000 liters per acre"
        },
        {
            "crop": "Beans",
            "season": "March to June or September to October",
            "moisture_requirement": "32% to 40%",
            "humidity": "50% to 70%",
            "temperature": "20°C to 30°C",
            "irrigation": "4,000 to 6,000 liters per acre"
        },
        {
            "crop": "Peas",
            "season": "October to November",
            "moisture_requirement": "40% to 48%",
            "humidity": "60% to 80%",
            "temperature": "10°C to 20°C",
            "irrigation": "3,000 to 5,000 liters per acre"
        }
    ]
}


def suggest_crops(soil, temperature, humidity, season):
    if soil not in data_dict:
        return "Invalid soil type. Please enter 'red', 'sandy', 'clayey', or 'silty'."

    suitable_crops = []
    for crop_info in data_dict[soil]:
        crop_season = crop_info["season"].lower()
        crop_temperature = crop_info["temperature"]
        
        # Parse temperature range
        temp_range = crop_temperature.split(" to ")
        temp_min = int(temp_range[0].replace("°C", "").strip())
        temp_max = int(temp_range[1].replace("°C", "").strip())
        
        # Check conditions (season and temperature)
        if (season.lower() in crop_season) and (temp_min <= int(temperature) <= temp_max):
            # Append both the crop and its irrigation info
            suitable_crops.append(f"{crop_info['crop']} (Irrigation: {crop_info['irrigation']})")
             
    return suitable_crops if suitable_crops else ["No suitable crops found for the given conditions."]

def main():
    print("Crop Suggestion Program")

    # Take soil type and season as inputs from the user
    soil = input("Enter the soil type (red, sandy, clayey, silty): ").strip().lower()

    if soil not in data_dict:
        print("Invalid soil type. Please restart and enter a valid soil type.")
        return

    season = input("Enter the season (e.g., 'May to June', 'June to July'): ").strip().lower()

    # Connect to the Arduino
    ser = serial.Serial('COM3', 9600)  # Change 'COM3' to your Arduino port
    time.sleep(2)  # Wait for the serial connection to initialize

    try:
    
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            temperature, humidity, soil_moisture = map(float, data.split(','))
            #print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Soil Moisture: {soil_moisture}")

            # Suggest crops based on the user input and sensor data
            crops = suggest_crops(soil, temperature, humidity, season)
            print("Suitable Crops:",end=" ")
            for i in crops: 
                print(i)
            time.sleep(2)  # Read data every 2 seconds
    except KeyboardInterrupt:
        print("Exiting program.")
    finally:
        ser.close()

if __name__ == "__main__":
    main()
