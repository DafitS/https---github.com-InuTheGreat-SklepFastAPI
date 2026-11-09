from sqlalchemy import text
from app.db.database import engine


try:
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database()")
        )

        database_name = result.scalar()

        print("POLACZENIE UDANE!")
        print(f"Baza danych: {database_name}")

except Exception as error:
    print("BLAD POLACZENIA!")
    print(error)