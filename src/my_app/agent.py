from openai import OpenAI
from .utils import get_title_and_description
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def get_video_summary(url: str):
    title, description = get_title_and_description(url)

    prompt = f"""
    This is a YouTube video.
    Title: {title}
    Description: {description}
    
    Based on the title and description, what is this video about? 
    Generate a short script or detailed explanation assuming the content.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a YouTube video explainer."},
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "title": title,
        "description": description,
        "summary": response.choices[0].message.content
    }
