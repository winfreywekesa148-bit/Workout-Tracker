from extensions import db

class WorkoutExercise(db.Model):

    __tablename__ = 'workout_exercises'

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    sets = db.Column(db.Integer, nullable=True)
    reps = db.Column(db.Integer, nullable=True)
    duration_seconds = db.Column(db.Integer, nullable=True)

    # relationships
    workout = db.relationship('Workout', back_populates='workoutexercises')
    exercise = db.relationship('Exercise', back_populates='workoutsexercises')
