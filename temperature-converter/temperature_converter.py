print("Welcome to the Python Temperature Converter") 
print("---------------------------")

user_temp = float(input("Please enter a temperature: "))
temp_type = input("Is this temperature in Celsius or Fahrenheit? Enter C or F: ").strip().lower()

def is_valid_unit(unit):
    if unit == "C" or unit =="F":
        return True
    else:
        print("The unit entered is invalid!")
        return False

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

if temp_type == "C" or temp_type == "c":
    celsius_to_fahrenheit(user_temp)
    print(celsius_to_fahrenheit(user_temp))
elif temp_type == "F" or temp_type == "f":
    fahrenheit_to_celsius(user_temp)
    print(celsius_to_fahrenheit(user_temp))
