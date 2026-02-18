from pydantic import BaseModel

"""
This file controls input validation and response format.
Defines what data looks like when:
•	client sends request
•	API sends response
"""

# POST /feedback, validates incoming JSON
class FeedbackCreate(BaseModel): 
    user_name: str
    message: str


class FeedbackResponse(FeedbackCreate):
    id: int

    class Config:
        from_attributes = True

