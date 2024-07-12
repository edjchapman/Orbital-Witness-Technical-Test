import aiohttp


async def get_messages():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://owpublic.blob.core.windows.net/tech-task/messages/current-period"
        ) as response:
            return await response.json()


async def get_report(report_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://owpublic.blob.core.windows.net/tech-task/reports/{report_id}"
        ) as response:
            if response.status == 200:
                return await response.json()
            return None
