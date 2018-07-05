from app import db
from ..model import BaseModel


class User(BaseModel):
    id = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @property
    def books(self):
        from .book import Book
        return Book.query.filter_by(author_id=self.id)

    @property
    def poems(self):
        from .poem import Poem
        return Poem.query.filter_by(author_id=self.id, book_id=None)
