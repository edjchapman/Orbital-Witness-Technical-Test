from fastapi import FastAPI, HTTPException
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


@app.get("/usage")
async def usage():
    try:
        messages = await get_messages()
        usage_data = []

        for message in messages.get("messages"):
            credits_ = calculate_credits(message.get("message", ""))
            report_name = ""
            if "report_id" in message:
                report = await get_report(message["report_id"])
                if report:
                    report_name = report["name"]
                    credits_ = report["credit_cost"]

            usage_data.append(
                {
                    "id": message["id"],
                    "timestamp": message["timestamp"],
                    "reportName": report_name,
                    "creditsUsed": round(credits_, 2),
                }
            )

        return {"usage": usage_data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
