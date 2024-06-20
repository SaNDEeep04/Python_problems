adult=75
child=30
weight=int(input())
no_adults=int(input())
no_children=int(input())
total=(no_adults*adult)+(no_children*child)#Obtaining the total by adding the weights of the adults and the children
if(total>weight): #If total weight greater than boat then it will sink
  print("Boat will sink")
else: #Else it will float
  print("Boat is stable")