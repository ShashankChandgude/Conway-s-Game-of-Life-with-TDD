Conway's Game of Life with TDD
This repository implements Conway's Game of Life using Python, following Test-Driven Development (TDD) principles. The project emphasizes simplicity, maintainability, and clean code through the use of best practices such as DRY, KISS, and the Single Responsibility Principle.

Project Overview
Conway's Game of Life is a classic cellular automaton devised by mathematician John Conway. The simulation consists of a grid of cells that evolve over time based on simple rules:

Birth: A dead cell with exactly three live neighbors becomes alive.
Survival: A live cell with two or three live neighbors remains alive.
Death: In all other cases, a cell dies or remains dead.
In this project, the game logic is implemented in src/game_of_life.py, while the interactive graphical user interface (GUI) is implemented in src/start_simulation.py using Pygame.

Key Features
Game Logic:

Implements cell state transitions using a simple rule set.
Generates neighbor signals, counts them, and computes the next generation.
Provides helper functions to compute grid bounds and simulate the game until extinction.
Graphical User Interface (GUI):

Displays the grid with live and dead cells.
Allows users to toggle cell states by clicking on the grid.
Provides three buttons:
Next Gen: Advances the simulation one generation.
Start/Stop: Toggles continuous simulation (with a 200 ms delay per generation).
Clear: Clears the board (kills all cells).
Test-Driven Development (TDD):

All core game logic is covered by unit tests located in test/test_game_of_life.py.
The tests validate cell behavior, signal generation, next generation computation, grid bounds, and the simulation until extinction.
GUI code is excluded from test coverage to focus testing on game logic.
Task Automation:

Paver is used to manage project tasks such as setup, testing, cleaning, and code quality analysis.
Refer to pavement.py for available commands:
paver setup – Installs all required packages.
paver test – Runs the unit tests with coverage.
paver clean – Cleans up temporary files.
paver radon – Runs radon to analyze code complexity.
paver run – Launches the GUI simulation.
Installation and Setup
Clone the Repository:

bash
Copy
git clone https://github.com/YourUsername/Conway-s-Game-of-Life-with-TDD.git
cd Conway-s-Game-of-Life-with-TDD
Create and Activate a Virtual Environment (Optional but Recommended):

bash
Copy
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
Install Dependencies:

bash
Copy
paver setup
This command installs all packages listed in requirements.txt.

Running the Application
To start the GUI simulation, simply run:

bash
Copy
paver run
This opens a window where you can:

Click on cells to toggle their state.
Click Next Gen to advance one generation.
Click Start/Stop to toggle continuous simulation.
Click Clear to reset the grid.
Running the Tests
To run the unit tests for the game logic:

bash
Copy
paver test
This command runs the tests (excluding the GUI code) and reports code coverage.

Code Quality
The project uses radon for code complexity analysis. The paver radon task checks that the core game logic adheres to maintainable complexity levels. If you encounter complexity issues, consider refactoring parts of the code to further simplify them.

Project Structure
bash
Copy
├── src
│   ├── __init__.py
│   ├── game_of_life.py       # Core game logic
│   └── start_simulation.py   # Pygame-based GUI
├── test
│   └── test_game_of_life.py  # Unit tests for game logic
├── tests.txt               # Test descriptions
├── pavement.py             # Paver tasks for automation
├── requirements.txt        # Project dependencies
└── README.md               # Project description (this file)
Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

License
This project is open-source and available under the MIT License.

