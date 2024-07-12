import pytest
from typing import Dict
from services.calculate_credits import calculate_credits


@pytest.mark.parametrize(
    "message, expected_credits",
    [
        ({"message": "Hello world"}, 1.0),
        ({"message": "a ab abc abcd abcde abcdef abcdefg abcdefgh"}, 4.05),
        ({"message": "aei oei aei"}, 2.75),
        ({"message": "a" * 101}, 38.500000000000036),
        ({"message": "unique words all different"}, 2.3),
        ({"message": "A man a plan a canal Panama"}, 7.300000000000002),
        ({"message": ""}, 1.0),
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
def test_calculate_credits(message: Dict[str, str], expected_credits: float):
    assert calculate_credits(message) == expected_credits
