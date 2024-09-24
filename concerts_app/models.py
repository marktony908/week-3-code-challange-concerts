from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)

    concerts = relationship('Concert', back_populates='band', overlaps="venue")
    venues = relationship('Venue', secondary='concerts', back_populates='bands')

    def all_introductions(self):
        return [f"Hello {venue.city}!!!!! We are {self.name} and we're from {self.hometown}" for venue in self.venues]

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)

    concerts = relationship('Concert', back_populates='venue', overlaps="band")
    bands = relationship('Band', secondary='concerts', back_populates='venues')

class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    date = Column(String, nullable=False)

    band = relationship('Band', back_populates='concerts', overlaps="venues")
    venue = relationship('Venue', back_populates='concerts', overlaps="bands")
