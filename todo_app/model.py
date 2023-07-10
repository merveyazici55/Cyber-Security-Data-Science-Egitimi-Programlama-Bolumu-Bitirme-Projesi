from app import db

#Todo modeli
class Todo(db.Model):
    id = db.Coulmn(db.Integer, primary_key=True)
    title = db.Coulmn(db.String(100), nullable=False)
    completed = db.Coulmn(db.Boolean, default=False)
    reminder = db.Coulmn(db.DateTime)

    def __repr__(self):
        return '<Todo %r>' % self.title
    