from datetime import datetime
from typing import Optional, List, Dict

from services.calculate_credits import calculate_credits
from services.fetch_data import get_report


def format_timestamp(timestamp: str) -> str:
    return datetime.fromisoformat(timestamp).strftime("%d-%m-%Y %H:%M")


async def process_messages(messages: List[Dict]) -> List[Dict]:
    processed_messages = []
    for message in messages:
        report_name = ""
        credits_ = None
        if "report_id" in message:
            report = await get_report(message["report_id"])
            if report:
                report_name = report["name"]
                credits_ = report["credit_cost"]
        processed_messages.append(
            {
                "message_id": message["id"],
                "timestamp": format_timestamp(message["timestamp"]),
                "report_name": report_name,
                "credits_used": credits_ or calculate_credits(message.get("text", "")),
            }
        )
    return processed_messages


def sort_by(usage_data: List[Dict], sort_key: str, descending: bool) -> List[Dict]:
    return sorted(usage_data, key=lambda x: x[sort_key], reverse=descending)


def sort_usage_data(
    usage_data: List[Dict],
    sort_credits_used: Optional[str] = "",
    sort_report_name: Optional[str] = "",
):
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
