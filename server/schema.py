from marshmallow import Schema, fields, validates, ValidationError


#exercise schema
class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool(default=False)

    @validates('name')
    def validate_name(self, value):
        if not value:
            raise ValidationError('Name is required.')

#workout schema
class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()

    @validates('duration_minutes')
    def validate_duration(self, value):
        if value <= 0:
            raise ValidationError('Duration must be greater than 0')

#workout exercise schema
class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    sets = fields.Int(required=True)
    reps = fields.Int(required=True)
    duration_seconds = fields.Int()

    @validates('sets')
    def validate_sets(self, value):
        if value <= 0:
            raise ValidationError('Sets must be greater than 0')

    @validates('reps')
    def validate_reps(self, value):
        if value <= 0:
            raise ValidationError('Reps must be greater than 0')

