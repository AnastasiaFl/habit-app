# Habit tracking application

## Table of Contents

- [Project Description](#project-description)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)

## Project Description

The purpose of this project is to provide a user a habit tracking application. Here, a user can create new habits, 
check-off and delete them, collect useful analytics.

## Getting Started

### Prerequisites

Python version <= 3.7

### Installation

To install and set up the project, follow next steps:

1. Clone the repository:

   ```sh
   git clone https://github.com/AnastasiaFl/habit-app.git

## Usage
To use the application please run it on your IDE or
open terminal and go to root directory of the project, then write

    python main.py

The application should be started. Follow instructions placed in the console.

## Running Tests
To run the project's unit tests, please open terminal in the root directory of the project and 
run tests using following commands:

1. For running file_processor tests:
   ```sh
    python -m unittest tests/file_processor_tests.py
         
2. For running habit_processor tests:
   ```sh
    python -m unittest tests/habit_processor_tests.py 
   
3. For running checked_off_history_processor tests:
    ```sh
    python -m unittest tests/checked_off_history_processor_tests.py