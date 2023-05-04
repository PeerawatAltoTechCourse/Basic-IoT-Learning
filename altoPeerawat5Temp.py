TempEachDay = []
for x in range(7):
    k = float(input("Enter your Temperature : \n"))
    TempEachDay.append(k)
print("The Temperature in this week is :")
print(TempEachDay)
sum = 0
count = 0

for number in TempEachDay:
    sum += number
    count += 1 
average = sum/count
print("The Average Temperature of this week is :")
print(average)
maxtemp = max(TempEachDay)
print("The highest Temperature of this week is :")
print(maxtemp)
mintemp = min(TempEachDay)
print("The lowest Temperature of this week is :")
print(mintemp)
