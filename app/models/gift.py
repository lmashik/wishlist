from sqlalchemy import Column, String

from app.core.db import Base


class Gift(Base):
    name = Column(String(100), nullable=False)
