# get user input
your_year =  input("Enter a year: ")
val = True
while val:
    if your_year.isdigit():
        if int(your_year) >= 0:
            break
    your_year =  input("Enter a year: ")

year = int(your_year)
if year % 12 == 0:
    print(your_year + ' is the year of Monkey. ')
elif year % 12 == 1:
    print(your_year + ' is the year of Rooster. ')
elif year % 12 == 2:
    print(your_year + ' is the year of Dog. ')
elif year % 12 == 3:
    print(your_year + ' is the year of Pig. ')
elif year % 12 == 4:
    print(your_year + ' is the year of Rat. ')
elif year % 12 == 5:
    print(your_year + ' is the year of Ox. ')
elif year % 12 == 6:
    print(your_year + ' is the year of Tiger. ')
elif year % 12 == 7:
    print(your_year + ' is the year of Hare. ')
elif year % 12 == 8:
    print(your_year + ' is the year of Dragon. ')
elif year % 12 == 9:
    print(your_year + ' is the year of Snake. ')
elif year % 12 == 10:
    print(your_year + ' is the year of Horse. ')
else:
    print(your_year + ' is the year of Snake. ')

## you code needs to do the following things:
## 1. check if it is a integer; if not, ask the user to re input 
## 2. check if it is non negative; if not, ask the user to re input 
## 3. print the user's animal of the year on the screen

