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




if __name__ == '__main__':
    app.run(port=5555, debug=True)
