from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Load pre-trained BART summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Create Pydantic model for request body
class TextRequest(BaseModel):
    text: str
    summary_length: int = 50

# Define endpoint for text summarization
@app.post("/ai_summarizer/")
async def summarize_text(request: TextRequest):
    try:
        # Summarize the text
        summary = summarizer(request.text, max_length=request.summary_length, min_length=30, do_sample=False)
        return {"summary": summary[0]["summary_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
