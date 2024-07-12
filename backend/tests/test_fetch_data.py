import asyncio
from services.fetch_data import get_messages, get_report


def test_get_messages():
    messages = asyncio.run(get_messages())
    assert "messages" in messages


def test_get_report():
    report = asyncio.run(get_report(report_id="some_valid_report_id"))
    assert report is None or isinstance(report, dict)
