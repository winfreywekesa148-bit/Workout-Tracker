from extensions import db

class Exercise(db.Model):

    __tablename__ = 'exercises'

    id = db.Column(db.Interger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    equipment_needed = db.Column(db.Boolean, nullable=True)

    # relationships
    workoutsexercises = db.relationship('Workout', back_populates='exercises')
