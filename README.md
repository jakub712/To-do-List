To-Do List CLI App

A simple, interactive command-line to-do list application built with Python and JSON. Designed for local use with persistent task storage.
Features

    Add tasks with descriptions

    Mark tasks as complete

    Remove tasks from the list

    View all tasks with status indicators

    Input validation to prevent crashes

    Clean, color-coded menu using colorama

    JSON-based storage so your data persists between sessions

How It Works

    Tasks are stored in a file called tasks.json as dictionaries with "text" and "done" keys.

    Menu options are number-based (1–5) and can be entered repeatedly during the session.

    Typing 0 when asked for a task input (in add, complete, or remove) will cancel the operation and return to viewing your current list.

Sample tasks.json Structure

{
  "tasks": [
    {
      "text": "Finish Python project",
      "done": false
    },
    {
      "text": "Submit job applications",
      "done": true
    }
  ]
}

How to Run

    Ensure you have Python 3 installed.

    Install the colorama package:

pip install colorama

Create a tasks.json file with the following content (if one doesn’t exist yet):

{
  "tasks": []
}

Run the app:

    python your_script_name.py

Tech Stack

    Python 3

    json module

    colorama for terminal colors
    
