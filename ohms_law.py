# ohms_law.py

# Ask the user for current and resistance
current = float(input("Enter the current (in A): "))
resistance = float(input("Enter the resistance (in ohms): "))

# Calculate voltage
voltage = current * resistance

# Show the result
print("The voltage is:", voltage, "volts")
# Ohm's Law: V = I * R