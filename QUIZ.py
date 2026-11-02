
print("     PYTHON QUIZ APPLICATION")

name = input("Enter your name: ")

print("\nChoose your difficulty level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("Enter your choice (1/2/3): ")

# Easy questions
easy_questions = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "How many players are there in a cricket team on the field?",
        "options": ["A. 9", "B. 10", "C. 11", "D. 12"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Beijing", "B. Seoul", "C. Bangkok", "D. Tokyo"],
        "answer": "D"
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
        "answer": "C"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "B"
    }
]

# Medium questions
medium_questions = [
    {
        "question": "Which country won the ICC Men's Cricket World Cup in 2023?",
        "options": ["A. India", "B. England", "C. Australia", "D. New Zealand"],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol for silver?",
        "options": ["A. Si", "B. Ag", "C. Au", "D. Fe"],
        "answer": "B"
    },
    {
        "question": "Which is the smallest bone in the human body?",
        "options": ["A. Stapes", "B. Femur", "C. Tibia", "D. Radius"],
        "answer": "A"
    },
    {
        "question": "Who wrote the Indian national anthem?",
        "options": ["A. Bankim Chandra Chattopadhyay",
                    "B. Sarojini Naidu",
                    "C. Rabindranath Tagore",
                    "D. Subhas Chandra Bose"],
        "answer": "C"
    },
    {
        "question": "What is the square root of 2025?",
        "options": ["A. 35", "B. 40", "C. 45", "D. 55"],
        "answer": "C"
    }
]

# Hard questions
hard_questions = [
    {
        "question": "Which Indian won the first individual Olympic gold medal for India?",
        "options": ["A. Neeraj Chopra",
                    "B. Abhinav Bindra",
                    "C. Rajyavardhan Singh Rathore",
                    "D. Leander Paes"],
        "answer": "B"
    },
    {
        "question": "Which scientist formulated the uncertainty principle?",
        "options": ["A. Niels Bohr",
                    "B. Erwin Schrödinger",
                    "C. Werner Heisenberg",
                    "D. Max Planck"],
        "answer": "C"
    },
    {
        "question": "Which strait separates Asia and North America?",
        "options": ["A. Strait of Malacca",
                    "B. Bering Strait",
                    "C. Strait of Gibraltar",
                    "D. Bosporus Strait"],
        "answer": "B"
    },
    {
        "question": "Which Indian mathematician is famous for his work on number theory and partitions?",
        "options": ["A. C. V. Raman",
                    "B. Homi J. Bhabha",
                    "C. Srinivasa Ramanujan",
                    "D. S. N. Bose"],
        "answer": "C"
    },
    {
        "question": "In which year was the Battle of Plassey fought?",
        "options": ["A. 1757", "B. 1764", "C. 1857", "D. 1773"],
        "answer": "A"
    }
]
# Select questions based on difficulty
if choice == "1":
    questions = easy_questions
    print("\nYou selected EASY level!")

elif choice == "2":
    questions = medium_questions
    print("\nYou selected MEDIUM level!")

elif choice == "3":
    questions = hard_questions
    print("\nYou selected HARD level!")

else:
    questions = []
    print("Invalid choice! Please run the program again.")

# Start quiz
if len(questions) > 0:
    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}. {q['question']}")

        for option in q["options"]:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        while user_answer not in ["A", "B", "C", "D"]:
            user_answer = input(
                "Invalid answer! Enter A, B, C, or D: "
            ).strip().upper()

        if user_answer == q["answer"]:
            print("Correct answer!")
            score += 1
        else:
            print("Incorrect!")
            print("Correct answer:", q["answer"])

    # Display final result
    percentage = (score / len(questions)) * 100

    print("\n================================")
    print("         QUIZ COMPLETED!")
    print("================================")
    print("Player:", name)
    print("Difficulty:", choice)
    print("Final score:", score, "/", len(questions))
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Excellent performance!")
    elif percentage >= 60:
        print("Good job!")
    elif percentage >= 40:
        print("You can improve!")
    else:
        print("Keep practising!")

    