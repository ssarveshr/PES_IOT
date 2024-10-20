import serial
import time
arduino_port = 'COM3'  # Change to your Arduino's serial port
baud_rate = 9600  # Ensure this matches the baud rate in the Arduino sketch
try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)  # Wait for the serial connection to initialize
    print("Connected to Arduino at port:", arduino_port)
    l=[]
    backup=[]
    ssv1=-1
    ssv2=-1
    while True:
        if ser.in_waiting > 0:  # Check if there's data waiting to be read
            line = str(ser.readline().decode('utf-8').rstrip())  # Read and decode the line
            l.append(list(line.split(" ")))
            for i in l:
                if(ssv1!=int(i[1])):
                    print("24hrs ago",i[1],"%"," Fresh",i[3],"%"," temperature",i[5])
                    ssv1=int(i[1])
                    ssv2=int(i[3])
                    if(ssv1==int(i[1])):
                        l=[]
                elif(ssv2!=int(i[3])):
                    print("24hrs ago",i[1],"%"," Fresh",i[3],"%"," temperature",i[5])
                    ssv2=int(i[3])
                    ssv1=int(i[1])
                    if(ssv2==int(i[3])):
                        l=[]
except serial.SerialException as e:
    print(f"Error opening or communicating with serial port: {e}")
except KeyboardInterrupt:
    print("Program terminated.")
finally:
    if 'ser' in locals():
        ser.close()  # Close the serial port when done
        print("Serial connection closed.")


