import unittest
from parameterized import parameterized
from src.game_of_life import *


class TestGameOfLife(unittest.TestCase):

    def test_canary(self):
        self.assertTrue(True)

    @parameterized.expand(
        [
            (CellState.DEAD, 0, CellState.DEAD),
            (CellState.DEAD, 1, CellState.DEAD),
            (CellState.DEAD, 2, CellState.DEAD),
            (CellState.DEAD, 5, CellState.DEAD),
            (CellState.DEAD, 8, CellState.DEAD),
            (CellState.DEAD, 3, CellState.ALIVE),
        ]
    )
    def test_dead_cell_behavior(self, current_state, number_of_life_neighbors, expected_output):
        self.assertEqual(next_state(current_state, number_of_life_neighbors), expected_output)

    @parameterized.expand(
        [
            (CellState.ALIVE, 1, CellState.DEAD),
            (CellState.ALIVE, 4, CellState.DEAD),
            (CellState.ALIVE, 8, CellState.DEAD),
            (CellState.ALIVE, 2, CellState.ALIVE),
            (CellState.ALIVE, 3, CellState.ALIVE),
        ]
    )
    def test_live_cell_behavior(
        self, current_state, number_of_life_neighbors, expected_output
    ):
        self.assertEqual(next_state(current_state, number_of_life_neighbors), expected_output)

    @parameterized.expand(
    [
        ((2, 3), [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)]),
        ((3, 3), [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]),
        ((2, 4), [(1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)]),
        ((0, 0), [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]),
    ]
)
    def test_generate_signals_for_a_cell(self, cell, expected_signals):
        self.assertCountEqual(generate_signals_for_a_cell(cell), expected_signals)

    @parameterized.expand(
        [
            ([], []),
            ([(2, 3)], [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)]),
            ([(2, 3), (3, 3)],
             [(1, 2), (1, 3), (1, 4),
              (2, 2), (2, 4),
              (3, 2), (3, 3), (3, 4),
              (2, 2), (2, 3), (2, 4),
              (3, 2), (3, 4),
              (4, 2), (4, 3), (4, 4)]),
            ([(2, 3), (3, 3), (2, 4)], 
             [(1, 2), (1, 3), (1, 4),
              (2, 2), (2, 4),
              (3, 2), (3, 3), (3, 4),

              (2, 2), (2, 3), (2, 4),
              (3, 2), (3, 4),
              (4, 2), (4, 3), (4, 4),

              (1, 3), (1, 4), (1, 5),
              (2, 3), (2, 5),
              (3, 3), (3, 4), (3, 5)])
        ]
    )
    def test_generate_signals_from_multiple_cells(self, cells, expected_signals):
        self.assertCountEqual(generate_signals_from_multiple_cells(cells), expected_signals)

    @parameterized.expand(
        [
            ([], {}),
            ([(1, 1)], {(1, 1): 1}),
            ([(1, 1), (2, 2)], {(1, 1) : 1, (2, 2) : 1}),
            ([(1, 1), (1, 1), (2, 2)], {(1, 1) : 2, (2, 2) : 1}),
         ]
    )
    def test_count_cell_signals(self, signals, cell_signal_counts):
        self.assertEqual(count_cell_signals(signals), cell_signal_counts)

    def test_next_generation_no_cells(self):
        self.assertEqual(next_generation(set()), set())

    def test_next_generation_one_cell(self):
        self.assertEqual(next_generation({(2, 3)}), set())

    def test_next_generation_two_neighboring_cells(self):
        current_gen = {(1, 1), (1, 2)}
        expected_next_gen = set()

        self.assertEqual(next_generation(current_gen), expected_next_gen)

    def test_next_generation_three_cells_triangle(self):
        current_gen = {(1, 1), (1, 2), (2, 1)}
        expected_next_gen = {(1, 1), (1, 2), (2, 1), (2, 2)}

        self.assertEqual(next_generation(current_gen), expected_next_gen)

    def test_next_generation_block(self):
        current_gen = {(1, 1), (1, 2), (2, 1), (2, 2)}
        expected_next_gen = {(1, 1), (1, 2), (2, 1), (2, 2)}

        self.assertEqual(next_generation(current_gen), expected_next_gen)

    def test_next_generation_beehive(self):
        current_gen = {(2, 1), (3, 2), (3, 3), (2, 4), (1, 3), (1, 2)}
        expected_next_gen = {(2, 1), (3, 2), (3, 3), (2, 4), (1, 3), (1, 2)}

        self.assertEqual(next_generation(current_gen), expected_next_gen)

    def test_next_generation_horizontal_blinker(self):
        current_gen = {(2, 2), (2, 3), (2, 4)}
        expected_next_gen = {(1, 3), (2, 3), (3, 3)}

        self.assertEqual(next_generation(current_gen), expected_next_gen)

    def test_next_generation_vertical_blinker(self):
        current_gen = {(1, 3), (2, 3), (3, 3)}
        expected_next_gen = {(2, 2), (2, 3), (2, 4)}

        self.assertEqual(next_generation(current_gen), expected_next_gen)

    def test_next_generation_glider(self):
        current_gen = {(1, 1), (1, 2), (2, 2), (2, 3), (3, 1)}
        expected_next_gen = {(1, 1), (1, 2), (1, 3), (2, 3), (3, 2)}

        self.assertEqual(next_generation(current_gen), expected_next_gen)

    @parameterized.expand(
    [
        ([], ((0, 0), (10, 10))),
        ([(5, 5)], ((-5, -5), (15, 15))),
        ([(1, 3), (5, 2)], ((-9, -8), (15, 13))),
        ([(15, 1),(5, 10),(10, 20)], ((-5, -9), (25, 30))),
        ([(5, 5),(20, 10), (10, 20), (1, 15)], ((-9, -5), (30, 30))),
    ])
    def test_get_bounds(self, cells, expected_bounds):
        self.assertEqual(get_bounds(cells), expected_bounds)
        
    def test_simulate_until_extinction_single_cell(self):
        # A single cell should eventually die.
        final, iterations = simulate_until_extinction({(1, 1)})
        self.assertEqual(final, set())
        self.assertGreater(iterations, 0)

    def test_simulate_until_extinction_block(self):
        # A stable block should remain unchanged and require 0 iterations.
        block = {(1, 1), (1, 2), (2, 1), (2, 2)}
        final, iterations = simulate_until_extinction(block)
        self.assertEqual(final, block)
        self.assertEqual(iterations, 0)

    def test_simulate_until_extinction_oscillator(self):
        # An oscillator (blinker) is not extinct; with a low max_iterations it stops at that limit.
        blinker = {(2, 2), (2, 3), (2, 4)}
        final, iterations = simulate_until_extinction(blinker, max_iterations=5)
        self.assertNotEqual(final, set())
        self.assertEqual(iterations, 5)


if __name__ == "__main__":
    unittest.main()

