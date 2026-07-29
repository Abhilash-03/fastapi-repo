from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/async-example")
async def async_example():
    # Simulate a long-running I/O-bound operation using asyncio.sleep
    await asyncio.sleep(2)  # Simulating a delay of 2 seconds

    print("Async operation completed!")

    await asyncio.sleep(4)  # Simulating a delay of 4 seconds

    return {
        "message": "Async/Await example completed successfully!",
        "status": "success"
        }
