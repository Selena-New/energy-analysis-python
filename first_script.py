# My first energy Python script
# Saghi Tayebeh Khabbaz - Month 1

temperatures = [15, 18, 22, 19, 25, 30, 28]
average = sum(temperatures) / len(temperatures)

print("Daily temperatures:", temperatures)
print("Average temperature:", round(average, 2), "degrees")
print("Max temperature:", max(temperatures), "degrees")
print("Min temperature:", min(temperatures), "degrees")
print("")
print("Ready to analyse energy data!") 