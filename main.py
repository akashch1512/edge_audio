import edge_tts
import asyncio

async def speak():
    communicate = edge_tts.Communicate("Hello Akash : )", "en-US-AriaNeural")
    await communicate.save("output.mp3")

asyncio.run(speak())
