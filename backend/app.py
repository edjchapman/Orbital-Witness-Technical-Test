from typing import Optional
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from services.fetch_data import get_messages
from services.usage_messages import process_messages, sort_usage_data
from typings.usage import Usage

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/api/usage",
    response_model=Usage,
    summary="Retrieve usage data",
    description="Fetches usage data and supports optional sorting by credits used and report name.",
)
async def get_usage(
    sort_credits_used: Optional[str] = Query(
        None,
        title="Sort by Credits Used",
        description="Optionally sort by 'ascending' or 'descending'.",
        example="ascending",
    ),
    sort_report_name: Optional[str] = Query(
        None,
        title="Sort by Report Name",
        description="Optionally sort by 'ascending' or 'descending'.",
        example="descending",
    ),
) -> Usage:
    """
    Retrieve usage data with optional sorting.
    """
    try:
        messages = await get_messages()
        usage_data = await process_messages(messages=messages.get("messages", []))
        sorted_usage_data = sort_usage_data(
            usage_data=usage_data,
            sort_report_name=sort_report_name,
            sort_credits_used=sort_credits_used,
        )

        return Usage(usage=sorted_usage_data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
