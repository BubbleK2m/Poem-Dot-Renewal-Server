from app import db
from ..model import BaseModel


class Poem(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id', ondelete='cascade'), default=None)
    author_id = db.Column(db.String(20), db.ForeignKey('user.id', ondelete='cascade'), nullable=False)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
