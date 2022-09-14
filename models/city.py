#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "city"
    name = Column(String(128), nullable=False)
    state_id = Column(String(128), ForeignKey("states.id"), nullable=False)
