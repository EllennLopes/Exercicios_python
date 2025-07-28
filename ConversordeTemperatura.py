<<<<<<< HEAD
def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter the temperature in fahrenheit: "))
    celsius = float(fahrenheit - 32) * (5/9) 
    print ("The temperature in celsius is")
    print (round(celsius, 2))


def celsius_to_fahrenheit():
    celsius = float(input("Enter the temperature in celsius: "))
    fahrenheit = float(celsius * (9/5) + 32)
    print ("The temperature in fahrenheit is")
    print (round(fahrenheit, 2))    

def main():
    while True:
        choice = input("Type 'F' to convert Fahrenheit to Celsius or 'C' to convert Celsius to Fahrenheit: ").strip().upper()
        if choice == 'F':
            fahrenheit_to_celsius()
        elif choice == 'C':
            celsius_to_fahrenheit()
        elif choice == 'Q':
            print("Goodbye!")
        else:
            print("Invalid choice. Please enter 'F', 'C', or 'Q'.")
    

main()
=======
def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter the temperature in fahrenheit: "))
    celsius = float(fahrenheit - 32) * (5/9) 
    print ("The temperature in celsius is")
    print (round(celsius, 2))


def celsius_to_fahrenheit():
    celsius = float(input("Enter the temperature in celsius: "))
    fahrenheit = float(celsius * (9/5) + 32)
    print ("The temperature in fahrenheit is")
    print (round(fahrenheit, 2))    

def main():
    while True:
        choice = input("Type 'F' to convert Fahrenheit to Celsius or 'C' to convert Celsius to Fahrenheit: ").strip().upper()
        if choice == 'F':
            fahrenheit_to_celsius()
        elif choice == 'C':
            celsius_to_fahrenheit()
        elif choice == 'Q':
            print("Goodbye!")
        else:
            print("Invalid choice. Please enter 'F', 'C', or 'Q'.")
    

main()
>>>>>>> a5049ff4e84c593fc76a202aeff86fa1dace9175
