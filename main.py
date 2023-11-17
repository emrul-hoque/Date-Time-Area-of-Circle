from datetime import datetime
import math

current = datetime.now()

print("\n\nToday's date is\t",current.strftime("%d-%B-%Y"), "\n")

print("The current time is\t",current.strftime("%H:%M %p"), "\n\n")

r = float(input("Enter the radius of the circle:\t"))
area = math.pi * r**2
print("\nThe area of the circle is:\t", area, "\n")
