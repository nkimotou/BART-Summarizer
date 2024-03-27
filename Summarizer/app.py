from fastapi import FastAPI, HTTPException
from transformers import pipeline
from pydantic import BaseModel

"""
This localhost application exposes an API that can receive user-provided text inputs 
and summarize them using the Hugging Face BART model. 
There is an extended functionality to provide a compressed summary based on consecutive
repeating characters in the user-provided text. 

    Example:
    Original Summary: This committee meets annually to assess the effectiveness of policies on environmental protection.
    Compressed Summary: This com2it2e2 me2ts an2ual2y to as2es2 the ef2ectivenes2 of policies on environmental protection.

In the compressed summary example above, the 2s represent where there are repeating consecutive characters. 
Committee has two m, t, and e characters repeating consecutively. Therefore, it's returned as 'com2it2e2' in the summary. 
"""

# Initialize FastAPI application
app = FastAPI()

# Set up Hugging Face model for text input summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Set text and summary_length datatype in model for body of the request
class TextRequest(BaseModel):
    text: str
    summary_length: int = 50

# Define endpoint in the FastAPI application to accept POST requests for summarize
@app.post("/summarize/")
async def summarize_text(request: TextRequest):
    try:
        # Get summarized text by setting summary = to the summarizer object that has specifying parameters for the model
        summary = summarizer(request.text, max_length=request.summary_length, min_length=30, do_sample=False)
        # Return a dictionary containing the summary string
        # This portion is the response
        return {"Summary": summary[0]["summary_text"]}
    except Exception as e:
        # Raise standard internal web server error if request cannot be fulfilled
        raise HTTPException(status_code=500, detail=str(e))

# Define endpoint in the FastAPI application to accept POST requests for compress_summary
@app.post("/compress_summary/")
# Create an asynchronous function to handle requests coming into the endpoint
async def compress_summary(request: TextRequest):
    # Try to get summarized text, else perform an alternative action
    try:
        # Get summarized text by setting summary = to the summarizer object that has specifying parameters for the model
        summary = summarizer(request.text, max_length=request.summary_length, min_length=30, do_sample=False)[0]["summary_text"]
        # Compress summary using compression algorithm
        # Initialize an empty string to store the compressed summary text
        compressed_summary = ""
        # Set count = 1 to keep track of any repeating consecutive numbers
        count = 1
        # Iterate of characters in the summary text
        for i in range(1, len(summary)):
            # If a character is the same as the character in the previous index
            if summary[i] == summary[i - 1]:
                # Increase the counter to indicate it's a repeating consecutive character
                count += 1
            else:
                # If the character is not the same the character in previous index
                if count == 1:
                    # Append the character to the compressed summary
                    compressed_summary += summary[i - 1]
                else:
                    compressed_summary += summary[i - 1] + str(count)
                    count = 1
        # End iterative loop
        # Append the final character to compressed summary
        if count == 1:
            compressed_summary += summary[-1]
        else:
            compressed_summary += summary[-1] + str(count)
        # Return a dictionary containing the compressed summary string
        # This portion is the response
        return {"Compressed_summary": compressed_summary}
    except Exception as e:
        # Raise standard internal web server error if request cannot be fulfilled
        raise HTTPException(status_code=500, detail=str(e))
