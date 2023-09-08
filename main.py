#5 урок
import sqlite3

class User:
    def __init__(self,name,surname,gender):
        self.name=name
        self.surname=surname
        self.gender=gender
def create_table_user(cursor):
    command="""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        gender TEXT);
    """
    cursor.execute(command)

def add_user(cursor,user):
    command = """
    INSERT INTO users (name,surname,gender) VALUES (?,?,?);
    """
    cursor.execute(command, (user.name, user.surname, user.gender))

def get_users_list(cursor):
    command = """
    SELECT * FROM users
    """
    result = cursor.execute(command)
    users = result.fetchall()
    print(users)

def get_users(cursor,user_id):
    command = """
    SELECT * FROM users WHERE id = ?;
    """
    result = cursor.execute(command, (user_id,))
    users = result.fetchall()
    print(users)

def update_user_name(curcor, value, user_id):
    command = """
    UPDATE users SET name = ? WHERE id = ?;
    """
    curcor.execute(command, (value, user_id,))

def delete_users(cursor):
    command = """
    DELETE FROM users;
    """
    cursor.execute(command)
if __name__ == '__main__':
    with sqlite3.connect('base1.db') as cursor:
        print(cursor)
        create_table_user(cursor)
        delete_users(cursor)
        add_user(cursor, User(name='Максим',surname='Иванов',gender='male'))
        add_user(cursor, User(name='Владимир', surname='Орлов', gender='male'))
        add_user(cursor, User(name='Катя', surname='Дудкина', gender='female'))
        get_users_list(cursor)
        update_user_name(cursor, 'Юля', 3 )
        get_users(cursor, 3)