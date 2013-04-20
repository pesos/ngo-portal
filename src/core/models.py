from . import db

# Application models

class User(db.Model):
    """ `User` is any entity which uses the application. User will
    have a valid facebook account to access the application.
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return "<User:%r:%r>" % (self.id , self.name)