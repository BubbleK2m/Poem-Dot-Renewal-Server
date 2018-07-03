from app import db
from ..model import BaseModel


class Heart(BaseModel):
    author_id = db.Column(db.String, db.ForeignKey('user.id', ondelete='cascade'))
    book_id = db.Column(db.String, db.ForeignKey('book.id', ondelete='cascade'))

    @property
    def author(self):
        from .user import User
        return User.find_by_id(self.author_id)
