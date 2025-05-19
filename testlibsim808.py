import SIM808 as GPS

gps = GPS.GPS('/dev/serial0', 9600)
gps.setPowerOn()

coordinates = gps.getLocation()

print("lat = ", coordinates[0], "lng = ",coordinates[1])
