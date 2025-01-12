from sqlmodel import create_engine, SQLModel

mydb = create_engine("sqlite:///database.db", echo=True)

def create_db_and_tables():
  SQLModel.metadata.create_all(mydb)
  