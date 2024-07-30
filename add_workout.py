from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        new_workoutsessions = ("2", "1245", "2024-07-29", "Evening", "Running")

        query = "INSERT INTO workoutsessions (member_id, session_id, session_date, session_time, activity) VALUES (%s,%s,%s,%s,%s)"

        cursor.execute(query, new_workoutsessions)
        conn.commit()
        print("Workout session added successfully.")

    finally:
        cursor.close()
        conn.close()

        from connect_mysql import connect_database

# adds workouts to the table