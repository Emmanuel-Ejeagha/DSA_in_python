# Calculate Average Temperature

# Solution 1: without list
numDays = int(input("How many day's temperature? "))
total = 0
for day in range(1, numDays+1):
    nextDay = int(input("Day " + str(day) + "'s high temp: "))
    total += nextDay

avg = round(total/numDays,2)
print(f"\nAverage = {avg}")


# Solution 2: with list
numDays = int(input("How many day's temperature? "))
total = 0
temp = []

for day in range(numDays):
    nextDay = int(input("Day " + str(day+1) + "'s high temp:"))
    temp.append(nextDay)
    total += temp[day]

average = avg = round(total/numDays,2)
print("\nAverage = " + str(avg))

above = 0
for i in temp:
    if i > avg:
        above += 1

print(f"{above} day(s) above average")