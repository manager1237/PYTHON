def calculate_discount(price, discount_percent):
            if discount_percent >= 20:
                discount_amount = price * (discount_percent / 100)
                return price - discount_amount
            else:
                return price

price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
else:
    print(f"No discount applied. Original price: {final_price:.2f}")


