years = 2020
months  = 10
days = 28      

def AddDays(numOfDays):
    global days
    global months
    global years
    maxes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    maxDay = maxes[months-1]
    totalDays = days+numOfDays 

    while (totalDays>maxDay):
        
            months = months + 1
            if (months == 13):
                years = years + 1
                months = 1
            totalDays = totalDays - maxDay 
            maxDay = maxes[months-1]
  
    days = totalDays 

AddDays(10)
print(str(days) + " " + str(months)+" " + str(years))
