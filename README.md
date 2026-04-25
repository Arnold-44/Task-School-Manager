# Task-School-Manager
#### Video Demo: https://youtu.be/ptOApWWquGw?si=K6Dd3nxTGZQLug9Z
#### Description:

**Task-School-Manager** is a Command-Line Interface (CLI) application designed to help students, specifically those at the **École Nationale Supérieure Polytechnique de Douala (ENSPD)**, to organize their academic workload and software development projects.

The project was born out of a personal need to bridge the gap between simple "to-do" lists and complex project management tools. As an engineering student, I often have to juggle between complex mathematics exercises, physics labs, and full-stack development tasks. This tool provides a streamlined way to track these responsibilities directly from the terminal.

### Key Features
- **Object-Oriented Design**: Uses a `Task` class to encapsulate data and logic.
- **Persistent Storage**: Saves and loads data automatically using JSON.
- **Professional UI**: Generates clean, readable tables using the `tabulate` library.
- **Robust CLI**: Implements `argparse` for a professional command-line experience.

### File Structure and Components

#### 1. `project.py`
This is the main entry point of the application. It contains the core logic divided into three main parts:
- **The Task Class**: Defines the structure of a task (title, category, priority, and status). It includes specific methods like `to_dict()` and `from_dict()` for data serialization, allowing objects to be stored in and retrieved from a JSON file.
- **Global Functions**: As per CS50P requirements, I implemented three core functions outside the class:
    - `add_task`: Handles the creation of new task objects and their addition to the main list.
    - `remove_task`: Manages the deletion of tasks with built-in error handling for invalid IDs.
    - `format_tasks`: Transforms the list of Python objects into a visually appealing grid using `tabulate`.
- **Main Function**: Uses `argparse` to parse user commands and coordinate between the file system and the application logic.

#### 2. `test_project.py`
This file contains the unit tests for the three required global functions. Using `pytest`, I verified:
- That tasks are correctly instantiated and added to the list.
- That the removal logic correctly handles index offsets (converting user-friendly 1-based indexing to Python's 0-based indexing).
- That the formatting function correctly identifies and displays task data.

#### 3. `requirements.txt`
Lists the external dependencies required for the project. For this application, the primary external library is `tabulate`.

#### 4. `tasks.json`
The database file where all tasks are stored in a structured format. This ensures that your progress is never lost when you close your Ubuntu terminal.

### Design Choices
During development, I made several strategic choices:
- **JSON over CSV**: I chose JSON because it maps perfectly to Python dictionaries, making the `from_dict` factory method more intuitive and scalable for future updates.
- **Error Handling**: I implemented `try...except` blocks in the loading and removal functions to ensure the program doesn't crash when files are missing or users provide incorrect input.
- **Priority System**: I implemented a numerical priority system (1 to 3) to help students focus on high-stakes exams or urgent coding bugs first.

### How to Use
On an Ubuntu environment, you can interact with the manager using the following commands:
- **Add a task**: `python project.py --add "Maths Revision" --cat "ENSPD" --prio 1`
- **View tasks**: `python project.py --list`
- **Complete a task**: `python project.py --finish [ID]`
- **Delete a task**: `python project.py --delete [ID]`

This project represents the culmination of my learning in CS50P combining file I/O, OOP, and professional CLI development.