import smbus 

import time 

  

# Adresse I2C du MPU6050 

MPU6050_ADDR = 0x68 

  

# Registres du MPU6050 

MPU6050_PWR_MGMT_1 = 0x6B 

MPU6050_ACCEL_XOUT_H = 0x3B 

MPU6050_GYRO_XOUT_H = 0x43 

  

# Initialisation de l'I2C 

bus = smbus.SMBus(1)  # Utilisez 1 pour la plupart des Raspberry Pi modernes 

  

def write_register(device_addr, reg_addr, data): 

    """Écrit un octet dans un registre.""" 

    bus.write_byte_data(device_addr, reg_addr, data) 

  

def read_register_16(device_addr, reg_addr): 

    """Lit deux octets (16 bits) depuis un registre.""" 

    high = bus.read_byte_data(device_addr, reg_addr) 

    low = bus.read_byte_data(device_addr, reg_addr + 1) 

    value = (high << 8) | low 

    if value >= 0x8000:  # Convertir en entier signé 

        value = -((65535 - value) + 1) 

    return value 

  

# Initialisation du MPU6050 

write_register(MPU6050_ADDR, MPU6050_PWR_MGMT_1, 0x00)  # Réveil du capteur 

  

try: 

    while True: 

        # Lire les données d'accéléromètre 

        accel_x = read_register_16(MPU6050_ADDR, MPU6050_ACCEL_XOUT_H) 

        accel_y = read_register_16(MPU6050_ADDR, MPU6050_ACCEL_XOUT_H + 2) 

        accel_z = read_register_16(MPU6050_ADDR, MPU6050_ACCEL_XOUT_H + 4) 

  

        # Lire les données de gyroscope 

        gyro_x = read_register_16(MPU6050_ADDR, MPU6050_GYRO_XOUT_H) 

        gyro_y = read_register_16(MPU6050_ADDR, MPU6050_GYRO_XOUT_H + 2) 

        gyro_z = read_register_16(MPU6050_ADDR, MPU6050_GYRO_XOUT_H + 4) 

  

        # Afficher les résultats 

        print(f"Accel: X={accel_x}, Y={accel_y}, Z={accel_z}") 

        print(f"Gyro:  X={gyro_x}, Y={gyro_y}, Z={gyro_z}") 

        print("-----------------------") 

        time.sleep(0.1) 

  

except KeyboardInterrupt: 

    print("Arrêt du programme.") 

 