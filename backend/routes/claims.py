# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from database import SessionLocal
# from models import ClaimCheck


# router = APIRouter()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/check-claim")
# def check_claim(condition: str, db: Session = Depends(get_db)):
#     covered_conditions = ["cataract", "ayush", "surgery", "icu"]
#     eligible = "Yes" if condition.lower() in covered_conditions else "No"
#     reason = "Covered by Arogya Sanjeevani" if eligible == "Yes" else "Not covered in standard policy"
    
#     record = ClaimCheck(condition=condition, eligible=eligible, reason=reason)
#     db.add(record)
#     db.commit()
#     db.refresh(record)
#     return {"condition": condition, "eligible": eligible, "reason": reason}



from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import SessionLocal
from models import ClaimCheck

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/check-claim")
def check_claim(condition: str = Query(...), db: Session = Depends(get_db)):
    covered_conditions = ["cataract", "ayush", "surgery", "icu"]
    eligible = "Yes" if condition.lower() in covered_conditions else "No"
    reason = "Covered by Arogya Sanjeevani" if eligible == "Yes" else "Not covered in standard policy"
    
    record = ClaimCheck(condition=condition, eligible=eligible, reason=reason)
    db.add(record)
    db.commit()
    db.refresh(record)
    return {"condition": condition, "eligible": eligible, "reason": reason}
