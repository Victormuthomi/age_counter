from datetime import datetime
today= datetime.today()

year_a=today.strftime('%Y')
year_a=int(year_a)

month_a=today.strftime('%m')
month_a=int(month_a)

day_a=today.strftime('%d')
day_a=int(day_a)

import time
name=input('Hello, Nice to meet you how should i call you:' + ' ')
b=print('welcome to age counter '+ " "+ name)
time=time.sleep(2)
year=input('What is your year of birth :' + " ")
year=int(year)
#asks for the year the user was born
if year >9999:
    print(name +" "+ 'sorry Years can only be between 0001-9999')

    year=input('Enter a valid year')
    year=int(year)
elif year > year_a:
    print(name.title() +" "+ 'sorry you year of birth should not be' 
    + ' ' + 'greater than' + ' ' + str(year_a))
    year=input('Enter a valid year')
    year=int(year)
#checks if the user has entered a valid year(same in months and days)
month=input('which month were you born in :' + ' ')
month=int(month)
if month>12:
    print(name +' ' + 'Sorry they are only 12 months in a year,')

    month=input('Enter a valid month:')
    month=int(month)
if month == 1:
	print('note the days should not be greater than 31')
	day=int(input('d'))
	if day > 31:
		print('eror2')
	else:
		print('a')

elif  month == 3:
	print('note that the days should not be greater than 31 days')
	day=int(input('d'))
	if day > 31:
		print('error')
	else:
		print('okey2')

elif  month == 5:
	print('note that the days should not be greater than 31 days')
	day=int(input('d'))
	if day > 31:
		print('error')
	else:
		print('okey2')
		
elif  month == 7:
	print('note that the days should not be greater than 31 days')
	day=int(input('d'))
	if day > 31:
		print('error')
	else:
		print('okey2')

elif  month == 8:
	print('note that the days should not be greater than 31 days')
	day=int(input('d'))
	if day > 31:
		print('error')
	else:
		print('okey2')
		
elif  month == 10:
	print('note that the days should not be greater than 31 days')
	day=int(input('d'))
	if day > 31:
		print('error')
	else:
		print('okey2')
		
elif  month == 12:
	print('note that the days should not be greater than 31 days')
	day=int(input('d'))
	if day > 31:
		print('error')
	else:
		print('okey2')

elif  month == 4:
	print('note that the days should not be greater than 30days')
	day=int(input('d'))
	if day > 30:
		print('error 1')
	else:
		print('okey256')

elif  month == 5:
	print('note that the days should not be greater than 30days')
	day=int(input('d'))
	if day > 30:
		print('error 1')
	else:
		print('okey256')
		
elif  month == 6:
	print('note that the days should not be greater than 30days')
	day=int(input('d'))
	if day > 30:
		print('error 1')
	else:
		print('okey256')
		
elif  month == 8:
	print('note that the days should not be greater than 30days')
	day=int(input('d'))
	if day > 30:
		print('error 1')
	else:
		print('okey256')
	
elif  month == 10:
	print('note that the days should not be greater than 30days')
	day=int(input('d'))
	if day > 30:
		print('error 1')
	else:
		print('okey256')
		
elif  month == 4:
	print('note that the days should not be greater than 30days')
	day=int(input('d'))
	if day > 11:
		print('error 1')
	else:
		print('okey256')
		
elif  month == 2 and year % 4 ==0 :
	print('note that the days should not be greater than 29days')
	day=int(input('d'))
	if day > 29:
		print('error 2')
	else:
		print('okey200')
		
elif  month == 2 and year % 4 !=0 :
	print('note that the days should not be greater than 28days')
	day=int(input('d'))
	if day > 28:
		print('error 3')
	else:
		print('okey300')


year_b= year_a-year

if month_a > month:
	month_b = month_a - month
	
elif month_a < month:
	months = month - month_a
	month_b = 12 - months
	year_b = year_b-1
	
elif month_a == month:
		year_b = year_b + 1
		month_b = month_a - month
	
if day_a > day:
	day_b = day_a - day
	
elif day_a < day:
	days = day - day_a
	if month == 1:
		day_b = 31 - days
	if month_a == month:
		month_b = 11
	else:
		month_b = month_b - 1
		
if day_a > day:
	day_b = day_a - day
	
elif day_a < day:
	days = day - day_a
	if month == 3:
		day_b = 31 - days
	if month_a == month:
		month_b = 11
	else:
		month_b = month_b - 1

if day_a > day:
	day_b = day_a - day
	
elif day_a < day:
	days = day - day_a
	if month == 5:
		day_b = 31 - days
	if month_a == month:
		month_b = 11
	else:
		month_b = month_b - 1

if day_a > day:
	day_b = day_a - day
	
elif day_a < day:
	days = day - day_a
	if month == 7:
		day_b = 31 - days
	if month_a == month:
		month_b = 11
	else:
		month_b = month_b - 1
		
if day_a > day:
	day_b = day_a - day
	
elif day_a < day:
	days = day - day_a
	if month == 8:
		day_b = 31 - days
	if month_a == month:
		month_b = 11
	else:
		month_b = month_b - 1
		
if day_a > day:
	day_b = day_a - day
	
elif day_a < day:
	days = day - day_a
	if month == 10:
		day_b = 31 - days
	if month_a == month:
		month_b = 11
	else:
		month_b = month_b - 1

if day_a > day:
	day_b = day_a - day
	
elif day_a < day:
	days = day - day_a
	if month == 12:
		day_b = 31 - days
	if month_a == month:
		month_b = 11
	else:
		month_b = month_b - 1
		
if day_a > day:
	day_b = day_a - day
	
elif day_a < day:
	days = day - day_a
	if month == 4:
		day_b = 30 - days
	if month_a == month:
		month_b = 11
	else:
		month_b = month_b - 1

if day_a > day:
	day_b = day_a - day
	
elif day_a < day:
	days = day - day_a
	if month == 6:
		day_b = 30 - days
	if month_a == month:
		month_b = 11
	else:
		month_b = month_b - 1
	


if day_a > day:
	day_b = day_a - day
	
elif day_a < day:
	days = day - day_a
	if month == 9:
		day_b = 30 - days
	if month_a == month:
		month_b = 11
	else:
		month_b = month_b - 1
		
if day_a > day:
	day_b = day_a - day
	
elif day_a < day:
	days = day - day_a
	if month == 11:
		day_b = 30 - days
	if month_a == month:
		month_b = 11
	else:
		month_b = month_b - 1

if day_a > day:
	day_b = day_a - day
	
elif day_a < day:
	days = day - day_a
	if month == 2 and year % 4 == 0:
		day_b = 29 - days
	if month_a == month:
		month_b = 11
	else:
		month_b = month_b - 1

if day_a > day:
	day_b = day_a - day
	
elif day_a < day:
	days = day - day_a
	if month == 2 and year % 4 != 0:
		day_b = 28 - days
	if month_a == month:
		month_b = 11
	else:
		month_b = month_b - 1
		
elif day_a == day:
		month_b = month_b + 1
		day_b = day_a - day


year_b = str(year_b)
month_b = str(month_b)
day_b = str(day_b)

print(name +' ' +'You are now' +' ' +year_b+' '+ 'years' +
','+month_b+' '+'months' + ' '+'and' + ' ' 
+day_b+ ' '+ ' '+ 'days' ' old')
