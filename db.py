import sqlite3


def execute_query(sql_query):
    with sqlite3.connect('chat.db') as db:
        cur = db.cursor()
        result = cur.execute(sql_query)
        db.commit()
    return result


def insert_msg(name, message):
    sql_query = "INSERT INTO chat(name,messages) VALUES ('%s','%s')" % (
        name, message)
    execute_query(sql_query)


def display_msg():
    sql_query = ''' SELECT * from chat '''
    result = execute_query(sql_query)
    return result.fetchall()


def delete_all():
    sql_query = ''' DELETE FROM chat '''
    result = execute_query(sql_query)


