from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    def to_string(self):
        return f"{self.id}: {self.title} Description {self.description}"

#we can configure lots of different types