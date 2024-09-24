from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Venue, Concert

# Database setup
engine = create_engine('sqlite:///concerts.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def main():
    session = Session()

    # Placeholder for future data
    # You can add more functionality here

if __name__ == "__main__":
    main()
