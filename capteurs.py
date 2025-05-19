from mpu6050 import mpu6050
import time
import math
# Initialisation du capteur
sensor = mpu6050(0x68)  # Adresse I2C par défaut du MPU6050
ajustX = -8.88 # A ajuster en fonction de l'emplacement du capteur
ajustY = -3.42 # A ajuster en fonction de l'emplacement du capteur
ajustZ = 0.10 # A ajuster en fonction de l'emplacement du capteur

# Lecture des données d'accélération
def read_accelerometer():
    
    accelerometer_data = sensor.get_accel_data()
    x = accelerometer_data['x'] - ajustX
    y = accelerometer_data['y'] - ajustY
    z = accelerometer_data['z'] - ajustZ
    
    # Calcul de l'accélération globale
    global_acceleration = math.sqrt(x**2 + y**2 + z**2)
    
    print("Données d'accélération (g) :")
    print(f"X : {x:.2f} g")
    print(f"Y : {y:.2f} g")
    print(f"Z : {z:.2f} g")
    print(f"Accélération globale : {global_acceleration:.2f} Km/h²")


# Boucle principale
if __name__ == "__main__":
    try:
        while True:
            read_accelerometer()
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("Arrêt du programme.")





