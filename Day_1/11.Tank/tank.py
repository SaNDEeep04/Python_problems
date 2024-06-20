radius=int(input())
height=int(input())
water_recieved=int(input())
total_hours=int(input())
volume= 3.14*(radius**2)*height #formula for volume of cylinder
if(water_recieved*total_hours>=volume): #we multiply the amount of water recieved with the time
    print("The tank can be filled within",total_hours,"hours")
else:
    print("The tank cannot be filled within",total_hours,"hours")
