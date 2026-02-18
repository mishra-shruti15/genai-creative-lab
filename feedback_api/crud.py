from sqlalchemy.orm import Session
from models import Feedback
from schemas import FeedbackCreate

# CRUD = Create, Read, Update and Delete
# Contains all DB operations and logic

def create_feedback(db: Session, feedback: FeedbackCreate):
    # convert pydantic model to SQLAlchemy model
    feedback_obj = Feedback(
        user_name=feedback.user_name,
        message=feedback.message
    )
    db.add(feedback_obj)
    db.commit()
    db.refresh(feedback_obj)
    return feedback_obj

# Fetch single feedback by ID
# SQL equivalent: SELECT * FROM feedbacks WHERE id = x;
def get_feedback(db: Session, feedback_id: int):
    return db.query(Feedback).filter(
        Feedback.id == feedback_id
    ).first()

# Fetch and delete records and then commit.
def delete_feedback(db: Session, feedback_id: int):
    feedback = get_feedback(db, feedback_id)
    if feedback:
        db.delete(feedback)
        db.commit()
    return feedback

# List all feedback
# SQL equivalent: SELECT * FROM feedbacks;
def get_all_feedbacks(db: Session):
    return db.query(Feedback).all()

