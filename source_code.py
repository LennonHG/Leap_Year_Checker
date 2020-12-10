year_21st = []

start_year = 0 # year count start's from 0. 

def leap_year(): # function based on formula used in "https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year"
    for year in year_21st: # to check whether it is leap year or not
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("{} the year is a leap year,it has 366 days".format(year))
                else:
                    print("{} the year is not a leap year, it has 365 days".format(year))
            else:
                print("{} the year is a leap year,it has 366 days".format(year))
        else:
            print("{} the year is not a leap year, it has 365 days".format(year))
            
def range_years(num1, num2):        # this stores the range of years user input in. 
    for i in range(num1, num2):
        year = start_year + i
        year_21st.append(year)
    print(year_21st)

print("Please enter range of years you want to check for leap year")
num1 = int(input("Start Year:")) # prompts user to input in the start year
num2 = int(input("End Year: "))  # prompts user to input in the end year
range_years(num1, num2) # initiate the store function
leap_year() # initiate the leap checker function 
