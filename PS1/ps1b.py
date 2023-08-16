current_savings = 0
roi = 0.04
portion_down_payment = 0.25

input_annual_salary = input("Enter your annual salary:​ ")

if len(input_annual_salary) < 1:
    annual_salary = 120000
else:
    annual_salary = int(input_annual_salary)

input_portion_saved = input("Enter the percent of your salary to save, as a decimal:")

if len(input_portion_saved) < 1:
    portion_saved = 0.05
else:
    portion_saved = float(input_portion_saved)

input_total_cost = input("Enter the cost of your dream home:​ ")

if len(input_total_cost) < 1:
    total_cost = 500000
else: total_cost = int(input_total_cost)

input_semi_annual_raise = input("Enter the semi­annual raise, as a decimal:​ ")

if len(input_semi_annual_raise) < 1:
    semi_annual_raise = 0.03
else:
    semi_annual_raise = float(input_semi_annual_raise)

down_payment = portion_down_payment * total_cost
months = 0


while current_savings < down_payment:
    months += 1
    current_savings += (annual_salary / 12 * portion_saved) + (current_savings * roi / 12)
    #print("Its been",months, "months and you have", current_savings) #debug
    if months % 6 == 0:
        annual_salary =+ (annual_salary * (1 + semi_annual_raise))

print("Number of Months: ", months)

#print(annual_salary, portion_saved, total_cost, annual_salary)