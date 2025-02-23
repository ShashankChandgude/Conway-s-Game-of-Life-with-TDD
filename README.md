# Conway's Game of Life with TDD

This repository implements **Conway's Game of Life** using Python, following Test-Driven Development (TDD) principles. The project emphasizes simplicity, maintainability, and clean code by adhering to best practices such as DRY, KISS, and the Single Responsibility Principle (SRP).

## Project Overview

**Conway's Game of Life** is a cellular automaton devised by mathematician John Conway. The simulation consists of a grid of cells that evolve over time based on a set of simple rules:

- **Birth:** A dead cell with exactly three live neighbors becomes alive.
- **Survival:** A live cell with two or three live neighbors remains alive.
- **Death:** In all other cases, a cell dies or remains dead.

In this project, the core game logic is implemented in `src/game_of_life.py`, and an interactive graphical user interface (GUI) is provided via `src/start_simulation.py` (built using Pygame).

## Key Features

- **Game Logic:**  
  - Implements cell state transitions, neighbor signal generation, and next generation computation.
  - Provides helper functions for calculating grid bounds and simulating the game until extinction.
  - Fully covered by unit tests in `test/test_game_of_life.py`.

- **Graphical User Interface (GUI):**  
  - Displays a grid where live and dead cells are visualized.
  - Allows users to click on cells to toggle their state.
  - Provides three main controls:
    - **Next Gen:** Advances the simulation one generation.
    - **Start/Stop:** Toggles continuous simulation (with a 200 ms delay between generations).
    - **Clear:** Resets the board by killing all cells.
  - GUI code is excluded from automated tests to focus on game logic.

- **Test-Driven Development (TDD):**  
  - The project is developed using TDD, with comprehensive tests for the game logic.
  - Tests are located in `test/test_game_of_life.py`, and detailed test descriptions are provided in `tests.txt`.

- **Automation & Code Quality:**  
  - **Paver** is used to manage project tasks such as setup, testing, cleaning, and code quality analysis (using radon and coverage).
  - Refer to `pavement.py` for available commands:
    - `paver setup` – Installs all required packages.
    - `paver test` – Runs the unit tests and displays code coverage.
    - `paver clean` – Cleans up temporary files.
    - `paver radon` – Analyzes code complexity.
    - `paver run` – Launches the GUI simulation.

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YourUsername/Conway-s-Game-of-Life-with-TDD.git
   cd Conway-s-Game-of-Life-with-TDD
