p1=float(input())
p2=float(input())
disc=float(input())
decimal_disc=disc/100 #converting discount to decimal
final_p1=p1*decimal_disc #price of product with discount
final_p2=p2*decimal_disc
final=(final_p1+final_p2) #price of product added
p=p1+p2
print("%.2f" %p) #.2f is used so as to get output only upto two decimals
print("%.2f" %(p-final))
print("%.2f" %final)