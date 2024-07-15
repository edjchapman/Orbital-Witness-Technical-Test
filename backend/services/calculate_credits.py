from decimal import Decimal, ROUND_HALF_UP


def base_cost() -> Decimal:
    return Decimal("1.00")


def character_count_cost(char_count: int) -> Decimal:
    return Decimal("0.05") * Decimal(char_count)


def word_length_multipliers(words: list) -> Decimal:
    credits_ = Decimal("0.00")
    for word in words:
        length = len(word)
        if length <= 3:
            credits_ += Decimal("0.1")
        elif length <= 7:
            credits_ += Decimal("0.2")
        else:
            credits_ += Decimal("0.3")
    return credits_


def third_vowels_cost(text: str) -> Decimal:
    vowels = set("aeiouAEIOU")
    credits_ = Decimal("0.00")
    for i, char in enumerate(text):
        if (i + 1) % 3 == 0 and char in vowels:
            credits_ += Decimal("0.3")
    return credits_


def length_penalty(char_count: int) -> Decimal:
    return Decimal("5") if char_count > 100 else Decimal("0.00")


def unique_word_bonus(words: list) -> Decimal:
    unique_words = set(words)
    if len(words) > 1 and len(words) == len(unique_words):
        return Decimal("-2")
    return Decimal("0.00")


def palindrome_check(text: str, credits_: Decimal) -> Decimal:
    cleaned_text = "".join([t for t in text if t.isalnum()]).lower()
    if cleaned_text and cleaned_text == cleaned_text[::-1]:
        credits_ *= Decimal("2")
    return credits_


def calculate_credits(message: str) -> Decimal:
    text = message
    words = text.split()
    char_count = len(text)

    credits_ = Decimal("0.00")
    credits_ += character_count_cost(char_count)
    credits_ += word_length_multipliers(words)
    credits_ += third_vowels_cost(text)
    credits_ += length_penalty(char_count)
    credits_ += unique_word_bonus(words)
    credits_ = palindrome_check(text, credits_)

    return max(base_cost(), credits_.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
