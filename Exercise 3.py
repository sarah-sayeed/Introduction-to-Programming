#Exercise 3: Biography - 25 Marks
name = input("Enter your Name: ")
hometown = input("Enter your Hometown: ")
age = int(input("Enter your Age: "))
print("\nBiography")
dict = {'Name':name,'Hometown':hometown,'Age':age}
for i in dict:
    print(i,':',dict[i])