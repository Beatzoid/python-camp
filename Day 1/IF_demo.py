baseTemp = 72

while True:
	currentTemp = int(input("Please enter the room temperature in Fahrenheit: "))

	heater = False
	fan = False

	if currentTemp < baseTemp:
		heater = True
		fan = False
		print("Heater on")
		print("Fan off")
	elif currentTemp > baseTemp:
		heater = False
		fan = True
		print("Heater off")
		print("Fan on")
	else:
		fan = False
		heater = False
		print("Fan off")
		print("Heater off")
