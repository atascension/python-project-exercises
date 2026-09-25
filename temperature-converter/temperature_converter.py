"""
def is_valid_unit(unit):
    if unit == "C" or unit == "F":
        return True
    else:
        return False

The below is the equivilant of this ↑
"""

def is_valid_unit(unit):
    return unit == "C" or unit == "F"


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def display_result(original_temperature, original_unit, converted_temperature, converted_unit):
    print(f"{original_temperature:.1f}°{original_unit} converts to {converted_temperature:.1f}°{converted_unit}")


print("Temperature Converter")
print("---------------------")

user_temp = float(input("Please enter a temperature: "))
temp_type = input("Is this temperature in Celsius or Fahrenheit? Enter C or F: ").strip().upper()

if is_valid_unit(temp_type):
    if temp_type == "C":
        converted_temp = celsius_to_fahrenheit(user_temp)
        display_result(user_temp, "C", converted_temp, "F")
    else:
        converted_temp = fahrenheit_to_celsius(user_temp)
        display_result(user_temp, "F", converted_temp, "C")
else:
    print("The unit entered is invalid!")
