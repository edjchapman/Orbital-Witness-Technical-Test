from fastapi import FastAPI
from services.fetch_data import get_messages, get_report

app = FastAPI()


@app.get("/usage")
async def usage():
    messages = await get_messages()
    usage_data = []
    for message in messages:
        report_name = None
        credits_ = 0
        if "report_id" in message:
            report = await get_report(message["report_id"])
            if report:
                report_name = report["name"]
                credits_ = report["credits"]
        usage_data.append(
            {
                "id": 1,  # TODO message["id"],
                "timestamp": 1,  # TODO "timestamp": message["timestamp"]
                "reportName": report_name,
                "creditsUsed": round(credits_, 2),
            }
        )
    return {"usage": usage_data}
