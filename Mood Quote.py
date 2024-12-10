# Mood-Quote-generator
def get_quote(mood):
    # Define some quotes for different moods
    mood_quotes = {
        "happy": "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
        "sad": "Tears are words that need to be written. - Paulo Coelho",
        "angry": "Holding onto anger is like drinking poison and expecting the other person to die. - Buddha",
        "excited": "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "relaxed": "Sometimes the most productive thing you can do is relax. - Mark Black",
        "motivated": "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "grateful": "Gratitude is not only the greatest of virtues, but the parent of all the others. - Marcus Tullius Cicero",
        "confused": "It's okay to be unsure, just keep moving forward. - Unknown",
    }

    # Return the corresponding quote based on the mood
    return mood_quotes.get(mood.lower(), "Sorry, I don't have a quote for that mood.")

def main():
    # Greet the user and ask for their mood
    print("Hello! How are you feeling today?")
    user_mood = input("Enter your mood (happy, sad, angry, excited, relaxed, motivated, grateful, confused): ").strip()

    # Get and display the quote or greeting based on the user's mood
    quote = get_quote(user_mood)
    print("\nHere is a quote for you: ")
    print(quote)

if __name__ == "__main__":
    main()
