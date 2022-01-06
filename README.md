# TODO CLI in python

This is a todo app in the CLI built with Python.

## Tech Stack

- [Rich](https://github.com/Textualize/rich) - format the table and text colors.
- [Typer](https://github.com/tiangolo/typer) - CLI functionality
- sqlite3 - database for the tasks

## Demo

![example image of table](assets/app.png)

## Installation

First, install [poetry](https://python-poetry.org/)

```bash
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Check it's installed

```bash
  poetry --version
```

Poetry uses the currently activated Python version to create a virtual environment for the project

To check your environment information, use the command below

```bash
  poetry env info
```

If your python version is not compatible with the `python` requirement of the project, Poetry will find one that is and use it.

If it's unable to find a compatible version, you might need to install one. You can use [pyenv](https://github.com/pyenv/pyenv) to do so.

More on environments in the [docs](https://python-poetry.org/docs/managing-environments/#switching-between-environments)

## Run Locally

Clone the project

```bash
  git clone https://github.com/benthecoder/todocli.git
```

Go to the project directory

```bash
  cd todocli
```

Install dependencies with poetry

```bash
  poetry install
```

Run the `todocli.py` file with specific commands

```bash
  poetry run python todocli.py --commands
```

You can alias the command like below to shorten things down

```bash
  alias todo="poetry run python todocli.py"
```

## Usage/Examples

This is the list of commands available

```text
Commands:
  add          adds an item
  clear        removes all tasks
  complete     completes an item
  delete       deletes an item
  remove-done  removes all completed tasks
  show         show the todos in a table
  update       updates an item
```

### Adding a tasks

![add](assets/add.png)

### Updating a tasks

![update](assets/update.png)

### Completing a tasks

![complete](assets/complete.png)

### Deleting a tasks

![delete](assets/delete.png)

### Clear the table

```bash
todo clear
```

### Adding more category colors

The available categories with colors are in `COLORS` dictionary in `todocli.py`. To add more options, just populate the dictionary as follows

```py
{...,
"category_name": "color"
}
```

## Acknowledgements

- [Python Engineer tutorial on this TODO app](https://youtu.be/ynd67UwG_cI)
- This README file was created with [readme.so](https://readme.so/)
