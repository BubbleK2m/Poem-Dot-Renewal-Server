from app import db
from ..model import BaseModel


class Poem(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String, nullable=False)
    book_id = db.Column(db.String, db.ForeignKey('book.id', ondelete='cascade'))
    author_id = db.Column(db.String, db.ForeignKey('user.id', ondelete='cascade'), nullable=False)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).one()
