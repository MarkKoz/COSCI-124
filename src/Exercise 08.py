import locale

locale.setlocale(locale.LC_ALL, "en") # 'en': 'en_US.ISO8859-1'.

gal: float = 1 / 112 # Gallons of paint required per ft² of wall space.
hours: float = 0.125 # Hours of work required per ft² of wall space.
rate: int = 35 # $ charged per hour of work.

# Retrieves user inputs.
space: float = float(input("Enter the amount of wall space to paint in ft²: "))
price: float = float(input("Enter the price of paint per gallon in $: "))

paint: float = space * gal # Gallons of paint required.
paintPrice: float = paint * price # Total price of the paint required.
labour: float = space * hours # Hours of labour required.
labourPrice: float = labour * rate # Total price of the labour required.

print(f"Paint required: {paint} gal")
print(f"Paint cost: {locale.currency(paintPrice, grouping = True)}")
print(f"Labour required: {labour} hr")
print(f"Cost of labour: {locale.currency(labourPrice, grouping = True)}")
print("Total cost of job: "
      f"{locale.currency(paintPrice + labourPrice, grouping = True)}")
