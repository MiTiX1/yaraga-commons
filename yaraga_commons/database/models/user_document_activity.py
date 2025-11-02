from sqlalchemy import Column, TIMESTAMP, text, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from yaraga_commons.database.base import Base


class UserDocumentActivity(Base):
    __tablename__ = "user_document_activity"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id", ondelete="CASCADE"), nullable=False)
    last_opened_at = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("user_id", "document_id"),
    )

    user = relationship("User", back_populates="document_activities")
    document = relationship("Document", back_populates="user_activities")
