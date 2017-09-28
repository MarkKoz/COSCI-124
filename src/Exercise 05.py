import locale

locale.setlocale(locale.LC_ALL, "en") # 'en': 'en_US.ISO8859-1'.

rateAss: float = 0.6 # Used to calculate assessment value (60%).
rateTax: float = 0.0072 # Tax rate (72¢ per $100).

val: float = float(input("Enter the actual value of the property: "))
ass: float = val * rateAss # Assessment value.
tax: float = ass * rateTax # Tax on the assessment value.

print(f"Assessment value: {locale.currency(ass, grouping = True)}")
print(f"Property tax: {locale.currency(tax, grouping = True)}")
