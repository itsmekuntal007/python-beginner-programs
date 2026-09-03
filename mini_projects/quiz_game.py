score = 0

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used to create web pages?",
        "options": ["A. Python", "B. C", "C. HTML", "D. Java"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. <!-- -->", "D. /* */"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Computer Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    }
]

print("🎮 Welcome to the Python Quiz Game!")
print("-" * 40)

for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == question["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
        print("Correct answer:", question["answer"])

print("\n" + "-" * 40)
print("🏆 Quiz Completed!")
print("Your score:", score, "/", len(questions))

if score == len(questions):
    print("🌟 Excellent! Perfect score!")
elif score >= 3:
    print("👏 Good job!")
else:
    print("📚 Keep practicing!")