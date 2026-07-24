import uuid
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship



class Author(SQLModel, table=True):

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True
    )

    name: str = Field()

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={
            "onupdate": lambda: datetime.now(timezone.utc),
        }
    )

    books: list["Book"] = Relationship(
        back_populates="author",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "lazy": 'selectin'
        }
    )



class Book(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True
    )

    name: str = Field()

    published_year: int = Field()
    author_id: uuid.UUID = Field(
        foreign_key="author.id",
        ondelete='CASCADE'
    )

    author: "Author" = Relationship(
        back_populates='books'
    )





# author.books