# Simple Emoji Predictor 🚀

def emoji_predictor(text):
    # Define keyword → emoji mapping
    emoji_map = {
        "happy": "😊",
        "sad": "😢",
        "angry": "😡",
        "love": "❤️",
        "surprise": "😲",
        "fear": "😨",
        "laugh": "😂",
        "cool": "😎",
        "sleep": "😴",
        "party": "🥳"
    }

    # Convert text to lowercase for matching
    text = text.lower()

    # Check if any keyword is in the text
    for keyword, emoji in emoji_map.items():
        if keyword in text:
            return f"Predicted Emoji: {emoji}"

    # Default if no keyword matches
    return "🤔 (No emoji found)"

# --- Demo ---
print(emoji_predictor("I am so happy today!"))
print(emoji_predictor("This makes me sad"))
print(emoji_predictor("Let's party tonight"))
print(emoji_predictor("Feeling sleepy now"))
