#!/usr/bin/python3
# models/place.py

from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

# Define the place_amenity table for the many-to-many relationship
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    __tablename__ = 'places'
    
    # Existing attributes...
    
    amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
    
    # For FileStorage
    @property
    def amenities(self):
        """Getter attribute amenities that returns the list of Amenity instances."""
        return [amenity for amenity in storage.all(Amenity).values() if amenity.id in self.amenity_ids]

    @amenities.setter
    def amenities(self, value):
        """Setter attribute amenities that handles append method for adding an Amenity.id."""
        if isinstance(value, Amenity):
            self.amenity_ids.append(value.id)

