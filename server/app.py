from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from extensions import db

from models.Exercise import Exercise
from models.Workout import Workout
from models.WorkoutExercises import WorkoutExercise

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# get all workout
@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify([workout.to_dict() for workout in workouts])

# get each workout
@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    return jsonify(workout.to_dict())

# create a new workout
@app.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()
    workout = Workout(date=data['date'], duration_minutes=data['duration_minutes'], notes=data('notes', ''))
    db.session.add(workout)
    db.session.commit()
    return jsonify(workout.to_dict()), 201

# delete a workout
@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return '', 204

# get all exercises
@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify([exercise.to_dict() for exercise in exercises])

# get each exercise
@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    return jsonify(exercise.to_dict())

# create a new exercise
@app.route('/exercises', methods=['POST'])
def create_exercise():
    data = request.get_json()
    exercise = Exercise(name=data['name'], category=data['category'], equipment_needed=data('equipment_needed', False))
    db.session.add(exercise)
    db.session.commit()
    return jsonify(exercise.to_dict()), 201

# delete an exercise
@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    db.session.delete(exercise)
    db.session.commit()
    return jsonify({"message": f"Exercise {id} deleted"})

# get all workout exercises
@app.route('/workout_exercises', methods=['GET'])
def get_workout_exercises():
    workout_exercises = WorkoutExercise.query.all()
    return jsonify([we.to_dict() for we in workout_exercises])

# create a new workout exercise
@app.route('/workout_exercises', methods=['POST'])
def create_workout_exercise():
    data = request.get_json()
    workout_exercise = WorkoutExercise(workout_id=data['workout_id'], exercise_id=data['exercise_id'], sets=data['sets'], reps=data['reps'], duration_seconds=data('duration_seconds'))
    db.session.add(workout_exercise)
    db.session.commit()
    return jsonify(workout_exercise.to_dict()), 201

if __name__ == '__main__':
    app.run(port=5555, debug=True)
