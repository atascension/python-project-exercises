weekend_days = ("Saturday", "Sunday")

weekend_plans = ["Visit the farmers market", "Watch a movie", "Go for a walk"]

print("Weekend Planner")

print("---------------------------")

print(f"Days: {weekend_days[0]} and {weekend_days[1]} ")

print(f"Current weekend plans: {weekend_plans}")

user_option = input("Do you have any other weekend plans? Type one here: ")

weekend_plans.append(user_option)

print(f"Updated weekend plans: {weekend_plans} ")