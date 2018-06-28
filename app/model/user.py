from app import db


class User(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).one()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
