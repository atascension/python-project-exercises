def is_valid_unit(unit):
    return unit == "C" or unit == "F"
    


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def read_temperature():
    while True:
        try:
            response = float(input("Please enter a temperature: "))
        except ValueError:
            print("Enter a number, such as 72 or 21.5.")
        else:
            return response


def read_unit():
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? Enter C or F: ").strip().upper()
        try:
            if not is_valid_unit(unit):
                raise ValueError("Enter C for Celsius or F for Fahrenheit.")
        except ValueError:
            print("Enter C for Celsius or F for Fahrenheit.")
        else:
            return unit


def display_result(original_temperature, original_unit, converted_temperature, converted_unit):
    print(f"{original_temperature:.1f}°{original_unit} converts to {converted_temperature:.1f}°{converted_unit}")


print("Temperature Converter Part 2")
print("----------------------------")

user_temp = read_temperature()
temp_type = read_unit()

if temp_type == "C":
    converted_temp = celsius_to_fahrenheit(user_temp)
    display_result(user_temp, "C", converted_temp, "F")
else:
    converted_temp = fahrenheit_to_celsius(user_temp)
    display_result(user_temp, "F", converted_temp, "C")
