from decimal import Decimal, ROUND_HALF_UP


def calculate_credits(message: str) -> Decimal:
    """
    Calculate the number of credits_ consumed by a message.

    Args:
        message (str): The message text.

    Returns:
        Decimal: The total number of credits_ consumed by the message.
    """
    # Get the message text
    text = message
    words = text.split()
    char_count = len(text)
    unique_words = set(words)
    vowels = set("aeiouAEIOU")

    # Base cost and character count
    credits_ = Decimal("1") + Decimal("0.05") * Decimal(char_count)

    # Word length multipliers
    for word in words:
        length = len(word)
        if length <= 3:
            credits_ += Decimal("0.1")
        elif length <= 7:
            credits_ += Decimal("0.2")
        else:
            credits_ += Decimal("0.3")

    # Third vowels
    for i, char in enumerate(text):
        if (i + 1) % 3 == 0 and char in vowels:
            credits_ += Decimal("0.3")

    # Length penalty
    if char_count > 100:
        credits_ += Decimal("5")

    # Unique word bonus
    if len(words) > 1 and len(words) == len(unique_words):
        credits_ -= Decimal("2")

    # Palindrome check
    cleaned_text = "".join([t for t in text if t.isalnum()]).lower()
    if cleaned_text and cleaned_text == cleaned_text[::-1]:
        credits_ *= Decimal("2")

    # Ensure minimum cost is 1 credit
    return max(
        Decimal("1.00"), credits_.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    )
