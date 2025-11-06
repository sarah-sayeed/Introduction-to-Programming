#Exercise 4: Primitive Quiz - 30 Marks
questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Greece": "Athens",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Switzerland": "Bern"
}
score = 0
for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ")
    if answer.strip().lower() == capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The capital of {country} is {capital}.")
print(f"\nYou got {score} out of {len(questions)} correct.")