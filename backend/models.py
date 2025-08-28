from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class Policy(Base):
    __tablename__ = "policies"
    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, nullable=False)
    upload_date = Column(DateTime, default=datetime.utcnow)
    raw_text = Column(Text)

class ClaimCheck(Base):
    __tablename__ = "claims"
    id = Column(Integer, primary_key=True, index=True)
    condition = Column(String)
    eligible = Column(String)  # Yes/No
    reason = Column(Text)
