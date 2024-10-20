import tkinter as tk
import serial
import time
from golain import GolainClient
from data_pb2 import Shadow


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
            "temperature": "10°C to 26°C",
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

golainClient = GolainClient(None)

def suggest_crops(soil, temperature, humidity, season):
    suitable_crops = []
    if soil not in data_dict:
        return ["Invalid soil type. Please enter 'red', 'sandy', 'clayey', or 'silty'."]

    for crop_info in data_dict[soil]:
        crop_season = crop_info["season"].lower()
        crop_temperature = crop_info["temperature"]
        
        # Parse temperature range
        temp_range = crop_temperature.split(" to ")
        temp_min = int(temp_range[0].replace("°C", "").strip())
        temp_max = int(temp_range[1].replace("°C", "").strip())
        
        # Check conditions (season and temperature)
        if (season.lower() in crop_season) and (temp_min <= float(temperature) <= temp_max):
            suitable_crops.append(f"{crop_info['crop']} (Irrigation: {crop_info['irrigation']})")
             
    return suitable_crops if suitable_crops else ["No suitable crops found for the given conditions."]

def get_sensor_data():
    arduino_port = 'COM3'  # Change to your Arduino's serial port
    baud_rate = 9600
    s = Shadow()
    try:
        ser = serial.Serial(arduino_port, baud_rate, timeout=1)
        time.sleep(2)
        if ser.in_waiting > 0:
            line = str(ser.readline().decode('utf-8').rstrip())
            data = list(line.split(" "))
            s.h = float(data[4])
            s.t1 = float(data[5])
            return s.t1, s.h
    except serial.SerialException as e:
        print(f"Error opening or communicating with serial port: {e}")
    return None, None

def on_submit():
    soil = soil_var.get()
    season = season_var.get()
    
    temperature, humidity = get_sensor_data()
    if temperature is None or humidity is None:
        return  # If sensor data couldn't be retrieved
    
    crops = suggest_crops(soil, temperature, humidity, season)
    result_text = "\n".join(crops)
    
    # Update label with crop suggestions
    result_label.config(text=result_text)

# Create the main window
root = tk.Tk()
root.title("Crop Suggestion Tool")
root.geometry("500x300")  # Set the window size to 500x300 pixels

# Create labels and input fields
tk.Label(root, text="Select Soil Type:").pack(pady=5)
soil_var = tk.StringVar()
tk.OptionMenu(root, soil_var, *data_dict.keys()).pack(pady=5)

tk.Label(root, text="Enter Season:").pack(pady=5)
season_var = tk.StringVar()
tk.Entry(root, textvariable=season_var).pack(pady=5)

# Submit button
tk.Button(root, text="Get Crop Suggestions", command=on_submit).pack(pady=20)

# Label for displaying crop suggestions
result_label = tk.Label(root, text="", justify="left", anchor="nw")
result_label.pack(pady=10, padx=10)

# Start the GUI loop
root.mainloop()
