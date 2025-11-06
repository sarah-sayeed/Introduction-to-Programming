#Exercise 5: Days of the Month - 30 Marks
days_in_month = {
    1: 31,
    2: 28,  
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
month = int(input("Enter the month number (1-12): "))
if month < 1 or month > 12:
    print("Invalid month number. Please enter a number between 1 and 12.")
else:
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").strip().lower()
        if leap == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        print(f"Month {month} has {days_in_month[month]} days.")