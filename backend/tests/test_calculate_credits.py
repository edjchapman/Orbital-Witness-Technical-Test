from decimal import Decimal

import pytest
from services.calculate_credits import calculate_credits


@pytest.mark.parametrize(
    "message, expected_credits",
    [
        ("Hello world", Decimal("1.00")),
        ("a ab abc abcd abcde abcdef abcdefg abcdefgh", Decimal("4.05")),
        ("aei oei aei", Decimal("2.75")),
        ("a" * 101, Decimal("38.50")),
        ("unique words all different", Decimal("2.30")),
        ("A man a plan a canal Panama", Decimal("7.30")),
        ("", Decimal("1.00")),
    ],
    ids=[
        "Simple message",
        "Words of varying lengths",
        "Multiple third vowels",
        "Long message (101 chars)",
        "All unique words",
        "Palindromic message",
        "Empty message",
    ],
)
def test_calculate_credits(message: str, expected_credits: Decimal):
    assert calculate_credits(message) == expected_credits
