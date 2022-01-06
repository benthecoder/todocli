import sqlite3
from typing import List
import datetime
from model import Todo

conn = sqlite3.connect('todos.db')
c = conn.cursor()


def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS todos (
            task text,
            category text,
            date_added text,
            date_completed text,
            status integer,
            position integer
            )''')


create_table()


def insert_todo(todo: Todo):
    c.execute('SELECT COUNT(*) FROM todos')
    count = c.fetchone()[0]
    todo.position = count if count else 0
    with conn:
        c.execute('INSERT INTO todos VALUES (:task, :category, :date_added, :date_completed, :status, :position)',
                  {'task': todo.task, 'category': todo.category, 'date_added': todo.date_added,
                   'date_completed': todo.date_completed, 'status': todo.status, 'position': todo.position})


def get_all_todos() -> List[Todo]:
    c.execute('SELECT * FROM todos')
    results = c.fetchall()
    todos = []
    for result in results:
        todos.append(Todo(*result))
    return todos


def delete_todo(position: int):
    c.execute('SELECT COUNT(*) FROM todos')
    count = c.fetchone()[0]

    with conn:
        c.execute('DELETE FROM todos WHERE position=:position',
                  {'position': position})
        for pos in range(position + 1, count):
            change_position(pos, pos - 1, False)


def change_position(curr_pos: int, new_pos: int, commit: bool = True):
    c.execute('UPDATE todos SET position = :new_pos WHERE position = :curr_pos', {
        'new_pos': new_pos, 'curr_pos': curr_pos
    })

    # within context manager, all changes are internally committed
    if commit:
        conn.commit()


def update_todo(position: int, task: str, category: str):
    with conn:
        if task is not None and category is not None:
            c.execute('UPDATE todos SET task = :task, category = :category WHERE position = :position', {
                'task': task, 'category': category, 'position': position
            })
        elif task is not None:
            c.execute('UPDATE todos SET task = :task WHERE position = :position', {
                'task': task, 'position': position
            })
        elif category is not None:
            c.execute('UPDATE todos SET category = :category WHERE position = :position', {
                'category': category, 'position': position
            })


def complete_todo(position: int):
    with conn:
        c.execute('UPDATE todos SET status = 2, date_completed = :date_completed WHERE position = :position', {
            'position': position, 'date_completed': datetime.datetime.now().isoformat()
        })


def get_task_name(position: int) -> str:
    c.execute('SELECT task FROM todos where position = :position', {
        'position': position
    })
    task_name = c.fetchone()[0]
    return task_name


def clear_all_done_tasks():
    with conn:
        c.execute('DELETE FROM todos WHERE status = 2')


def clear_all_tasks():
    with conn:
        c.execute('DELETE FROM todos')
