#!/usr/bin/env python3

from app import app
from models.WorkoutExercises import WorkoutExercise
from models.Workout import Workout
from models.Exercise import Exercise
from extensions import db

with app.app_context():
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    db.session.commit()

    # Create some exercises
    exercise1 = Exercise(name="Push-up", category="Strength", equipment_needed=False)
    exercise2 = Exercise(name="Squat", category="Strength", equipment_needed=False)

    # Add exercises to the session
    exercise1.save()
    exercise2.save()




