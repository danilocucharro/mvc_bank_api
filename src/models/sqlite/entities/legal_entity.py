from sqlalchemy import Column, BIGINT, String, INTEGER
from src.models.sqlite.settings.base import Base

class LegalEntityTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True)
    faturamento = Column(INTEGER, nullable=False)
    idade = Column(INTEGER, nullable=False)
    nome_fantasia = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    email_corporativo = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(INTEGER, nullable=False)