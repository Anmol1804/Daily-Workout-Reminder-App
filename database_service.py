import mysql.connector

table = "workouts"
table_today = "workout_today"


conn = mysql.connector.connect(
    host='127.0.0.1',
    user="root",
    password="",
    db="workout_app"
)

cursor = conn.cursor()
Query = "INSERT INTO workout_today VALUES ('123');"
cursor.execute(Query)

# cursor.execute("SELECT * FROM WORKOUTS")
cursor.close()


def insert_workout(workout_data):
    pass

def delete_workout(workout_id):
    pass

def get_all_workout():
    pass

def get_workout_today():
    pass

def update_workout_today(workout_data, insert=False):
    pass



