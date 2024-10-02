#Student Name: Hannes Meyer-Rahlfs  
#Program Title: Metric ton converter

#input stage
tons = int(input("Enter the number of tons:"))
stone = int(input("Enter the number of stone:"))
pounds = int(input("Enter the number of pounds:"))
ounces = int(input("Enter the number of ounces:"))

# Convert everything to ounces using the formula
total_Ounces = 35840 * tons + 224 * stone + 16 * pounds + ounces

# Divide the total ounces by 35.274 to get the weight in kilograms
total_Kilos = total_Ounces / 35.274

# Calculate the number of metric tons
metric_Tons = int(total_Kilos//1000)

# Subtract the metric tons portion to get the remaining kilograms
remaining_Kilos = int(total_Kilos % 1000)

# Multiply the remaining kilograms by 1000 to convert to grams
grams = (total_Kilos - int(total_Kilos)) * 1000

# Print the weight in metric tons, kilograms, and grams (with grams rounded to one decimal place).
print(f"The metric weight is {metric_Tons} metric tons, {int(remaining_Kilos)} kilos, and {grams:.1f} grams.")

# Ready to mark