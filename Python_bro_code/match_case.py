# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            print("It is Sunday") # or can return "It is Sunday" and then => print(day_of_weeek(day))
        case 2:
            print("It is Monday")
        case 3:
            print("It is Tuesday")
        case 4:
            print("It is Wednesday")
        case 5:
            print("It is Thursday")
        case 6:
            print("It is Friday")
        case 7:
            print("It is Saturday")
        # Can be considered as 'else' in if-elif-else or default in switch-case
        case _: 
            print("Invalid day")

day = int(input("Enter a number to get the day of the week: "))
day_of_week(day)

print("----------------------------------------------------------------------------")

# If multiple conditions have the same output, they can be grouped together using '|' as we use in other languages

def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False
        
print(is_weekend("Monday"))