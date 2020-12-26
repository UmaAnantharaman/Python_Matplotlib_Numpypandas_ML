from datetime import date

def numofdays(date1,date2):
    return (date2- date1).days

#Difference between 2 dates using datetime 
date1 = date(2018,12,10)
date2 = date(2019,10,4)
print(numofdays(date1,date2),"days")
