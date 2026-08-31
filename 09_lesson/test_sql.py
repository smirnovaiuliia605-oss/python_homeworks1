import pytest
from sqlalchemy import create_engine, text


db_connection_string = ("postgresql://postgres:123@localhost:5432/QA")
db = create_engine(db_connection_string)


def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM users"))


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO users"
               " (\"user_id\",\"user_email\",\"subject_id\")"
               " VALUES ('1795','smirnova@list.ru','25')")
    connection.execute(sql, {"new_user_email": "smirnova@list.ru"})

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE users SET subject_id = '25' WHERE user_id = 1795")
    connection.execute(sql, {"user_id": 'New user_id', "id": 1795})

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM users WHERE user_id = :user_id")
    connection.execute(sql, {"user_id": 1795})

    transaction.commit()
    connection.close()
