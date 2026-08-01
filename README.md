# Workout-Tracker

## Project Description
The Workout Tracker Backend API is a Flask-based REST API that allows personal trainers to create and manage workouts and exercises.

## Installation

### Clone the repository

```bash
git clone <repository-url>

cd Workout-Tracker/server

pip install -r requirements.txt
```

### Run the application
```bash
flask run
```

## API Endpoints

### Authentication

GET /workouts = list all workouts

POST /workouts = creates workout

GET /exercises = list all exercises

POST /exercises = creates exercises

GET /workouts exercises = list all workouts exercises

POST /workouts exercises = creates workout exercises
