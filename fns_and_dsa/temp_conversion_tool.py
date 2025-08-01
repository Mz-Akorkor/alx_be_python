# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program logic
def main():
    temp_input = input("Enter the temperature to convert: ")

     # Check if the input is a valid number using if-else
    if temp_input.replace('.', '', 1).isdigit() or \
       (temp_input.startswith('-') and temp_input[1:].replace('.', '', 1).isdigit()):
        
        temp_input = float(temp_input)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            result = convert_to_fahrenheit(temp_input)
            print(f"{temp_input}°C is {result}°F")
        elif unit == 'F':
            result = convert_to_celsius(temp_input)
            print(f"{temp_input}°F is {result}°C")
        else:
            print("Invalid unit. Please enter C or F.")
    else:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()