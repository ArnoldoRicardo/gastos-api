from typing import TYPE_CHECKING

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .tipo import Tipo  # noqa: F401


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    cantidad =  Column(Float)
    total =  Column(Float)
    fecha =  Column(Date)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="items")
    tipo_id = Column(Integer, ForeignKey("tipo.id"))
    tipo = relationship("Tipo", back_populates="items")
