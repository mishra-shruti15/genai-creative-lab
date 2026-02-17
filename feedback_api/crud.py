from sqlalchemy.orm import Session
from models import Feedback
from schemas import FeedbackCreate


def create_feedback(db: Session, feedback: FeedbackCreate):
    feedback_obj = Feedback(
        user_name=feedback.user_name,
        message=feedback.message
    )
    db.add(feedback_obj)
    db.commit()
    db.refresh(feedback_obj)
    return feedback_obj


def get_feedback(db: Session, feedback_id: int):
    return db.query(Feedback).filter(
        Feedback.id == feedback_id
    ).first()


def delete_feedback(db: Session, feedback_id: int):
    feedback = get_feedback(db, feedback_id)
    if feedback:
        db.delete(feedback)
        db.commit()
    return feedback


def get_all_feedbacks(db: Session):
    return db.query(Feedback).all()

