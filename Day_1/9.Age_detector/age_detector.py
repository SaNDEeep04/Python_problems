birth_year=int(input())
current_year=int(input())
#if the person is born in the previous century the output may differ
#to fix this we subtract 100 and add it to current year
prev_cent=(100-birth_year)+current_year
age=current_year-birth_year
if(birth_year<=current_year):
    print(age)
else:
    print(prev_cent)
 