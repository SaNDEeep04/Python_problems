length=int(input())
water=int(input())
volume=length**3 #formula for volume
if(volume*1000<length):
  print("Cannot store")
else:
  print("Can store")