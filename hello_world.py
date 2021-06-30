# hello_world.py
# By Beatzoid
# 6/28/21

print("Welcome!\n--------")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = input("Please enter your height (format 5'8\"): ")
weight = int(input("Pleae enter your weight in pounds: "))
married = input("Are you married? ")
driversLicense = input("Do you have a drivers license? ")
phoneNumber = input("Please enter your phone number (format (123) 456-7890): ")
SSN = input("Please enter your social security number (format 123-45-6789): ")

print("\nHello " + name + "! You are currently " + str(age) +
      " years old with a height of " + str(height) +
      " and a weight of " + str(weight) + ". Your phone number is " + phoneNumber + " and your social security number is " + SSN + "\n\nOh you're " + str(age+1) + " now, happy birthday! ")
