from sqlalchemy import Integer, String
from main import db
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn


class Base(DeclarativeBase):
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = MappedColumn(Integer, primary_key=True)
    title: Mapped[str] = MappedColumn(String(150), nullable=False)
    author: Mapped[str] = MappedColumn(String(150), nullable=False)
    rating: Mapped[float] = MappedColumn(Integer, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"
