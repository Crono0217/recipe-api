from app.db.database import engine, Base
from app.models.recipe import Recipe

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":      #executes only when executed directly, not when imported
    create_tables()
    print("Tables created with success.")