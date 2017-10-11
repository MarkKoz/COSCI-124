import locale

locale.setlocale(locale.LC_ALL, "en") # 'en': 'en_US.ISO8859-1'.

def calcCompInterest(p: float, i: float, t: int) -> float:
    return p * ((1 + i) ** t)

# Retrieves user inputs.
p: float = float(input("Enter the present value of the account: "))
i: float = float(input("Enter the monthly interest rate "
                       "as a percentage: ")) / 100
t: int = int(input("Enter the number of months the money will be left in the "
                   "account: "))

# Calls calculation function, formats return value as currency, and prints it.
print("Future value: "
      f"{locale.currency(calcCompInterest(p, i, t), grouping = True)}")