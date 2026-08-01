#!/usr/bin/env python3

from app import app
from models.WorkoutExercises import WorkoutExercise
from models.Workout import Workout
from models.Exercise import Exercise

with app.app_context():
