
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

# List of quiz questions. Each question is a dictionary.
questions = [
    {
        "prompt": "Which Indian city is also known as the 'Silicon Valley of India'?",
        "options": ["A. Hyderabad", "B. Mumbai", "C. Chennai", "D. Bangalore"],
        "answer": "D"
    },
    {
        "prompt": "Which is the largest state in India by area?",
        "options": ["A. Maharashtra", "B. Rajasthan", "C. Uttar Pradesh", "D. Madhya Pradesh"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "What is the currency of India?",
        "options": ["A. Dollar", "B. Rupee", "C. Yen", "D. Euro"],
        "answer": "B"
    }
]

# Run the quiz
run_quiz(questions)