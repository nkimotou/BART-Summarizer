from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

# Pydantic model for text input
class TextInput(BaseModel):
    text: str = Field(..., title="Text", description="Input text to process")

# Pydantic model for summarization request
class SummarizeRequest(BaseModel):
    text: str = Field(..., title="Text", description="Input text to summarize")
    summary_length: Optional[int] = Field(50, ge=1, le=100, title="Summary Length", description="Length of the summary")

# Pydantic model for compression request
class CompressionRequest(BaseModel):
    text: str = Field(..., title="Text", description="Input text to compress")
    summary_length: Optional[int] = Field(50, ge=1, le=100, title="Summary Length", description="Length of the summary")

# Dependency to validate input text
def validate_input_text(text_input: TextInput):
    if not text_input.text.strip():
        raise HTTPException(status_code=422, detail="Input text cannot be empty")
    return text_input.text

# Dependency to validate summarization request
def validate_summarize_request(request: SummarizeRequest):
    if not request.text.strip():
        raise HTTPException(status_code=422, detail="Input text cannot be empty")
    return request

# Dependency to validate compression request
def validate_compression_request(request: CompressionRequest):
    if not request.text.strip():
        raise HTTPException(status_code=422, detail="Input text cannot be empty")
    return request

# Define endpoint for text summarization
@app.post("/summarize/")
async def summarize(text: str = Depends(validate_input_text), request: SummarizeRequest = Depends(validate_summarize_request)):
    try:
        # Perform summarization here using the 'text' and 'request.summary_length'
        summary_text = "This is a summarized text."
        return JSONResponse(content=jsonable_encoder({"Summary": summary_text}), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Define endpoint for text compression
@app.post("/compress_summary/")
async def compress_summary(text: str = Depends(validate_input_text), request: CompressionRequest = Depends(validate_compression_request)):
    try:
        # Perform compression here using the 'text' and 'request.summary_length'
        compressed_text = "This is a compressed text."
        return JSONResponse(content=jsonable_encoder({"Compressed_summary": compressed_text}), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
