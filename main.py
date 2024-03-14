
print("Welcome to PyQuiz")

# Get user's readiness to play the Quiz
answer = input("Are you ready to play the Quiz? (yes/no) :")

# Initialize the score and total number of questions
score = 0
total_questions = 4

# Check if the user is ready to play
if answer.lower() == "yes":
    # Question 1
    answer = input("Question 1: What is the capital city of India?")
    if answer.lower() == "delhi":
        score += 1
        print("correct")  # User's answer is correct, increment the score
    else:
        print("Wrong Answer :(")  # User's answer is incorrect

    # Question 2
    answer = input("Question 2: What is the chemical symbol for water? ")
    if answer.lower() == "h2o":
        score += 1
        print("correct")  # User's answer is correct, increment the score
    else:
        print("Wrong Answer :(")  # User's answer is incorrect

    # Question 3
    answer = input(
        "Question 3: Who wrote the play Romeo and Juliet? ")
    if answer.lower() == "william shakespeare":
        score += 1
        print("correct")  # User's answer is correct, increment the score
    else:
        print("Wrong Answer :(")  # User's answer is incorrect

    # Question 4
    answer = input(
        "Question 4: What is the largest mammal in the world? ")
    if answer.lower() == "blue whale":
        score += 1
        print("correct")  # User's answer is correct, increment the score
    else:
        print("Wrong Answer :(")  # User's answer is incorrect


# Display the result and user's score
print(
    "Thank you for Playing this small quiz game, you attempted",
    score,
    "questions correctly!",
)
mark = int((score / total_questions) * 100)
print(f"Marks obtained: {mark}%")

# Farewell message
print("BYE!")
