#!/usr/bin/python3
"""model state"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    Represents a state with an ID and a name.

    Attributes:
        id (int): The unique identifier of the state.
        name (str): The name of the state.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
