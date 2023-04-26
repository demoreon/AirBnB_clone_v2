#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay:
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place")
        amenities = relationship('Amenity', secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """ Returns list of reviews.id """
            from models import Review
            rel_rev = [review for review in models.storage.all(Review).values()
                       if self.id == review.place_id]
            return rel_rev

        @property
        def amenities(self):
            '''returns the list of Amenity instances based on the attributes
               amenity_ids that contains all Amenity.id linked to the Place
            '''
            from models.amenity import Amenity
            rel_amenity = [models.storage.all(Amenity).get(amenity_id)
                           for amenity_id in self.amenity_ids]
            return rel_amenity

        @amenities.setter
        def amenities(self, obj):
            ''' Adds Amenity.id to the attribute amenity_ids'''
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
