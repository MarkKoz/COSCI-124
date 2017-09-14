"""
Purchase
"""
shares: int = 2000 # Quantity of shares purchased.
price: float = 40.00 # Price paid for each share.
rate: float = 0.03 # Brokerage commission rate %.

total: float = shares * price # Total price paid for all shares.
print(f"Purchase - total price of shares: {total}")

commission: float = total * rate # Amount paid to brokerage.
print(f"Purchase - commission: {commission}\n")

"""
Sale
"""
sharesSale: int = 2000 # Quantity of shares purchased.
priceSale: float = 42.75 # Price paid for each share.
rateSale: float = 0.03 # Brokerage commission rate %.

# Total amount received for the sale of all shares.
totalSale: float = sharesSale * priceSale
print(f"Sale - total price of shares: {totalSale}")

# Net profit, taking into account commission expenses.
commissionSale: float = totalSale * rateSale # Amount paid to brokerage.
print(f"Sale - commission: {commissionSale}\n")

"""
Profit
"""
gross: float = totalSale - total # Gross profit.
net: float = gross - commission - commissionSale

# Determines profit or loss based on the sign of the net value.
if net > 0:
    print(f"Net: {net}\nMade a profit.")
elif net < 0:
    print(f"Net: {net}\nMade a loss.")
else:
    print(f"Net: {net}\nBroke even.")
