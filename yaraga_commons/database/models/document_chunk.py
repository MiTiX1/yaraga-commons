from sqlalchemy import Column, Integer, String, TIMESTAMP, text, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector  # <-- use this for pgvector
from yaraga_commons.database.base import Base


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    chunk_uuid = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id", ondelete="CASCADE"), nullable=False)
    chunk_number = Column(Integer, nullable=False)
    content = Column(String, nullable=False)
    tsv = Column(TSVECTOR, nullable=False)
    embedding = Column(Vector(768))  # <-- fixed
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"))
    corpus_id = Column(UUID(as_uuid=True), ForeignKey("corpuses.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    document = relationship("Document", back_populates="chunks")

    __table_args__ = (
        UniqueConstraint("document_id", "chunk_number"),
    )
