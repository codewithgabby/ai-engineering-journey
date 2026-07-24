from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg://postgres:REMOVED_SECRET@localhost:5432/database_lab"

engine = create_engine(DATABASE_URL)