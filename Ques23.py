# Program to convert temperature from Celsius to Fahrenheit and vice versa based on user input

# Taking the temperature and unit as input from the user
temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()

# Converting the temperature based on the unit
if unit == 'C':
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {converted_temperature}°F.")
elif unit == 'F':
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {converted_temperature}°C.")
else:
    print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
