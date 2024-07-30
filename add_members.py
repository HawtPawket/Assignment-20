from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        new_member = ("Hazel Patrick", "4", "19")

        query = "INSERT INTO members (name, id, age) VALUES (%s, %s, %s)"

        cursor.execute(query, new_member)
        conn.commit()
        print("New member added successfully.")

    finally:
        cursor.close()
        conn.close()

# adds new members to the table