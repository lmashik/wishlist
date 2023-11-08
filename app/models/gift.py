from sqlalchemy import Column, String, Text, Integer

from app.core.db import Base


class Gift(Base):
    name = Column(String(100), nullable=False)
    comment = Column(Text)
    link = Column(String(256))
    price = Column(Integer)
    # author =
