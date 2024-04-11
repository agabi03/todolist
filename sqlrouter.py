from fastapi import APIRouter, Depends
from pydantic import BaseModel

from auth import get_current_username
from connect_to_db import create_connection

db_r = APIRouter(
    prefix="/db",
    dependencies=[Depends(get_current_username)]
)


class TodoItem(BaseModel):
    title: str


@db_r.get('/todolist/')
def show_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM todolist""")
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    columns = [column[0] for column in cursor.description]
    result = [dict(zip(columns, row)) for row in books]
    return result


@db_r.post('/post_todolist/')
def create_todo(todo_item: TodoItem):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO todolist (title) VALUES (?)""", (todo_item.title,))
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Todo item created successfully", "item": todo_item.title}


@db_r.delete('/del_todolist/')
def delete_todo(todo_item: TodoItem):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM todolist
    WHERE title=?""", (todo_item.title,))
    connection.commit()
    cursor.close()
    connection.close()