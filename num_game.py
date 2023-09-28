#Number game
print("welcome to brain picking game")
#Define Categories and questions in a Dictonary
categories = {
    "Technology": [
        {"question": "what does CPU stand for?", "answer": "central processing unit"},
        {"question": "What does GPU stand for?", "answer": "graphics processing unit"},      
    ],
"History":[
    {"question": "Who was the first president of the United States?","answer":"geroge washington" },
    {"question": "In whoch year did World Was II end?", "answer":"1945"},
]

}
#Function to play the quiz for a specfic category
def play_quiz(category):
    print(f"category: {category}")
    score = 0

    for question_data in categories[category]:
        question = question_data["question"]
        correct_answer = question_data["answer"]

        answer = input(question + " ")
        if answer.lower() == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print (f"you got {score}/{len(categories[category])} questions correct in the {category} category.")
# Ask the user to select a category
while True:
    print("choose a category:")
    for category in categories:
        print(category)

    selected_category = input("Enter the category you want to play (or 'quit' to exit): ")

    if selected_category.lower() == 'quit':
        break

    if selected_category in categories:
        play_quiz(selected_category)
    else:
        print("Invalid category. Please choose from the avaiable categories.")




