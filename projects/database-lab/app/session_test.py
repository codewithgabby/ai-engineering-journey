from app.database import SessionLocal

session = SessionLocal()

print(session)

session.close()