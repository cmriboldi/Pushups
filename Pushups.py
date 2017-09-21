import math

worldRecord = 1500230
setsPerDay = 3
increasePerDay = 1

def getYearlyAmount(setsPerDay, increasePerDay):
    yearlyAmount = 0
    for day in range(1,366):
        yearlyAmount += day * setsPerDay * increasePerDay
    return yearlyAmount

def calcStartDate(worldRecord, setsPerDay, increasePerDay):
    day = 1
    yearTotal = getYearlyAmount(setsPerDay, increasePerDay)
    yearlyDifference = (yearTotal + (366 * setsPerDay * increasePerDay) - (1 * setsPerDay * increasePerDay)) - yearTotal
    while(yearTotal < worldRecord):
        day += 1
        yearTotal += yearlyDifference
    print(day)

calcStartDate(worldRecord, setsPerDay, increasePerDay)