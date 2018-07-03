from app import db
from ..model import BaseModel


class Book(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author_id = db.Column(db.String, db.ForeignKey('user.id', ondelete='cascade'), nullable=False)

    @property
    def poems(self):
        from .poem import Poem
        return Poem.query.filter_by(book_id=self.id)
