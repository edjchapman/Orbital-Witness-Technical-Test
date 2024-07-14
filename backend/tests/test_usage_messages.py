from typing import List, Dict, Optional

import pytest

from services.usage_messages import format_timestamp, process_messages, sort_usage_data


def test_format_timestamp():
    assert format_timestamp("2024-07-10T12:34:56") == "10-07-2024 12:34"


@pytest.mark.asyncio
async def test_process_messages(mocker):
    message = {
        "id": "1",
        "timestamp": "2024-07-10T12:34:56",
        "text": "Test message",
    }
    mocker.patch("app.get_report", return_value=None)
    result = await process_messages([message])
    assert len(result) == 1
    assert result[0]["message_id"] == "1"
    assert result[0]["timestamp"] == "10-07-2024 12:34"
    assert result[0]["report_name"] == ""
    assert result[0]["credits_used"] > 0


@pytest.mark.parametrize(
    "usage_data, sort_credits_used, sort_report_name, expected_first_item",
    [
        (
            [
                {
                    "timestamp": "10-07-2024 12:34",
                    "report_name": "B",
                    "credits_used": 5,
                },
                {
                    "timestamp": "09-07-2024 12:34",
                    "report_name": "A",
                    "credits_used": 10,
                },
            ],
            "descending",
            "",
            {"timestamp": "09-07-2024 12:34", "report_name": "A", "credits_used": 10},
        ),
        (
            [
                {
                    "timestamp": "10-07-2024 12:34",
                    "report_name": "B",
                    "credits_used": 5,
                },
                {
                    "timestamp": "09-07-2024 12:34",
                    "report_name": "A",
                    "credits_used": 10,
                },
            ],
            "ascending",
            "",
            {"timestamp": "10-07-2024 12:34", "report_name": "B", "credits_used": 5},
        ),
        (
            [
                {
                    "timestamp": "10-07-2024 12:34",
                    "report_name": "B",
                    "credits_used": 5,
                },
                {
                    "timestamp": "09-07-2024 12:34",
                    "report_name": "A",
                    "credits_used": 10,
                },
            ],
            "",
            "descending",
            {"timestamp": "10-07-2024 12:34", "report_name": "B", "credits_used": 5},
        ),
        (
            [
                {
                    "timestamp": "10-07-2024 12:34",
                    "report_name": "B",
                    "credits_used": 5,
                },
                {
                    "timestamp": "09-07-2024 12:34",
                    "report_name": "A",
                    "credits_used": 10,
                },
            ],
            "",
            "ascending",
            {"timestamp": "09-07-2024 12:34", "report_name": "A", "credits_used": 10},
        ),
        (
            [
                {
                    "timestamp": "10-07-2024 12:34",
                    "report_name": "B",
                    "credits_used": 5,
                },
                {
                    "timestamp": "09-07-2024 12:34",
                    "report_name": "A",
                    "credits_used": 10,
                },
            ],
            "ascending",
            "ascending",
            {"timestamp": "10-07-2024 12:34", "report_name": "B", "credits_used": 5},
        ),
        (
            [
                {
                    "timestamp": "10-07-2024 12:34",
                    "report_name": "B",
                    "credits_used": 5,
                },
                {
                    "timestamp": "09-07-2024 12:34",
                    "report_name": "A",
                    "credits_used": 10,
                },
            ],
            "descending",
            "descending",
            {"timestamp": "09-07-2024 12:34", "report_name": "A", "credits_used": 10},
        ),
    ],
    ids=[
        "Sort by credits_used descending",
        "Sort by credits_used ascending",
        "Sort by report_name descending",
        "Sort by report_name ascending",
        "Sort by credits_used ascending and report_name ascending",
        "Sort by credits_used descending and report_name descending",
    ],
)
def test_sort_usage_data(
    usage_data: List[Dict],
    sort_credits_used: Optional[str],
    sort_report_name: Optional[str],
    expected_first_item: Dict,
):
    sorted_data = sort_usage_data(usage_data, sort_credits_used, sort_report_name)
    assert sorted_data[0] == expected_first_item
