#if the lengths of a square is equal to the diameter it will fit
rad=int(input())
length=int(input())
dia=rad*2
if (dia<=length):
  print("Circle can be inside a square")
else:
  print("Circle cannot be inside a square")

  #Note: Even though the sample output says to print out "The circle cannot be inside a square" & "The circle can be inside a square"
  #It actually is "Circle cannot be inside a square" & "Circle can be inside a square"