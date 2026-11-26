def convert_price(price):
    value = float(price)

    if value < 0:
        raise ValueError("Price cannot be negative")

    return value

try:
    price = convert_price("-50")
    print("Price:", price)

except ValueError as e:
    print("Invalid price:", e)