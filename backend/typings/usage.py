from typing import Optional, List

from pydantic import BaseModel, Field


class UsageData(BaseModel):
    message_id: float
    timestamp: str
    report_name: Optional[str] = Field(None, description="Name of the report")
    credits_used: float


class Usage(BaseModel):
    usage: List[UsageData]
