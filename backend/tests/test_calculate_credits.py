from decimal import Decimal

from services.calculate_credits import calculate_credits


def test_the_base_cost():
    assert calculate_credits("") == Decimal(
        "1.00"
    ), "Every message should have a base cost of 1 credit"


def test_character_count():
    assert calculate_credits("b b d") == Decimal(
        "1.55"
    ), "Should add 0.05 credits for each character in the message."


def test_word_length_multipliers():
    assert calculate_credits("a aa aaa aaaa aaaaaa aaaaaaaa") == Decimal(
        "7.10"
    ), "Should add credits based on word length."


def test_third_vowels():
    assert calculate_credits("aeioaeio") == Decimal(
        "2.30"
    ), "Should add 0.3 credits for each third vowel."


def test_length_penalty():
    assert calculate_credits("a" * 101) == Decimal(
        "42.50"
    ), "Should add a penalty of 5 credits if the message length exceeds 100 characters."


def test_unique_word_bonus():
    assert calculate_credits("unique words all different") == Decimal(
        "2.30"
    ), "Should subtract 2 credits if all words are unique."


def test_palindromic_message_doubles_the_total_cost():
    palindromic_credits = calculate_credits("A man a plan a canal Panama")
    non_palindromic_credits = calculate_credits("B man a plan a canal Panama")
    assert (
        palindromic_credits == non_palindromic_credits * 2
    ), "A palindromic message should be exactly double the credits."
