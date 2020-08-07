import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

db_url = "postgres+psycopg2://postgres:raushan@localhost:5432/edxPython"

engine = create_engine(db_url)
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("11-flights.csv")
    reader = csv.reader(f)
    for org, dest, dur in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                    {"origin": org, "destination": dest, "duration": dur})
        print(f"Added flight from {org} to {dest} lasting {dur} minutes.")
    db.commit()

if __name__ == "__main__":
    main()
