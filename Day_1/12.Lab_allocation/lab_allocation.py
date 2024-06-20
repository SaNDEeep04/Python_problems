#This question is very simple but the question is phrased in a confusing manner
#It expects us to print the smallest lab other than the lab input given by the user
L1=int(input())
L2=int(input())
L3=int(input())
face=input()
#I solved it by comparing all the elements with each for each face input
#If there is a easier i.e smaller way please inform me
if face=="L1":
    if(L2<L3):
        print("L2")
    else:
        print("L3")
elif face=="L2":
    if(L1<L3):
        print("L1")
    else:
        print("L3")
elif face=="L3":
    if(L1<L2):
        print("L1")
    else:
        print("L2")