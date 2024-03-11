def calculate_discount(price, discount_percent):
  if discount_percent >=20:
    final_price=price-(price*(discount_percent/100))
  else:
    final_price=price
  print(f"The final price is {final_price}.")

price=int(input("What is the original price? "))
discount_percent=int(input("What is the discount percentage (as an integer)? "))
calculate_discount(price, discount_percent)