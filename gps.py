import serial
import time
import re

def send_at_command(serial_connection, command, delay=1):
    serial_connection.write((command + '\r\n').encode())
    time.sleep(delay)
    response = serial_connection.read_all().decode('utf-8', errors='ignore')
    return response

def ddm_to_decimal(ddm):
    ddm = float(ddm)
    degrees = int(ddm/100)
    minutes = ddm - (degrees * 100)
    return degrees + (minutes / 60)
    
def get_gps_coordinates():
    try:
        serial_connection = serial.Serial(
            port='/dev/serial0', 
            baudrate=9600,
            timeout=1
        )
        
        if not serial_connection.isOpen():
            serial_connection.open()
        
        print("Activation du GPS...")
        response = send_at_command(serial_connection, "AT+CGPSPWR=1")
        print(response)
        
        print("Vérification de l'état du GPS...")
        response = send_at_command(serial_connection, "AT+CGPSSTATUS?")
        print(response)
        
        print("Obtention des coordonnées GPS...")
        while True:
            response = send_at_command(serial_connection, "AT+CGPSINF=0")
            print(f"Réponse brute: {response}")
            
            match = re.search(r'\+CGPSINF: 0,([0-9.]+),([0-9.]+),', response)
            if match:
                latitude = ddm_to_decimal(match.group(1))
                longitude = ddm_to_decimal(match.group(2))
                print(f"Coordonnées GPS: {latitude},{longitude}")
                break
            else:
                print("Coordonnées non disponibles. Nouvelle tentative...")
                time.sleep(5)

    except Exception as e:
        print(f"Erreur: {e}")
    finally:
        if serial_connection and serial_connection.isOpen():
            serial_connection.close()

if __name__ == "__main__":
    get_gps_coordinates()
