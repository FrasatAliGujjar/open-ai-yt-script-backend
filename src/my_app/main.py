from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .agent import get_video_summary

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize")
async def summarize(request: Request):
    try:
        data = await request.json()
        url = data.get("url")
        if not url:
            return {"error": "URL is required"}
        return await get_video_summary(url)
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Better for direct run
