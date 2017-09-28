# Retrieves user inputs for speed and time. Casts str inputs to ints.
speed: int = int(input("What is the speed of the vehicle in mph?"))
time: int = int(input("How many hours has it traveled?"))

# Prints the table header.
print("Hour\tDistance Traveled")

# Calculates the total distance for every hour traveled.
for t in range(1, time + 1):
    print(f"{t}\t\t{t * speed}")
