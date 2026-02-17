from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud
from database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Feedback API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/feedback", response_model=schemas.FeedbackResponse)
def create_feedback(
    feedback: schemas.FeedbackCreate,
    db: Session = Depends(get_db)
):
    return crud.create_feedback(db, feedback)


@app.get("/feedback/{feedback_id}", response_model=schemas.FeedbackResponse)
def get_feedback(feedback_id: int, db: Session = Depends(get_db)):
    feedback = crud.get_feedback(db, feedback_id)
    if not feedback:
        raise HTTPException(
            status_code=404,
            detail="Feedback not found"
        )
    return feedback


@app.delete("/feedback/{feedback_id}")
def delete_feedback(feedback_id: int, db: Session = Depends(get_db)):
    feedback = crud.delete_feedback(db, feedback_id)
    if not feedback:
        raise HTTPException(
            status_code=404,
            detail="Feedback not found"
        )
    return {"message": "Feedback deleted successfully"}


@app.get(
    "/feedbacks",
    response_model=List[schemas.FeedbackResponse]
)
def list_feedbacks(db: Session = Depends(get_db)):
    return crud.get_all_feedbacks(db)

