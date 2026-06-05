from database import DatabaseManager
class WorkoutService:
    @staticmethod
    def calculate_1rm(weight, reps): return weight if reps == 1 else round(weight * (1 + (reps / 30)), 2)
    @classmethod
    def log_workout(cls, exercise, sets, reps, weight):
        exercise = exercise.lower().strip()
        with DatabaseManager() as cursor:
            cursor.execute('INSERT INTO workout_logs (exercise_name, sets, reps, weight) VALUES (?, ?, ?, ?)', (exercise, sets, reps, weight))
        cls.update_pr(exercise, weight, cls.calculate_1rm(weight, reps))
    @staticmethod
    def update_pr(exercise, weight, calculated_1rm):
        with DatabaseManager() as cursor:
            cursor.execute('SELECT max_weight FROM personal_records WHERE exercise_name = ?', (exercise,))
            record = cursor.fetchone()
            if record is None:
                cursor.execute('INSERT INTO personal_records (exercise_name, max_weight, calculated_1rm) VALUES (?, ?, ?)', (exercise, weight, calculated_1rm))
            elif weight > record['max_weight']:
                cursor.execute('UPDATE personal_records SET max_weight = ?, calculated_1rm = ? WHERE exercise_name = ?', (weight, calculated_1rm, exercise))
  
