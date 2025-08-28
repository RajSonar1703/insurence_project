# from fastapi import APIRouter, UploadFile, Depends
# from sqlalchemy.orm import Session
# from database import SessionLocal
# from models import Policy

# import fitz  # PyMuPDF

# router = APIRouter()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/upload-policy")
# async def upload_policy(file: UploadFile, user_email: str, db: Session = Depends(get_db)):
#     content = ""
#     with fitz.open(stream=await file.read(), filetype="pdf") as doc:
#         for page in doc:
#             content += page.get_text()

#     new_policy = Policy(user_email=user_email, raw_text=content)
#     db.add(new_policy)
#     db.commit()
#     db.refresh(new_policy)
#     return {"message": "Policy uploaded successfully", "policy_id": new_policy.id}


from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Policy
import fitz  # PyMuPDF

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload-policy")
async def upload_policy(
    file: UploadFile = File(...),
    user_email: str = Form(...),
    db: Session = Depends(get_db)
):
    content = ""
    with fitz.open(stream=await file.read(), filetype="pdf") as doc:
        for page in doc:
            content += page.get_text()

    new_policy = Policy(user_email=user_email, raw_text=content)
    db.add(new_policy)
    db.commit()
    db.refresh(new_policy)
    return {"message": "Policy uploaded successfully", "policy_id": new_policy.id}
