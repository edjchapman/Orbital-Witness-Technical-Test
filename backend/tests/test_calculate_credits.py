from decimal import Decimal
from services.calculate_credits import (
    calculate_credits,
    character_count_cost,
    word_length_multipliers,
    third_vowels_cost,
    length_penalty,
    unique_word_bonus,
    palindrome_check,
)


def test_the_base_cost():
    assert calculate_credits("x") == Decimal(
        "1.00"
    ), "Every message should have a base cost of 1 credit"


def test_character_count():
    assert character_count_cost(3) == Decimal(
        "0.15"
    ), "Should add 0.05 credits for each character in the message."


def test_word_length_multipliers():
    assert word_length_multipliers("a aa aaa aaaa aaaaaa aaaaaaaa".split()) == Decimal(
        "1.00"
    ), "Should add credits based on word length."


def test_third_vowels():
    assert third_vowels_cost("aeioaeio") == Decimal(
        "0.60"
    ), "Should add 0.3 credits for each third vowel."


def test_length_penalty():
    assert length_penalty(101) == Decimal(
        "5.00"
    ), "Should add a penalty of 5 credits if the message length exceeds 100 characters."


def test_unique_word_bonus():
    assert unique_word_bonus("unique words all different".split()) == Decimal(
        "-2.00"
    ), "Should subtract 2 credits if all words are unique."


def test_palindromic_message_doubles_the_total_cost():
    palindromic_credits = palindrome_check(
        "A man a plan a canal Panama", Decimal("5.00")
    )
    non_palindromic_credits = palindrome_check(
        "B man a plan a canal Panama", Decimal("5.00")
    )
    assert (
        palindromic_credits == non_palindromic_credits * 2
    ), "A palindromic message should be exactly double the credits."


def test_calculate_credits():
    assert calculate_credits("") == Decimal(
        "1.00"
    ), "Every message should have a base cost of 1 credit"
    assert calculate_credits("b b d") == Decimal(
        "1.00"
    ), "Should add 0.05 credits for each character in the message."
    assert calculate_credits("a aa aaa aaaa aaaaaa aaaaaaaa") == Decimal(
        "5.10"
    ), "Should add credits based on word length."
    assert calculate_credits("aeioaeio") == Decimal(
        "1.30"
    ), "Should add 0.3 credits for each third vowel."
    assert calculate_credits("a" * 101) == Decimal(
        "40.50"
    ), "Should add a penalty of 5 credits if the message length exceeds 100 characters."
    assert calculate_credits("unique words all different") == Decimal(
        "1.30"
    ), "Should subtract 2 credits if all words are unique."
    palindromic_credits = calculate_credits("A man a plan a canal Panama")
    non_palindromic_credits = calculate_credits("B man a plan a canal Panama")
    assert (
        palindromic_credits == non_palindromic_credits * 2
    ), "A palindromic message should be exactly double the credits."
