#Exercise 8: Simple Search - 30 Marks
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search_term = input("Enter the name to search: ")
if search_term in names:
    print(search_term," was found in the list!")
else:
    print(search_term,"was not found in the list.")