import sqlite3

username = 'funkymonjey'
def insert_username(username):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO 'usernames' VALUES ('%s')" % username)
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        if conn:
            conn.close()

insert_username(username)
def get_usernames():
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT nickname FROM usernames")
        data = [row[0] for row in cursor.fetchall()]
        return data
    except Exception as ex:
        print(ex)
    finally:
        if conn:
            conn.close()
