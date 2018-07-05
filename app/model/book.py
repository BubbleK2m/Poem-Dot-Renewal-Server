from app import db
from ..model import BaseModel


class Book(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    author_id = db.Column(db.String, db.ForeignKey('user.id', ondelete='cascade'), nullable=False)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @property
    def poems(self):
        from .poem import Poem
        return Poem.query.filter_by(book_id=self.id)

    @property
    def hearts(self):
        from .heart import Heart
        return Heart.query.filter_by(book_id=self.id)

    def to_dict(self):
        return dict(super(Book, self).to_dict(),
                    poems=[p.to_dict() for p in self.poems],
                    hearts=self.hearts.count())
