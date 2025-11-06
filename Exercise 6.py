#Exercise 6: Brute Force Attack - 30 Marks
for i in range(5):
    if input("Enter password: ") == "12345":
        print("Access granted.")
        break
    print("Incorrect. Attempts remaining:", 4 - i)
else:
    print("Maximum attempts reached. Authorities have been alerted.")