rows = int(input())
column =int(input())
trees = int(input())
first_start = column +1
first_end = column * 2
last_start = column  *(rows- 1)
last_end = column  *(rows- 1)
if first_start <= trees <= first_end or last_start <= trees <= last_end:
  print("It is an orange tree")
else:
  print("It is not an orange tree")

#I have no idea how this program passed the three test cases
