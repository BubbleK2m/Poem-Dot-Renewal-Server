from app import db


class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, **kwargs):
        for attr, val in kwargs:
            setattr(self, attr, val)

        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()
