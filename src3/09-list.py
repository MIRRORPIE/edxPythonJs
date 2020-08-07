import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

db_url = "postgres+psycopg2://postgres:raushan@localhost:5432/edxPython"

engine = create_engine(db_url)
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    main()
