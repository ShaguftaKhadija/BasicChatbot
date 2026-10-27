import random
from datetime import datetime


def buddy_bot():
    print("\n" + "=" * 45)
    print("       BUDDYBOT - YOUR FRIENDLY COMPANION")
    print("=" * 45)
    print("Hello! I'm BuddyBot. Let's have a conversation!")
    print("Type 'help' to see what I can do.")
    print("Type 'bye' to exit.\n")

    name = input("BuddyBot: What's your name? ").strip().title()

    if not name:
        name = "Friend"

    print(f"\nBuddyBot: Nice to meet you, {name}!")
    print("BuddyBot: What's on your mind today?\n")

    jokes = [
        "Why do programmers love Python? Because it makes coding easier!",
        "Why did the computer go to the doctor? It had a virus!",
        "Why do programmers prefer dark mode? Because light attracts bugs!"
    ]

    quotes = [
        "Small steps every day lead to big achievements!",
        "Believe in yourself. Every expert was once a beginner.",
        "Don't stop when you're tired. Stop when you're done!",
        "Your hard work today builds your future tomorrow."
    ]

    while True:
        message = input(f"{name}: ").strip().lower()

        if not message:
            print("BuddyBot: I'm listening! Tell me something.")

        elif message in ["bye", "exit", "quit"]:
            print(f"BuddyBot: Goodbye, {name}! Keep learning and growing!")
            break

        elif any(word in message.split()
                 for word in ["hi", "hello", "hey"]):
            print(f"BuddyBot: Hey {name}! How is your day going?")

        elif "how are you" in message:
            print("BuddyBot: I'm doing great! Thanks for asking.")
            print("BuddyBot: What about you?")

        elif "your name" in message:
            print("BuddyBot: I'm BuddyBot, your Python-powered companion!")

        elif "my name" in message:
            print(f"BuddyBot: You're {name}! Of course I remember.")

        elif any(word in message for word in
                 ["artificial intelligence", " ai ", " ai", "ai "]):
            print("\nBuddyBot: Interested in Artificial Intelligence?")
            print("Here are some beginner-friendly project ideas:")
            print("1. Fake News Awareness Tool")
            print("2. Student Study Planner")
            print("3. Spam Message Detector")
            print("4. AI-Based Plant Disease Identifier")
            print("5. Personal Learning Assistant")
            print("\nBuddyBot: Start with Python basics, then explore")
            print("data handling and suitable AI libraries.")

        elif "project" in message:
            print("\nBuddyBot: Let's find a project you can build!")
            print("1. Expense Tracker")
            print("2. Student Result Analyzer")
            print("3. Quiz Application")
            print("4. Personal Chatbot")
            print("5. File Organizer")
            print("\nBuddyBot: Choose something that solves a real problem.")

        elif "python" in message or "coding" in message:
            print("BuddyBot: Python is a great language to learn!")
            print("Start with variables, conditions, loops, functions,")
            print("lists, dictionaries, and small practical projects.")

        elif "study" in message or "exam" in message:
            print("BuddyBot: Make a small study plan.")
            print("Study one topic, practise questions, and revise it.")
            print("Consistency is more important than cramming!")

        elif "joke" in message:
            print("BuddyBot:", random.choice(jokes))

        elif "motivate" in message or "quote" in message:
            print("BuddyBot:", random.choice(quotes))

        elif "time" in message:
            current_time = datetime.now().strftime("%I:%M %p")
            print(f"BuddyBot: The current time is {current_time}.")

        elif "thank" in message:
            print(f"BuddyBot: You're welcome, {name}!")

        elif "help" in message:
            print("\nBuddyBot understands these topics:")
            print("- Greetings")
            print("- AI and project ideas")
            print("- Python and coding")
            print("- Studying and exams")
            print("- Jokes and motivation")
            print("- Current time")
            print("- Goodbye\n")

        else:
            print("BuddyBot: Interesting question!")
            print("I don't have a predefined answer for that yet.")
            print("Try asking about Python, AI, projects, or studying.")


if __name__ == "__main__":
    buddy_bot()