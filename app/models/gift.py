from sqlalchemy import Column, String, Text

from app.core.db import Base


class Gift(Base):
    name = Column(String(100), nullable=False)
    comment = Column(Text)
