from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel
import app
# Define a new model for feedback
class FeedbackRequest(BaseModel):
    feedback: str
    # Optional rating from 1 to 5
    rating: Optional[int] = None  


# Define endpoint to accept POST requests for feedback
@app.post("/feedback/")
async def submit_feedback(request: FeedbackRequest):
    try:
        # Print feedback
        print("Received feedback:", request.feedback)
        if request.rating is not None:
            print("Rating:", request.rating)

        # Return a confirmation response
        return {"message": "Feedback received successfully"}
    except Exception as e:
        # Raise standard internal web server error 
        raise HTTPException(status_code=500, detail=str(e))
