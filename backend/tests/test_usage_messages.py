from typing import List, Optional

import pytest
from pydantic import TypeAdapter
from services.usage_messages import process_messages, sort_usage_data, format_timestamp
from typings.usage import UsageData


def test_format_timestamp():
    assert format_timestamp("2024-07-10T12:34:56") == "10-07-2024 12:34"


@pytest.mark.asyncio
async def test_process_messages(monkeypatch):
    message = {
        "id": "1",
        "timestamp": "2024-07-10T12:34:56",
        "text": "Test message",
    }

    async def mock_get_report(report_id):
        return None

    monkeypatch.setattr("services.fetch_data.get_report", mock_get_report)

    result = await process_messages([message])
    assert len(result) == 1
    assert result[0].message_id == 1
    assert result[0].timestamp == "10-07-2024 12:34"
    assert result[0].report_name == ""
    assert result[0].credits_used > 0


@pytest.mark.parametrize(
    "usage, sort_credits_used, sort_report_name, expected_first_item",
    [
        (
            [
                {
                    "message_id": 1,
                    "timestamp": "10-07-2024 12:34",
                    "report_name": "B",
                    "credits_used": 5,
                },
                {
                    "message_id": 2,
                    "timestamp": "09-07-2024 12:34",
                    "report_name": "A",
                    "credits_used": 10,
                },
            ],
            "descending",
            "",
            {
                "message_id": 2,
                "timestamp": "09-07-2024 12:34",
                "report_name": "A",
                "credits_used": 10,
            },
        ),
        (
            [
                {
                    "message_id": 1,
                    "timestamp": "10-07-2024 12:34",
                    "report_name": "B",
                    "credits_used": 5,
                },
                {
                    "message_id": 2,
                    "timestamp": "09-07-2024 12:34",
                    "report_name": "A",
                    "credits_used": 10,
                },
            ],
            "ascending",
            "",
            {
                "message_id": 1,
                "timestamp": "10-07-2024 12:34",
                "report_name": "B",
                "credits_used": 5,
            },
        ),
        (
            [
                {
                    "message_id": 1,
                    "timestamp": "10-07-2024 12:34",
                    "report_name": "B",
                    "credits_used": 5,
                },
                {
                    "message_id": 2,
                    "timestamp": "09-07-2024 12:34",
                    "report_name": "A",
                    "credits_used": 10,
                },
            ],
            "",
            "descending",
            {
                "message_id": 1,
                "timestamp": "10-07-2024 12:34",
                "report_name": "B",
                "credits_used": 5,
            },
        ),
        (
            [
                {
                    "message_id": 1,
                    "timestamp": "10-07-2024 12:34",
                    "report_name": "B",
                    "credits_used": 5,
                },
                {
                    "message_id": 2,
                    "timestamp": "09-07-2024 12:34",
                    "report_name": "A",
                    "credits_used": 10,
                },
            ],
            "",
            "ascending",
            {
                "message_id": 2,
                "timestamp": "09-07-2024 12:34",
                "report_name": "A",
                "credits_used": 10,
            },
        ),
        (
            [
                {
                    "message_id": 1,
                    "timestamp": "10-07-2024 12:34",
                    "report_name": "B",
                    "credits_used": 5,
                },
                {
                    "message_id": 2,
                    "timestamp": "09-07-2024 12:34",
                    "report_name": "A",
                    "credits_used": 10,
                },
            ],
            "ascending",
            "ascending",
            {
                "message_id": 1,
                "timestamp": "10-07-2024 12:34",
                "report_name": "B",
                "credits_used": 5,
            },
        ),
        (
            [
                {
                    "message_id": 1,
                    "timestamp": "10-07-2024 12:34",
                    "report_name": "B",
                    "credits_used": 5,
                },
                {
                    "message_id": 2,
                    "timestamp": "09-07-2024 12:34",
                    "report_name": "A",
                    "credits_used": 10,
                },
            ],
            "descending",
            "descending",
            {
                "message_id": 2,
                "timestamp": "09-07-2024 12:34",
                "report_name": "A",
                "credits_used": 10,
            },
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
    usage: List[dict],
    sort_credits_used: Optional[str],
    sort_report_name: Optional[str],
    expected_first_item: dict,
):
    type_adapter = TypeAdapter(List[UsageData])
    usage_data = type_adapter.validate_python(usage)
    sorted_data = sort_usage_data(usage_data, sort_credits_used, sort_report_name)
    assert sorted_data[0].model_dump() == expected_first_item
