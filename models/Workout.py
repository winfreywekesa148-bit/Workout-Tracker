from extensions import db

class Workout(db.Model):
    
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)

    # relationships
    exercises = db.relationship('Exercise', secondary='workout_exercises', back_populates='workoutsexercises')
    workoutexercises = db.relationship('WorkoutExercise', back_populates='workout')
