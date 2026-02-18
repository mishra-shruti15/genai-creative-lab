from sqlalchemy import Column, Integer, String, Text
from database import Base

# This script defines how feedback data is stored in PostgreSQL.
# Database name is feedback_db

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)

