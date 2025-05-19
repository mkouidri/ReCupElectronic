import serial
import time

def send_at(command, delay=1):
    ser.write((command + "\r\n").encode())
    time.sleep(delay)
    response = ser.read_all().decode(errors='ignore')
    return response

# Ouvre la communication série
ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=2)
time.sleep(2)  # laisse le temps au module de démarrer

print("Activation du GPS...")
print(send_at("AT"))  # test de communication
print(send_at("AT+CGNSPWR=1"))  # active le GPS
time.sleep(2)

print("Lecture des données GPS...")
while True:
    gps_data = send_at("AT+CGNSINF")
    print("Données GPS brutes :", gps_data)

    # Tu peux parser ici si nécessaire :
    if "+CGNSINF:" in gps_data:
        parts = gps_data.split(',')
        if parts[1] == '1':  # fix GPS obtenu
            latitude = parts[3]
            longitude = parts[4]
            altitude = parts[5]
            print(f"✅ Fix GPS : {latitude}, {longitude}, Altitude : {altitude} m")
            break
        else:
            print("❌ Pas encore de fix GPS...")
    else:
        print("Réponse invalide")

    time.sleep(3)

ser.close()
