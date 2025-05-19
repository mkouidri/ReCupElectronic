#!/usr/bin/env python 

# -*- coding: latin-1 -*- 

  

''' 

Accéléromètre MMA7455 branché à un Raspberry Pi. 

C'est un périphérique I2C, donc on le branche à SCL et SDA, et s'assurer 

que l'i2C a été préalablement paramétré sur le Raspbery Pi. 

  

Pour plus d'infos: 

http://electroniqueamateur.blogspot.com/2015/01/accelerometre-mma7455-et-raspberry-pi.html 

  

''' 

  

import smbus 

import time 

import math 

  

# Valeurs à ajouter à chaque mesure pour calibrer votre MMA7455 

ajustx = 0  # car j'obtenais -10 à la place de 0 

ajusty = 0  # car j'obtenais -19 à la place de 0 

ajustz = 0  # car j'obtenais 69 à la place de 63 

  

# Définition d'une classe associée au capteur 

class MMA7455: 

    bus = smbus.SMBus(1) 

     

    def __init__(self): 

        # Réglage de la définition. Le 3e parametre est 0x05 pour mesurer de -2g à +2g. 

        self.bus.write_byte_data(0x68, 0x16, 0x05) 

     

    # Lecture des valeurs en x, y et z 

    def getValueX(self): 
        return self.bus.read_byte_data(0x68, 0x06) + ajustx 

    def getValueY(self): 
        return self.bus.read_byte_data(0x68, 0x07) + ajusty 

    def getValueZ(self): 
        return self.bus.read_byte_data(0x68, 0x08) + ajustz 
    

    def getXYZ(sel):
        return self.x, self.y, self.z

    def getAccel(self):
        x, y , z = get(XYZ)
        total = math.sqrt(x * x + y * y + z * z) 

        return total
    




try: 
    while True: 

        x = mma.getValueX() 
        if x > 127: 
            x = x - 255 

        y = mma.getValueY() 
        if y > 127: 
            y = y - 255 

        z = mma.getValueZ() 
        if z > 127: 
             z = z - 255 

        # Valeur totale de l'accélération 

        total = math.sqrt(x * x + y * y + z * z) 

  

        # Calcul des angles et conversion en degrés 

        angleX = round(math.asin(x / total) * 180.0 / 3.1416) 
        angleY = round(math.asin(y / total) * 180.0 / 3.1416) 
        angleZ = round(math.acos(z / total) * 180.0 / 3.1416) 

        total = round(total) 

        print( 
            f'x = {x} y = {y} z = {z} total = {total} ' 
            f'anglex = {angleX} deg angley = {angleY} deg anglez = {angleZ} deg' 
        ) 

        time.sleep(0.2)  # Pause pour éviter une écriture trop rapide 

except KeyboardInterrupt: 

    print("Programme interrompu par l'utilisateur.") 

 