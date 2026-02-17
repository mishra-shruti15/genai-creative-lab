from pydantic import BaseModel


class FeedbackCreate(BaseModel):
    user_name: str
    message: str


class FeedbackResponse(FeedbackCreate):
    id: int

    class Config:
        from_attributes = True

