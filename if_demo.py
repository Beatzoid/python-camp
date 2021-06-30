# if_demo.py
# By Beatzoid
# 6/28/21

currentTemp = 72
desiredTemp = int(input("What is the desired temperature? "))

heater = False
fan = False

if currentTemp < desiredTemp:
    heater = True
    fan = False
    print("Heater on")
    print("Fan off")
elif currentTemp > desiredTemp:
    fan = True
    heater = False
    print("Fan on")
    print("Heater off")
else:
    heater = False
    fan = False
    print("Heater off")
    print("Fan off")
