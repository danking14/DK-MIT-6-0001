def savings_rate_bisection(annual_salary):
    # Constants and variables initialization
    total_cost = 1000000
    portion_down_payment = 0.25
    down_payment = total_cost * portion_down_payment
    semi_annual_raise = 0.07
    r = 0.04
    months = 36
    epsilon = 100
    low = 0
    high = 10000
    guess = (low + high) // 2
    num_of_steps = 0

    while low <= high:  # Bisection search loop
        current_savings = 0
        num_of_months = 0

        monthly_salary = annual_salary / 12
        portion_saved = guess / 10000.0

        while num_of_months < months:  # Calculate savings over months
            # Update current savings by adding investment returns and portion of monthly salary saved
            current_savings += current_savings * \
                (r / 12) + portion_saved * monthly_salary
            num_of_months += 1

            if num_of_months % 6 == 0:  # Apply semi-annual raise
                monthly_salary *= (1 + semi_annual_raise)

        # Check if savings are within desired accuracy
        if abs(current_savings - down_payment) <= epsilon:
            return guess / 10000.0, num_of_steps
        elif current_savings < down_payment:  # Adjust search space if savings are too low
            low = guess + 1
        else:  # Adjust search space if savings are too high
            high = guess - 1

        guess = (low + high) // 2  # Update guess for next iteration
        num_of_steps += 1

    return None, num_of_steps


starting_salary = int(input("Enter the starting salary:​ "))
best_savings_rate, steps = savings_rate_bisection(starting_salary)
if best_savings_rate != None:
    print("Best savings rate: ", best_savings_rate)
    print("Steps in bisection search: ", steps)
else:
    print("It is not possible to pay the down payment in three years.")
