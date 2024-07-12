from typing import Dict


def calculate_credits(message: Dict[str, str]) -> float:
    """
    Calculate the number of credits_ consumed by a message.

    Args:
        message (Dict[str, str]): A dictionary containing the message text.

    Returns:
        int: The total number of credits_ consumed by the message.
    """
    # Get the message text
    text = message.get("message", "")
    words = text.split()
    char_count = len(text)
    unique_words = set(words)
    vowels = set("aeiouAEIOU")

    # Base cost and character count
    credits_ = 1 + 0.05 * char_count

    # Word length multipliers
    for word in words:
        length = len(word)
        if length <= 3:
            credits_ += 0.1
        elif length <= 7:
            credits_ += 0.2
        else:
            credits_ += 0.3

    # Third vowels
    for i, char in enumerate(text):
        if (i + 1) % 3 == 0 and char in vowels:
            credits_ += 0.3

    # Length penalty
    if char_count > 100:
        credits_ += 5

    # Unique word bonus
    if len(words) == len(unique_words):
        credits_ -= 2

    # Palindrome check
    cleaned_text = "".join([t for t in text if t.isalnum()]).lower()
    if cleaned_text == cleaned_text[::-1]:
        credits_ *= 2

    # Ensure minimum cost is 1 credit
    return max(1.0, credits_)
