from app.database import SessionLocal
from app.models import Tag


db = SessionLocal()

try:
    tags = db.query(Tag).all()

    print("Tags in database:")

    for tag in tags:
        print(tag.id, tag.name)

finally:
    db.close()