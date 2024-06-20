mileage=float(input())
petrol=int(input())
distance=int(input())

if(mileage*petrol<distance): #Mileage*petrol gives us the amount of distance a vehicle can travel
  print("Cannot reach")#if it is smaller than the distance to be travelled it cannot be reached
else:
  print("Can reach")#if it is greater then it can be reached