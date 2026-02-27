from app.extensions import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    category = db.Column(db.String(100))
    location = db.Column(db.String(100))
    type = db.Column(db.String(10))  # lost / found
    status = db.Column(db.String(20), default="open")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))