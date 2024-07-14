from datetime import datetime
from typing import List, Dict, Optional

from services.calculate_credits import calculate_credits
from services.fetch_data import get_report
from typings.usage import UsageData


def format_timestamp(timestamp: str) -> str:
    return datetime.fromisoformat(timestamp).strftime("%d-%m-%Y %H:%M")


async def process_messages(messages: List[Dict]) -> List[UsageData]:
    processed_messages = []
    for message in messages:
        credits_used = calculate_credits(message.get("text", ""))
        report_name = ""
        if "report_id" in message:
            report = await get_report(message["report_id"])
            if report:
                report_name = report["name"]
                credits_used = report["credit_cost"]

        processed_messages.append(
            UsageData(
                message_id=message["id"],
                timestamp=format_timestamp(message["timestamp"]),
                report_name=report_name,
                credits_used=credits_used,
            )
        )
    return processed_messages


def sort_by(
    usage_data: List[UsageData], sort_key: str, descending: bool
) -> List[UsageData]:
    return sorted(usage_data, key=lambda x: getattr(x, sort_key), reverse=descending)


def sort_usage_data(
    usage_data: List[UsageData],
    sort_credits_used: Optional[str] = "",
    sort_report_name: Optional[str] = "",
) -> List[UsageData]:
    if sort_report_name:
        usage_data = sort_by(
            usage_data=usage_data,
            sort_key="report_name",
            descending=sort_report_name == "descending",
        )

    if sort_credits_used:
        usage_data = sort_by(
            usage_data=usage_data,
            sort_key="credits_used",
            descending=sort_credits_used == "descending",
        )
    return usage_data
