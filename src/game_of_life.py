from enum import Enum

class CellState(Enum):
    ALIVE = 1
    DEAD = 0


def next_state(current_state, number_of_life_neighbors):
    return CellState.ALIVE if number_of_life_neighbors == 3 or (current_state == CellState.ALIVE and number_of_life_neighbors == 2) else CellState.DEAD

def generate_signals_for_a_cell(cell):
    x, y = cell
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    return [(x + dx, y + dy) for dx, dy in directions]

def generate_signals_from_multiple_cells(cells):
    return sum([generate_signals_for_a_cell(cell) for cell in cells], [])

def count_cell_signals(signals):
    return {signal: signals.count(signal) for signal in signals}

def next_generation(live_cells):
    signal_counts = count_cell_signals(generate_signals_from_multiple_cells(live_cells))
    
    def cell_lives(cell, number_of_life_neighbors):
        return next_state(CellState.ALIVE if cell in live_cells else CellState.DEAD, number_of_life_neighbors) == CellState.ALIVE
    
    return {cell for cell, count in signal_counts.items() if cell_lives(cell, count)}

def get_bounds(cells):
    offset = 10
    
    if not cells:
        return (0, 0), (offset, offset)

    xs, ys = zip(*cells)
    return ((min(xs) - offset, min(ys) - offset), (max(xs) + offset, max(ys) + offset))

def simulate_until_extinction(live_cells, max_iterations=1000):
    iteration = 0
    current = live_cells
    while current and iteration < max_iterations:
        next_gen_cells = next_generation(current)
        if next_gen_cells == current:
            break
        current = next_gen_cells
        iteration += 1
    return current, iteration

