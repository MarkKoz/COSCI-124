# Retrieves use inputs, all cast to ints. inc is divide by 100 to convert
# percentage into decimal.
start: float = int(input("Starting number of organisms: "))
inc: float = int(input("Average daily increase: ")) / 100
days: int = int(input("Number of days to multiply: "))

# Prints the table header and the result for the first day because there is
# no growth at the start of the first day.
print("\nDay Approximate\t\tPopulation")
print(f"{1}\t\t\t\t\t{start}")

# Iterates
for i in range(1, days):
    start += start * inc
    print(f"{i + 1}\t\t\t\t\t{start}")
