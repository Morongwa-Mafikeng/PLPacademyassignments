#calculating final price after discount
def calculate_discount(price, discount_percent):
    
    if discount_percent == 0.2 or discount_percent > 0.2:
        amount_after_discount = price- (price * discount_percent)
        return f"Amount after discount = {amount_after_discount}"
    else:
        return f"The original price = {price}"

price = 53454.20
discount_percent = 0.2 #the discount is 20% so it is equal to 0.2    
print(calculate_discount(price, discount_percent))

# user prompts for price and discount_percent which should be enter not in percentages.

price = float(input("Enter the price of an item: "))
discount_percent = float(input("Enter the discount of the item: "))
print(calculate_discount(price, discount_percent))



