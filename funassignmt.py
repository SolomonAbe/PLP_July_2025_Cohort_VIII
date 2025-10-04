def calculate_discount(price, discount_percent):
    #Calculate final price after applying discount if >= 20%."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price 
# Prompt user input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    print(f"Final price: {final_price:.2f}")
except ValueError:
    print("Please enter valid numbers for price and discount.")