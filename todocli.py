import typer
from typing import Optional
from rich.console import Console
from rich.table import Table
from database import *

console = Console()

app = typer.Typer()


# color formatting for categories
COLORS = {"learn": "cyan",
          "read": "yellow",
          "rest": "green",
          }


@app.command(short_help="adds an item")
def add(task: str, category: str):
    typer.echo(f'Adding "{task}" under [{category}] category')

    todo = Todo(task, category)
    insert_todo(todo)
    show()


@app.command(short_help="deletes an item")
def delete(position: int):
    # position of todo object in UI starts from 1, so subtract 1
    name = get_task_name(position - 1)
    typer.echo(f'deleting "{name}"')

    delete_todo(position - 1)
    show()


@app.command(short_help="updates an item")
def update(position: int, task: str = typer.Argument(None), category: str = typer.Argument(None)):
    name = get_task_name(position - 1)
    typer.echo(f'updating task name from "{name}" -> "{task}"')

    update_todo(position - 1, task, category)
    show()


@app.command(short_help="completes an item")
def complete(position: int):
    name = get_task_name(position - 1)
    typer.echo(f'completed "{name}"')

    complete_todo(position - 1)
    show()


@app.command(short_help="removes all completed tasks")
def remove_done():
    typer.echo(f"removed completed tasks")

    clear_all_done_tasks()
    show()


@app.command(short_help="removes all tasks")
def clear():
    confirm = typer.confirm("Are you sure you want to clear all tasks?")

    if not confirm:
        typer.echo("not deleting")
        raise typer.Abort()
    typer.echo("deleted all tasks...")
    clear_all_tasks()
    show()


@app.command(short_help="show the todos in a table")
def show():
    tasks = get_all_todos()
    console.print("\n[bold magenta]Todos[/bold magenta]!", "💻")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")

    def get_category_color(category):
        if category in COLORS:
            return COLORS[category]
        return 'white'

    for idx, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        is_done_str = "✅" if task.status == 2 else "❌"
        table.add_row(str(idx), task.task,
                      f"[{c}]{task.category}[/{c}]", is_done_str)

    console.print(table)


if __name__ == "__main__":
    app()
