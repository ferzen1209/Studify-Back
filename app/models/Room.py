from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

from db import Base


class Room(Base):
    __tablename__ = "rooms"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    building = Column(String, nullable=False)
    location_description = Column(String, nullable=True)
    capacity = Column(Integer, nullable=False)
    current_occupancy = Column(Integer, nullable=False)
    features = Column(JSON, nullable=False)  # lista de strings
    coordinates = Column(JSON, nullable=False)  # { x: number, y: number }
    is_silent = Column(Boolean, nullable=False, default=False)
    next_free_time = Column(String, nullable=True)  # o Time, si prefieres
