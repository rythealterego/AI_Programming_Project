# AI Course Assistant Chatbot
# Author: RYAN GAKINYA - 250676DAI
# Unit: DAI011 Programming for AI - CAT2

def get_response(user_input: str) -> str:
    """
    Simple rule-based chatbot for course assistance.
    It looks for keywords in the user's input and returns responses.
    """

    # Normalize input
    text = user_input.lower().strip()
    words = text.split()  # helps avoid matching "hi" inside "this"

    # Intent 1: Greeting (match whole words only)
    if any(w in ["hi", "hello", "hey"] for w in words):
        return "Hello! 😊 I'm your AI course assistant bot. How can I help you today?"

    # Intent 2: Asking about the course/unit
    if "course" in text or "unit" in text:
        return ("This CAT is for the unit 'Programming for AI (DAI011)'. "
                "You will mainly use Python and basic AI concepts like rule-based systems.")

    # Intent 3: Asking about deadlines / submission
    if any(word in text for word in ["deadline", "due", "submit", "submission"]):
        return ("Please confirm the exact deadline on your course outline or Teams. "
                "Usually, you must submit both the GitHub link and the PDF report before the deadline.")

    # Intent 4: Asking about GitHub / repository
    if any(word in text for word in ["github", "repository", "repo"]):
        return ("Your GitHub repository should be named 'AI_Programming_Project'. "
                "Make sure it is public and has a clear README with your details and how to run the code.")

    # Intent 5: Asking for help / feeling stuck
    if any(word in text for word in ["help", "stuck", "confused", "don't understand", "do not understand"]):
        return ("It's okay to feel stuck. Try breaking the task into small steps and ask specific questions. "
                "You can also review lecture notes or ask your lecturer/TA for clarification.")

    # Intent 6: Asking about marks or grading
    if any(word in text for word in ["marks", "grade", "grading"]):
        return ("The CAT is marked out of 40, with 8 marks for GitHub, "
                "20 marks for the Python project, and 12 marks for documentation and reflection.")

    # Intent 7: Goodbye
    if any(word in text for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! 👋 All the best with your CAT!"

    # Fallback intent
    return ("Hmm, I'm not sure about that yet 🤔. "
            "Try asking about the course, GitHub, deadlines, or help with the assignment.")


def main():
    """Main loop for the chatbot."""
    print("=== AI Course Assistant Chatbot ===")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.strip().lower() in ["bye", "goodbye", "exit", "quit"]:
            print("Bot: Goodbye! 👋 All the best with your CAT.")
            break

        response = get_response(user_input)
        print("Bot:", response)


if __name__ == "__main__":
    main()
