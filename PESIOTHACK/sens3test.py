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
        return "Invalid soil type. Please enter 'red', 'sandy', 'clayey', or 'silty'."

    
    for crop_info in data_dict[soil]:
        crop_season = crop_info["season"].lower()
        crop_temperature = crop_info["temperature"]
        
        # Parse temperature range
        temp_range = crop_temperature.split(" to ")
        temp_min = int(temp_range[0].replace("°C", "").strip())
        temp_max = int(temp_range[1].replace("°C", "").strip())
        
        # Check conditions (season and temperature)
        if (season.lower() in crop_season) and (temp_min <= float(temperature) <= temp_max):
            # Append both the crop and its irrigation info
            suitable_crops.append(f"{crop_info['crop']} (Irrigation: {crop_info['irrigation']})")
             
    return suitable_crops if suitable_crops else ["No suitable crops found for the given conditions."]

def main():
    arduino_port = 'COM3'  # Change to your Arduino's serial port
    baud_rate = 9600  # Ensure this matches the baud rate in the Arduino sketch
    golainClient.connect()
    s = Shadow()
    try:
        ser = serial.Serial(arduino_port, baud_rate, timeout=1)
        time.sleep(2)  # Wait for the serial connection to initialize
        print("Connected to Arduino at port:", arduino_port)
        l=[]
        s.h=0
        s.t1=0
        s.sm1=0
        s.sm2=0
        ssv1=-1
        ssv2=-1
        s.t2=0
        s.sv1=0
        s.sv2=0
        while True:
            if ser.in_waiting > 0:  # Check if there's data waiting to be read
                line = str(ser.readline().decode('utf-8').rstrip())  # Read and decode the line
                l.append(list(line.split(" ")))
                for i in l:
                    if(ssv1!=int(i[1])):
                        print("24hrs ago",i[1],"%"," Fresh",i[3],"%"," temperature",i[5])
                        ssv1=int(i[1])
                        s.sv2=int(i[3])
                        if(ssv1==int(i[1])):
                            l=[]
                    elif(ssv2!=int(i[3])):
                        print("24hrs ago",i[1],"%"," Fresh",i[3],"%"," temperature",i[5])
                        ssv2=int(i[3])
                        s.sv1=int(i[1])
                        if(ssv2==int(i[3])):
                            l=[]
                    s.h=float(i[4])
                    s.sm1=int(i[1])
                    s.sm2=int(i[3])
                    s.t1=float(i[5])
                    s.t2=float(i[6])
                    s.sv1=int(i[0])
                    s.sv2=int(i[2])
                    break
                break
    except serial.SerialException as e:
        print(f"Error opening or communicating with serial port: {e}")
    except KeyboardInterrupt:
        print("Program terminated.")
    finally:
        if 'ser' in locals():
            ser.close()  # Close the serial port when done
    print("\nCrop Suggestion Program")
    golainClient.publishData('S', s.SerializeToString())
    # Take soil type and season as inputs from the user
    soil = input("Enter the soil type (red, sandy, clayey, silty): ").strip().lower()

    if soil not in data_dict:
        print("Invalid soil type. Please restart and enter a valid soil type.")
        return
    m=[]
    for crop_info in data_dict[soil]:
        m.append(crop_info["season"].lower())
    m1=set(m)
    print(m1)
    season = input("Enter the season").strip().lower()
    # Connect to the Arduino
    ser = serial.Serial('COM3', 9600)  # Change 'COM3' to your Arduino port
    time.sleep(2)  # Wait for the serial connection to initialize

    try:
    
        if ser.in_waiting > 0:
            #data = ser.readline().decode('utf-8').strip()
            #temperature, humidity, soil_moisture = map(float, data.split(','))
            #print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Soil Moisture: {soil_moisture}")
            temperature=s.t1
            humidity=s.h
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
