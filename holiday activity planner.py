# Holiday Activity Planner

# 1. Ask for the first choice (Holiday Type)
holiday_type = input("Choose a holiday type (beach/mountain): ")


if holiday_type == "beach":
    weather = input("Is it sunny or rainy? ")
    
    if weather == "sunny":
        print("Your plan: Go swimming and build sandcastles!")
    else:
        print("Your plan: Relax at a beach cafe and listen to the rain.")

elif holiday_type == "mountain":
    season = input("Is it summer or winter? ")
    
    if season == "summer":
        print("Your plan: Go hiking and look for wildlife!")
    else:
        print("Your plan: Go skiing or snowboarding down the slopes!")

else:
    print("Invalid holiday type chosen. Please run the program again.")