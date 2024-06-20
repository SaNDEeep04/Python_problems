bought=int(input())
sold_1=int(input())
sold=sold_1*12 #Converting prize of dozen sold to single unit
if sold>bought:
    print(f"Profit : Rs.{int(sold-bought)}")#Formula for profit
elif sold<bought:
    print(f"Loss : Rs.{int(bought-sold)}")#Formula for loss
else:
   print("No profit nor loss")