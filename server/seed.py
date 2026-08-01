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

    # Create a workout
    workout1 = Workout(name="Full Body Workout", date="2024-06-01", duration_minutes=45, notes="A full body workout routine.")
    workout2 = Workout(name="Cardio Blast", date="2024-06-02", duration_minutes=30, notes="High-intensity cardio session.")

    # Add the workout to the session
    workout1.save()
    workout2.save()
    
    # Create workout exercises
    workout_exercise1 = WorkoutExercise(workout_id=workout1.id, exercise_id=exercise1.id, sets=3, reps=15)
    workout_exercise2 = WorkoutExercise(workout_id=workout2.id, exercise_id=exercise2.id, sets=4, reps=20)

    # Add workout exercises to the session
    workout_exercise1.save()
    workout_exercise2.save()



