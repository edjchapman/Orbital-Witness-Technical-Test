from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from services.fetch_data import get_messages
from services.usage_messages import process_messages, sort_usage_data

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
        usage_data = await process_messages(messages=messages.get("messages", []))
        usage_data = sort_usage_data(
            usage_data=usage_data,
            sort_report_name=sort_report_name,
            sort_credits_used=sort_credits_used,
        )

        return {"usage": usage_data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
