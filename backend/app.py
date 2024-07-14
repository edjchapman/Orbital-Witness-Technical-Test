from datetime import datetime
from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from services.fetch_data import get_messages, get_report
from services.calculate_credits import calculate_credits
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/usage")
async def get_usage(
    sort_credits_used: Optional[str] = Query(None),
    sort_report_name: Optional[str] = Query(None),
):
    try:
        messages = await get_messages()
        usage_data = []

        for message in messages.get("messages"):
            credits_ = calculate_credits(message.get("text", ""))
            report_name = ""
            if "report_id" in message:
                report = await get_report(message["report_id"])
                if report:
                    report_name = report["name"]
                    credits_ = report["credit_cost"]

            formatted_timestamp = datetime.fromisoformat(message["timestamp"]).strftime(
                "%d-%m-%Y %H:%M"
            )
            usage_data.append(
                {
                    "message_id": message["id"],
                    "timestamp": formatted_timestamp,
                    "report_name": report_name,
                    "credits_used": credits_,
                }
            )

        if sort_report_name:
            usage_data.sort(
                key=lambda x: x["report_name"],
                reverse=(sort_report_name == "descending"),
            )

        if sort_credits_used:
            usage_data.sort(
                key=lambda x: x["credits_used"],
                reverse=(sort_credits_used == "descending"),
            )

        return {"usage": usage_data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
