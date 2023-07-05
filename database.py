import sqlite3

username = 'funkymonjey'
def   insert_username(username):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO 'usernames' VALUES ('%s')" % username)

        users = cursor.execute("SELECT * FROM 'usernames'")
        print(users.fetchall())

        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        if conn:
            conn.close()