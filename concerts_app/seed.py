from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Venue, Concert

# Database setup
engine = create_engine('sqlite:///concerts.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def seed_database():
    session = Session()

    # Create sample bands
    band1 = Band(name="The Beatles", hometown="Liverpool")
    band2 = Band(name="The Rolling Stones", hometown="London")

    # Create sample venues
    venue1 = Venue(title="Madison Square Garden", city="New York")
    venue2 = Venue(title="The O2", city="London")

    # Create sample concerts
    concert1 = Concert(band=band1, venue=venue1, date="2024-09-23")
    concert2 = Concert(band=band2, venue=venue2, date="2024-10-01")

    # Add to the session
    session.add_all([band1, band2, venue1, venue2, concert1, concert2])
    session.commit()

    print("Database seeded with initial data.")

if __name__ == "__main__":
    seed_database()
