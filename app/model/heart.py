from app import db
from ..model import BaseModel


class Heart(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.String(20), db.ForeignKey('user.id', ondelete='cascade'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id', ondelete='cascade'))

    __table_args__ = (
        db.UniqueConstraint('author_id', 'book_id'),
    )

    @classmethod
    def find_by_book_and_author_id(cls, book_id, author_id):
        return cls.query.filter_by(book_id=book_id, author_id=author_id).first()
