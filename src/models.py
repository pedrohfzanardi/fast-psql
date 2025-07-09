from sqlalchemy import Column, Integer, String

from config import Base


class Item(Base):
    __tablename__ = "items"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String)
    description: str = Column(String)

    def __repr__(self):
        return f"<Item(id={self.id}, name={self.name}, description={self.description})>"
