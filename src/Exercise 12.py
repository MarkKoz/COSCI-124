import locale

locale.setlocale(locale.LC_ALL, "en") # 'en': 'en_US.ISO8859-1'.

"""
Purchase
"""
shares: int = 2000 # Quantity of shares purchased.
price: int = 40 # Price paid for each share.
rate: float = 0.03 # Brokerage commission rate %.

total: float = shares * price # Total price paid for all shares.
print("Purchase - total price of shares: "
      f"{locale.currency(total, grouping = True)}")

commission: float = total * rate # Amount paid to brokerage.
print("Purchase - commission: "
      f"{locale.currency(commission, grouping = True)}\n")

"""
Sale
"""
sharesSale: int = 2000 # Quantity of shares purchased.
priceSale: float = 42.75 # Price paid for each share.
rateSale: float = 0.03 # Brokerage commission rate %.

# Total amount received for the sale of all shares.
totalSale: float = sharesSale * priceSale
print("Sale - total price of shares: "
      f"{locale.currency(totalSale, grouping = True)}")

commissionSale: float = totalSale * rateSale # Amount paid to brokerage.
print(f"Sale - commission: {locale.currency(commissionSale, grouping = True)}"
      "\n")

"""
Profit
"""
gross: float = totalSale - total # Gross profit.
# Net profit, taking into account commission expenses.
net: float = gross - commission - commissionSale

# Determines profit or loss based on the sign of the net value.
if net > 0:
    print(f"Net: {locale.currency(net, grouping = True)}\nMade a profit.")
elif net < 0:
    print(f"Net: {locale.currency(net, grouping = True)}\nMade a loss.")
else:
    print(f"Net: {locale.currency(net, grouping = True)}\nBroke even.")
